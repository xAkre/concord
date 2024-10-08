import asyncio
import logging

import aiohttp

from concord.types.common import DiscordApiVersion

from .dispatcher import GatewayEventDispatcher
from .errors import GatewayConnectionException, GatewayException
from .heartbeat import HeartbeatHandler
from .intents import Intents
from .receiver import GatewayMessageReceiver
from .sender import GatewayMessageSender
from .types.receive import GatewayHelloEventPayload, GatewayReceiveOpcode
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
        self._dispatcher = GatewayEventDispatcher()
        self._receiver = GatewayMessageReceiver()
        self._sender = GatewayMessageSender()
        self._heartbeat_handler = HeartbeatHandler()
        self._session: aiohttp.ClientSession | None = None
        self._ws: aiohttp.ClientWebSocketResponse | None = None
        self._token: str | None = None

    async def start(self, token: str) -> None:
        """
        Start the gateway client.

        :param token: The token to use for authentication.
        """
        self._token = token

        self._logger.info("Starting gateway client")
        await self._establish_connection()
        self._setup_receiver()
        self._setup_sender()
        self._register_handlers()

        if self._receiver._receive_loop_task and self._sender._send_loop_task:
            self._logger.info("Gateway client started")
            await asyncio.gather(
                self._receiver._receive_loop_task,
                self._sender._send_loop_task,
            )

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

        raise asyncio.CancelledError

    async def _establish_connection(self) -> None:
        """Establish a connection to the gateway."""
        self._logger.debug("Establishing connection to the gateway")
        self._session = aiohttp.ClientSession()

        try:
            self._ws = await self._session.ws_connect(self._get_ws_url())
        except aiohttp.WSServerHandshakeError as e:
            raise GatewayConnectionException("Failed to connect to the gateway.") from e

    def _setup_receiver(self) -> None:
        """Setup the receiver."""
        self._logger.debug("Setting up receiver")

        if self._ws is None:
            raise GatewayException("WebSocket is not established.")

        self._receiver.start(self._ws, self._dispatcher)

    def _setup_sender(self) -> None:
        """Setup the sender."""
        self._logger.debug("Setting up sender")

        if self._ws is None:
            raise GatewayException("WebSocket is not established.")

        self._sender.start(self._ws)

    def _register_handlers(self) -> None:
        """Register the required handlers for the client to function."""
        self._logger.debug("Registering handlers")
        self._dispatcher.register_handler(
            GatewayReceiveOpcode.HELLO, self._handle_hello
        )

    async def _handle_hello(self, payload: GatewayHelloEventPayload) -> None:
        """Handle the hello event."""
        self._logger.debug("Starting heartbeat handler")
        self._heartbeat_handler.start(
            payload["d"]["heartbeat_interval"], self._dispatcher, self._sender
        )
        await self._identify()

    async def _identify(self) -> None:
        """Identify with the gateway."""
        self._logger.debug("Identifying with the gateway")

        if self._token is None:
            raise GatewayException("Token is not set.")

        await self._sender.send(
            GatewayIdentifyMessage(
                data=GatewayIdentifyMessageData(
                    token=self._token,
                    intents=int(self.intents),
                    properties=GatewayIdentifyMessageConnectionProperties(
                        os="linux",
                        browser="concord",
                        device="concord",
                    ),
                )
            )
        )

    def _get_ws_url(self) -> str:
        """Get the WebSocket URL for the gateway."""
        return f"wss://gateway.discord.gg/?v={self.api_version}&enc=json"
