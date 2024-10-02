from __future__ import annotations

import asyncio
import json
import logging
import platform
import typing

import aiohttp

from concord.errors import ConcordException

from .constants import BASE_DISCORD_GATEWAY_URL
from .enums import DiscordAPIVersion, GatewayReceiveOpcode, GatewaySendOpcode
from .intents import Intents
from .types import (
    GatewayDispatchEventPayload,
    GatewayHeartbeatAcknowledgementEventPayload,
    GatewayHeartbeatEventPayload,
    GatewayHeartbeatMessage,
    GatewayHelloEventPayload,
    GatewayIdentifyMessage,
    GatewayMessage,
)


class ReconnectException(Exception):
    """Exception raised when the gateway client needs to reconnect."""

    pass


class HeartbeatHandler:
    """
    Handles the heartbeat mechanism for the Discord GatewayClient, ensuring that the
    client maintains an active connection by regularly sending heartbeats and handling
    server acknowledgments.

    :param client: The instance of `GatewayClient` to send heartbeats through.
    :param logger: A logger instance to log heartbeat activity.
    """

    def __init__(self, client: GatewayClient, logger: logging.Logger) -> None:
        """
        Initialize the HeartbeatHandler.

        :param client: The GatewayClient instance used to communicate with the Discord gateway.
        :param logger: A logger instance for logging heartbeat events.
        """
        self._client = client
        self._logger = logger
        self._interval_ms = 0
        self._acknowledged = True
        self._last_sequence_number: int | None = None
        self._task: asyncio.Task | None = None  # To control the heartbeat loop

        self._setup_hooks()

    def _setup_hooks(self) -> None:
        """
        Setup the necessary event hooks for handling heartbeat-related events from
        the Discord gateway. Hooks into HEARTBEAT_ACKNOWLEDGMENT, DISPATCH, and
        HEARTBEAT events.
        """
        self._client.hook_into(
            GatewayReceiveOpcode.HEARTBEAT_ACKNOWLEDGMENT,
            self._handle_heartbeat_acknowledgement,
        )
        self._client.hook_into(GatewayReceiveOpcode.DISPATCH, self._handle_dispatch)
        self._client.hook_into(
            GatewayReceiveOpcode.HEARTBEAT, self._handle_heartbeat_event
        )

    async def start(self, interval_ms: int) -> None:
        """
        Start the heartbeat loop with the specified interval.

        :param interval_ms: The interval in milliseconds at which to send heartbeats.
        """
        self._interval_ms = interval_ms
        self._acknowledged = True

        if self._task and not self._task.done():
            self._task.cancel()

        self._task = asyncio.create_task(self._heartbeat_loop())

    async def stop(self) -> None:
        """Stop the heartbeat loop gracefully by cancelling the ongoing heartbeat task."""
        if self._task:
            self._task.cancel()

            try:
                await self._task
            except asyncio.CancelledError:
                self._logger.info("Heartbeat task canceled.")

    async def _heartbeat_loop(self) -> None:
        """
        Continuously send heartbeats at the specified interval. If a heartbeat is not
        acknowledged by the server, a ReconnectException will be raised.

        :raises ReconnectException: If the heartbeat is not acknowledged by the server.
        """
        try:
            while True:
                if not self._acknowledged:
                    raise ReconnectException(
                        "Heartbeat was not acknowledged. Reconnecting..."
                    )

                await self._send_heartbeat()

                self._acknowledged = False
                await asyncio.sleep(self._interval_ms / 1000)
        except asyncio.CancelledError:
            self._logger.info("Heartbeat loop stopped.")

    async def _send_heartbeat(self) -> None:
        """Send a heartbeat message to the gateway."""
        self._logger.debug("Sending heartbeat...")

        await self._client._send(
            GatewayHeartbeatMessage(
                op=GatewaySendOpcode.HEARTBEAT, d=self._last_sequence_number
            )
        )

    async def _handle_heartbeat_acknowledgement(
        self, _: GatewayHeartbeatAcknowledgementEventPayload
    ) -> None:
        """
        Handle the receipt of a heartbeat acknowledgment from the server, confirming
        that the server received the last heartbeat message.

        :param _: The payload of the HEARTBEAT_ACKNOWLEDGMENT event (ignored in this method).
        """
        self._acknowledged = True
        self._logger.debug("Heartbeat acknowledged by server.")

    async def _handle_dispatch(self, payload: GatewayDispatchEventPayload) -> None:
        """
        Update the last sequence number on every dispatch event received from the server.

        :param payload: The payload of the DISPATCH event, which contains the latest
                        sequence number.
        """
        self._last_sequence_number = payload["s"]

    async def _handle_heartbeat_event(self, _: GatewayHeartbeatEventPayload) -> None:
        """
        Handle a HEARTBEAT event sent from the server by sending a heartbeat message back.

        :param _: The payload of the HEARTBEAT event (ignored in this method).
        """
        await self._send_heartbeat()


class GatewayClient:
    """
    A class that manages the WebSocket connection to the Discord gateway, handles
    heartbeats, identifies the client, and allows hooking into different gateway events.

    :param intents: The Discord intents for the connection.
    :param api_version: The Discord API version to use. Defaults to `DiscordAPIVersion.LATEST`.
    :param reconnect_attempts: The number of reconnection attempts before failing. Defaults to 5.
    """

    def __init__(
        self,
        intents: Intents | int,
        api_version: DiscordAPIVersion = DiscordAPIVersion.LATEST,
        reconnect_attempts: int = 5,
    ):
        """
        Initialize the GatewayClient.

        :param intents: The intents for the WebSocket connection.
        :param api_version: The Discord API version to use.
        :param reconnect_attempts: Number of reconnection attempts before giving up.
        """
        self._intents = intents
        self._api_version = api_version
        self._token: str | None = None
        # Assume the websocket is set so that we do not have to check for None
        self._ws: aiohttp.ClientWebSocketResponse = None  # type: ignore[assignment]
        self._queue: asyncio.Queue[GatewayMessage] = asyncio.Queue()
        self._last_sequence_number: int | None = None
        self._hooks: dict[GatewayReceiveOpcode, list[typing.Callable]] = {}
        self._is_identified = False
        self._reconnect_attempts = reconnect_attempts
        self._session: aiohttp.ClientSession | None = None
        self._logger = logging.getLogger("concord.gateway.client")
        self._heartbeat_handler = HeartbeatHandler(
            self, self._logger.getChild("heartbeat")
        )

    async def start(self, token: str) -> None:
        """
        Start the GatewayClient connection by establishing a WebSocket connection and
        entering the main loop.

        :param token: The bot token used to authenticate with Discord.
        """
        self._token = token
        await self._connect_and_run()

    async def _connect_and_run(self) -> None:
        """Establish connection and handle reconnection attempts automatically."""
        async with aiohttp.ClientSession() as session:
            self._session = session
            attempt = 0

            while attempt < self._reconnect_attempts:
                try:
                    await self._establish_connection()
                    await self._start_loop()
                except aiohttp.ClientError as e:
                    self._logger.error(f"Connection failed: {e}, reconnecting...")
                    attempt += 1
                    await asyncio.sleep(2**attempt)
                else:
                    break
            else:
                self._logger.critical("Max reconnect attempts reached. Shutting down.")

    async def _establish_connection(self) -> None:
        """
        Establish the WebSocket connection to the Discord gateway.

        :raises ConcordException: If the aiohttp session is not initialized.
        """
        ws_connection_url = self._get_ws_connection_url()

        if not self._session:
            raise ConcordException("Session not initialized")

        self._ws = await self._session.ws_connect(ws_connection_url)

    async def _start_loop(self) -> None:
        """Start the asynchronous tasks for sending and receiving WebSocket messages."""
        try:
            await asyncio.gather(self._send_loop(), self._receive_loop())
        except Exception as e:
            self._logger.error(f"Exception in gateway loop: {e}")
            raise

    async def _send_loop(self) -> None:
        """Continuously send messages from the queue to the WebSocket."""
        while True:
            message = await self._queue.get()
            self._logger.debug(
                f"Sending message with opcode: {message['op']} and data: {message['d']}"
            )
            await self._ws.send_json(message)

    async def _receive_loop(self) -> None:
        """
        Continuously receive and handle messages from the WebSocket. Raises a
        `ReconnectException` if the connection is closed or encounters an error.
        Automatically attempts to reconnect in case of disconnection.
        """
        try:
            async for msg in self._ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    self._logger.debug(f"Received message: {msg.data}")
                    await self._handle_message(msg.data)
                elif msg.type == aiohttp.WSMsgType.CLOSED:
                    self._logger.warning("WebSocket connection closed.")
                    raise ReconnectException("WebSocket connection closed.")
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    self._logger.error(f"WebSocket error: {msg.data}")
                    raise ReconnectException("WebSocket encountered an error.")
        except ReconnectException as e:
            self._logger.warning(f"Reconnection triggered: {e}")
            await self._reconnect()
        finally:
            await self._heartbeat_handler.stop()

    async def _reconnect(self) -> None:
        """
        Attempt to reconnect to the WebSocket after disconnection.
        Resets the identified state and attempts reconnection.
        """
        self._is_identified = False
        attempt = 0

        while attempt < self._reconnect_attempts:
            try:
                await self._establish_connection()
                await self._start_loop()
                break
            except aiohttp.ClientError:
                self._logger.warning(f"Reconnection attempt {attempt + 1} failed.")
                attempt += 1
                await asyncio.sleep(2**attempt)
        else:
            self._logger.critical(
                "Max reconnect attempts reached. Unable to reconnect."
            )

    async def _handle_message(self, message: str) -> None:
        """
        Handle an incoming message from the WebSocket by dispatching it to
        the appropriate handler.

        :param message: The JSON-encoded message received from Discord.
        """
        data = json.loads(message)
        op_code = GatewayReceiveOpcode(data["op"])

        self._logger.debug(f"Handling message with opcode: {op_code} and data: {data}")

        if op_code == GatewayReceiveOpcode.HELLO:
            await self._handle_hello(data)
        elif (
            op_code == GatewayReceiveOpcode.HEARTBEAT_ACKNOWLEDGMENT
            and not self._is_identified
        ):
            await self._identify()

        for callback in self._hooks.get(op_code, []):
            await callback(data)

    async def _send(self, message: typing.Any) -> None:
        """
        Queue a message to be sent to the WebSocket.

        :param message: The message to be sent, which must include the `op` code
                        and data (`d`).
        """
        self._logger.debug(
            f"Queuing message with opcode: {message['op']} and data: {message['d']}"
        )
        await self._queue.put(message)

    def _get_ws_connection_url(self) -> str:
        """
        Generate the WebSocket connection URL based on the API version and constants.

        :return: The WebSocket connection URL.
        """
        return f"{BASE_DISCORD_GATEWAY_URL}/?v={self._api_version}&enc=json"

    async def _identify(self) -> None:
        """
        Identify the client to Discord by sending an IDENTIFY message with the
        token and intents.
        """
        self._logger.debug("Identifying with Discord...")

        if not self._token:
            raise ConcordException("Token is not set")

        await self._send(
            GatewayIdentifyMessage(
                op=GatewaySendOpcode.IDENTIFY,
                d={
                    "token": self._token,
                    "intents": int(self._intents),
                    "properties": {
                        "os": platform.system(),
                        "browser": "concord",
                        "device": "concord",
                    },
                },
            )
        )

        self._is_identified = True

    async def _handle_hello(self, payload: GatewayHelloEventPayload) -> None:
        """
        Handle the HELLO event received from Discord and start the heartbeat handler.

        :param payload: The payload containing the heartbeat interval.
        """
        asyncio.create_task(
            self._heartbeat_handler.start(payload["d"]["heartbeat_interval"])
        )

    def hook_into(
        self,
        event: GatewayReceiveOpcode,
        callback: typing.Callable[
            [typing.Any], typing.Coroutine[typing.Any, typing.Any, None]
        ],
    ) -> None:
        """
        Hook into a specific gateway event to handle incoming messages.

        :param event: The event opcode to hook into.
        :param callback: A coroutine function to handle the event data.
        """
        if event not in self._hooks:
            self._hooks[event] = []

        self._hooks[event].append(callback)


__all__ = ["GatewayClient"]
