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
    """

    def __init__(
        self,
        logger: logging.Logger = logging.getLogger(__name__),
    ) -> None:
        """
        Initialize the emitter.

        :param logger: The logger to use. Defaults to the logger of this module.
        """
        self.queue: asyncio.PriorityQueue[typing.Any] = asyncio.PriorityQueue()
        self.logger = logger
        self._send_loop_task: asyncio.Task | None = None

    async def emit(self, message: dict, priority: int = 0) -> None:
        """
        Emit a message to the gateway.

        :param message: The message to emit.
        """
        self.logger.debug(f"Emitting message: {message}")
        await self.queue.put((priority, message))

    async def start(self, ws: aiohttp.ClientWebSocketResponse) -> None:
        """
        Start the emitter with the given websocket.

        :param ws: The websocket to emit messages to.
        """
        self._send_loop_task = asyncio.create_task(self._send_loop(ws))

    async def stop(self) -> None:
        """Stop the emitter."""
        if self._send_loop_task:
            self._send_loop_task.cancel()
            await self._send_loop_task

    async def _send_loop(self, ws: aiohttp.ClientWebSocketResponse) -> None:
        """
        Send messages to the websocket until cancelled.

        :param ws: The websocket to send messages to.
        """
        while True:
            message = await self.queue.get()
            self.logger.debug(f"Sending message: {message}")
            await ws.send_json(message)
