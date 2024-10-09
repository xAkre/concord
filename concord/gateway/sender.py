import asyncio
import logging
import typing

import aiohttp

from .types.send import GatewayMessage

__all__ = ("GatewayMessageSender",)


class GatewayMessageSender:
    """
    This class is responsible for sending messages to the gateway.

    It uses a priority queue to ensure that messages can be prioritized.
    """

    def __init__(
        self,
        loop: asyncio.AbstractEventLoop,
        logger: logging.Logger = logging.getLogger(__name__),
    ) -> None:
        """
        Initialize the sender.

        :param loop: The event loop to use.
        :param logger: The logger to use. Defaults to the logger of this module.
        """
        self._loop = loop
        self.queue: asyncio.PriorityQueue[
            typing.Tuple[int, GatewayMessage[typing.Any]]
        ] = asyncio.PriorityQueue()
        self._logger = logger
        self._send_loop_task: asyncio.Task[None] | None = None

    async def send(
        self, message: GatewayMessage[typing.Any], priority: int = 0
    ) -> None:
        """
        Send a message to the gateway.

        :param message: The message to send.
        """
        await self.queue.put((priority, message))

    def start(self, ws: aiohttp.ClientWebSocketResponse) -> asyncio.Task[None]:
        """
        Start the sender with the given websocket.

        :param ws: The websocket to emit messages to.
        :return: The task running the send loop.
        """
        self._logger.debug("Starting sender")
        self._send_loop_task = asyncio.create_task(self._send_loop(ws))

        return self._send_loop_task

    async def stop(self) -> None:
        """Stop the sender."""
        self._logger.debug("Stopping sender")

        if self._send_loop_task:
            self._send_loop_task.cancel()

            try:
                await self._send_loop_task
            except asyncio.CancelledError:
                self._logger.debug("Sender stopped")
                raise

    async def _send_loop(self, ws: aiohttp.ClientWebSocketResponse) -> None:
        """
        Send messages to the websocket until cancelled.

        :param ws: The websocket to send messages to.
        """
        while True:
            (_, message) = await self.queue.get()
            serialized = message.serialize()
            self._logger.debug(f"Sending message: {serialized}")
            await ws.send_str(serialized)
