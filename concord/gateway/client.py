import asyncio
import logging
import platform
import typing

import aiohttp

from concord.types.common import DiscordApiVersion

from .dispatcher import GatewayEventDispatcher
from .errors import GatewayConnectionException
from .heartbeat import GatewayHeartbeatHandler
from .intents import Intents
from .receiver import GatewayMessageReceiver
from .sender import GatewayMessageSender
from .types.receive import GatewayReadyEventPayload, GatewayReceiveOpcode
from .types.send import (
    GatewayIdentifyMessage,
    GatewayIdentifyMessageConnectionProperties,
    GatewayIdentifyMessageData,
)

__all__ = ("GatewayClient",)


class GatewayClient:
    """
    This class is responsible for connecting all the parts of the gateway
    together into a single interface.
    """

    def __init__(
        self,
        intents: Intents,
        api_version: DiscordApiVersion = DiscordApiVersion.DEFAULT,
        logger: logging.Logger = logging.getLogger(__name__),
    ) -> None:
        """
        Initialize the gateway client.

        :param intents: The intents to request.
        :param api_version: The API version to use.
        :param logger: The logger to use. Defaults to the logger of this module.
        """
        self.intents = intents
        self.api_version = api_version
        self._logger = logger
        self._loop: asyncio.AbstractEventLoop | None = None
        self._dispatcher: GatewayEventDispatcher | None = None
        self._receiver: GatewayMessageReceiver | None = None
        self._sender: GatewayMessageSender | None = None
        self._heartbeat_handler: GatewayHeartbeatHandler | None = None
        self._session: aiohttp.ClientSession | None = None
        self._ws: aiohttp.ClientWebSocketResponse | None = None
        self._token: str | None = None
        self._loop_task: typing.Awaitable[typing.Any] | None = None

    async def start(self, token: str) -> None:
        """
        Start the gateway client.

        :param token: The token to use for authentication.
        """
        self._logger.info("Starting gateway client")
        self._token = token
        self._loop = asyncio.get_running_loop()

        await self._establish_connection()

        self._setup_dispatcher()
        self._setup_sender()
        self._setup_receiver()

        self._logger.debug("Waiting for hello message")
        assert self._dispatcher is not None
        hello_payload = await self._dispatcher.next(GatewayReceiveOpcode.HELLO)
        self._logger.debug("Received hello message")

        await self._setup_heartbeat(hello_payload["d"]["heartbeat_interval"])

        await self._identify()
        ready_payload: GatewayReadyEventPayload = await self._dispatcher.next(
            GatewayReceiveOpcode.DISPATCH
        )
        self._logger.debug("Identified with the gateway")
        self._logger.info(
            f"Connected to Discord as {ready_payload['d']['user']['username']}"
        )

        assert self._sender is not None and self._sender._send_loop_task is not None
        assert (
            self._receiver is not None and self._receiver._receive_loop_task is not None
        )
        assert (
            self._heartbeat_handler is not None
            and self._heartbeat_handler._heartbeat_loop_task is not None
        )

        self._loop_task = asyncio.gather(
            self._sender._send_loop_task,
            self._receiver._receive_loop_task,
            self._heartbeat_handler._heartbeat_loop_task,
        )

        await self._loop_task

    async def stop(self) -> None:
        """Stop the gateway client."""
        self._logger.info("Closing gateway client")

        if self._receiver:
            try:
                await self._receiver.stop()
            except asyncio.CancelledError:
                pass

        if self._sender:
            try:
                await self._sender.stop()
            except asyncio.CancelledError:
                pass

        if self._heartbeat_handler:
            try:
                await self._heartbeat_handler.stop()
            except asyncio.CancelledError:
                pass

        if self._ws:
            try:
                await self._ws.close()
            except asyncio.CancelledError:
                self._logger.debug("WebSocket closed")

        if self._session:
            try:
                await self._session.close()
            except asyncio.CancelledError:
                self._logger.debug("Session closed")

        self._logger.info("Gateway client closed")

    async def _establish_connection(self) -> None:
        """Establish a connection to the gateway."""
        self._logger.debug("Establishing connection to the gateway")
        self._session = aiohttp.ClientSession()

        try:
            self._ws = await self._session.ws_connect(self._get_ws_url())
            self._logger.debug("Connected to the gateway")
        except aiohttp.WSServerHandshakeError as e:
            raise GatewayConnectionException("Failed to connect to the gateway") from e

    def _setup_dispatcher(self) -> None:
        """Setup the dispatcher."""
        assert self._loop is not None, "Event loop is not set"

        self._logger.debug("Setting up dispatcher")
        self._dispatcher = GatewayEventDispatcher(self._loop)
        self._logger.debug("Dispatcher setup complete")

    def _setup_sender(self) -> None:
        """Setup the sender."""
        assert self._loop is not None, "Event loop is not set"
        assert self._ws is not None, "WebSocket is not established"

        self._sender = GatewayMessageSender(self._loop)
        self._sender.start(self._ws)

    def _setup_receiver(self) -> None:
        """Setup the receiver."""
        assert self._loop is not None, "Event loop is not set"
        assert self._ws is not None, "WebSocket is not established"
        assert self._dispatcher is not None, "Dispatcher is not set"

        self._receiver = GatewayMessageReceiver(self._loop)
        self._receiver.start(self._ws, self._dispatcher)

    async def _setup_heartbeat(self, interval_ms: int) -> None:
        """
        Setup the heartbeat handler.

        :param interval_ms: The interval in milliseconds to send heartbeats.
        """
        assert self._loop is not None, "Event loop is not set"
        assert self._ws is not None, "WebSocket is not established"
        assert self._dispatcher is not None, "Dispatcher is not set"
        assert self._sender is not None, "Sender is not set"

        self._heartbeat_handler = GatewayHeartbeatHandler(self._loop)
        self._heartbeat_handler.start(interval_ms, self._dispatcher, self._sender)

    async def _identify(self) -> None:
        """Identify with the gateway."""
        assert self._token is not None, "Token is not set"
        assert self._sender is not None, "Sender is not set"

        self._logger.debug("Identifying with the gateway")
        await self._sender.send(
            GatewayIdentifyMessage(
                data=GatewayIdentifyMessageData(
                    token=self._token,
                    intents=int(self.intents),
                    properties=GatewayIdentifyMessageConnectionProperties(
                        os=platform.system(),
                        browser="concord",
                        device="concord",
                    ),
                )
            )
        )

    def _get_ws_url(self) -> str:
        """Get the WebSocket URL for the gateway."""
        return f"wss://gateway.discord.gg/?v={self.api_version}&enc=json"
