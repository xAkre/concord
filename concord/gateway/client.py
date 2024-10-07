import asyncio

import aiohttp

from concord.types.common import DiscordApiVersion

from .dispatcher import GatewayEventDispatcher
from .errors import GatewayConnectionException, GatewayException
from .heartbeat import HeartbeatHandler
from .intents import Intents
from .receiver import GatewayMessageReceiver
from .sender import GatewayMessageSender
from .types.receive import GatewayHelloEventPayload, GatewayReceiveOpcode

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
    ) -> None:
        """
        Initialize the gateway client.

        :param intents: The intents to request.
        :param api_version: The API version to use.
        """
        self.intents = intents
        self.api_version = api_version
        self._dispatcher = GatewayEventDispatcher()
        self._receiver = GatewayMessageReceiver()
        self._sender = GatewayMessageSender()
        self._heartbeat_handler = HeartbeatHandler()
        self._session: aiohttp.ClientSession | None = None
        self._ws: aiohttp.ClientWebSocketResponse | None = None

    async def start(self) -> None:
        """Start the gateway client."""
        await self._establish_connection()
        self._setup_receiver()
        self._setup_sender()
        self._register_handlers()

    async def close(self) -> None:
        """Close the gateway client."""
        await self._receiver.stop()
        await self._sender.stop()

        if self._ws:
            await self._ws.close()

        if self._session:
            await self._session.close()

    async def _establish_connection(self) -> None:
        """Establish a connection to the gateway."""
        self._session = aiohttp.ClientSession()

        try:
            self._ws = await self._session.ws_connect(self._get_ws_url())
        except aiohttp.WSServerHandshakeError as e:
            raise GatewayConnectionException("Failed to connect to the gateway.") from e

    def _setup_receiver(self) -> None:
        """Setup the receiver."""
        if self._ws is None:
            raise GatewayException("WebSocket is not established.")

        self._receiver.start(self._ws, self._dispatcher)

    def _setup_sender(self) -> None:
        """Setup the sender."""
        if self._ws is None:
            raise GatewayException("WebSocket is not established.")

        self._sender.start(self._ws)

    def _register_handlers(self) -> None:
        """Register the required handlers for the client to function."""
        self._dispatcher.register_handler(
            GatewayReceiveOpcode.HELLO, self._handle_hello
        )

    async def _handle_hello(self, payload: GatewayHelloEventPayload) -> None:
        """Handle the hello event."""
        self._heartbeat_handler.start(
            payload["d"]["heartbeat_interval"], self._dispatcher, self._sender
        )

    def _get_ws_url(self) -> str:
        """Get the WebSocket URL for the gateway."""
        return f"wss://gateway.discord.gg/?v={self.api_version}&encoding=json"
