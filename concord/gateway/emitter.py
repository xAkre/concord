import asyncio
import enum
import logging
import typing

import aiohttp

__all__ = ("GatewayMessageEmitter",)


class GatewayMessageEmitter:
    """
    This class is responsible for emitting messages to the gateway.

    It uses a priority queue to ensure that messages can be prioritized.

    :ivar session: The aiohttp.ClientSession instance.
    :ivar queue: The priority queue.
    """

    def __init__(
        self,
        session: aiohttp.ClientSession,
        logger: logging.Logger = logging.getLogger(__name__),
    ):
        """
        Initialize the emitter with the given session.

        :param session: The aiohttp.ClientSession instance.
        :param logger: The logger to use. Defaults to the logger of this module.
        """
        self.session = session
        self.queue: asyncio.PriorityQueue[typing.Any] = asyncio.PriorityQueue()
        self.logger = logger

    async def emit(self, message: dict, priority: int = 0):
        """
        Emit a message to the gateway.

        :param message: The message to emit.
        """
        self.logger.debug(f"Emitting message: {message}")
        await self.queue.put((priority, message))

    async def start(self):
        """Start the emitter."""
        while True:
            message = await self.queue.get()
            self.logger.debug(f"Sending message: {message}")
            await self.session.send_json(message)
