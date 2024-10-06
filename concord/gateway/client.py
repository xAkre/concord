import asyncio

import aiohttp

from concord.types.common import DiscordApiVersion

from .dispatcher import GatewayEventDispatcher
from .emitter import GatewayMessageEmitter
from .errors import GatewayConnectionException, GatewayException
from .intents import Intents
from .receiver import GatewayMessageReceiver
from .types.common import GatewayReceiveOpcode
from .types.receive import GatewayHelloEventPayload

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
    ):
        """
        Initialize the gateway client.

        :param intents: The intents to request.
        :param api_version: The API version to use.
        """
        self.intents = intents
        self.api_version = api_version
        self._dispatcher = GatewayEventDispatcher()
        self._receiver = GatewayMessageReceiver()
        self._emitter = GatewayMessageEmitter()
        self._session: aiohttp.ClientSession | None = None
        self._ws: aiohttp.ClientWebSocketResponse | None = None
        self._receiver_task: asyncio.Task | None = None
        self._emitter_task: asyncio.Task | None = None

    async def start(self):
        """Start the gateway client."""
        await self._establish_connection()
        await self._setup_receiver()
        await self._setup_emitter()
        await self._register_handlers()

    async def close(self):
        """Close the gateway client."""
        await self._receiver.stop()
        await self._emitter.stop()

        if self._receiver_task:
            self._receiver_task.cancel()
            await self._receiver_task

        if self._emitter_task:
            self._emitter_task.cancel()
            await self._emitter_task

        if self._ws:
            await self._ws.close()

        if self._session:
            await self._session.close()

    async def _establish_connection(self):
        """Establish a connection to the gateway."""
        self._session = aiohttp.ClientSession()

        try:
            self._ws = await self._session.ws_connect(self._get_ws_url())
        except aiohttp.WSServerHandshakeError as e:
            raise GatewayConnectionException("Failed to connect to the gateway.") from e

    async def _setup_receiver(self):
        """Setup the receiver."""
        if self._ws is None:
            raise GatewayException("WebSocket is not established.")

        self._receiver_task = asyncio.create_task(
            self._receiver.start(self._ws, self._dispatcher)
        )

    async def _setup_emitter(self):
        """Setup the emitter."""
        if self._ws is None:
            raise GatewayException("WebSocket is not established.")

        self._emitter_task = asyncio.create_task(self._emitter.start(self._ws))

    async def _register_handlers(self):
        """Register the required handlers for the client to function."""
        self._dispatcher.register_handler(
            GatewayReceiveOpcode.HELLO, self._handle_hello
        )

    async def _handle_hello(self, _: GatewayHelloEventPayload):
        """Handle the hello event."""
        pass

    def _get_ws_url(self) -> str:
        """Get the WebSocket URL for the gateway."""
        return f"wss://gateway.discord.gg/?v={self.api_version}&encoding=json"
