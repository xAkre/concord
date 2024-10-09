import asyncio
import logging

import aiohttp

from .dispatcher import GatewayEventDispatcher

__all__ = ("GatewayMessageReceiver",)


class GatewayMessageReceiver:
    """
    This class is repsonsible for receiving messages from the gateway and
    passing them on to the dispatcher.
    """

    def __init__(
        self,
        loop: asyncio.AbstractEventLoop,
        logger: logging.Logger = logging.getLogger(__name__),
    ) -> None:
        """
        Initialize the receiver.

        :param loop: The event loop to use.
        :param logger: The logger to use. Defaults to the logger of this module.
        """
        self._loop = loop
        self._logger = logger
        self._receive_loop_task: asyncio.Task[None] | None = None

    def start(
        self, ws: aiohttp.ClientWebSocketResponse, dispatcher: GatewayEventDispatcher
    ) -> asyncio.Task[None]:
        """
        Start the receiver with the given websocket and dispatcher.

        :param ws: The websocket to receive from.
        :param dispatcher: The dispatcher to pass messages to.
        :return: The task running the receive loop.
        """
        self._logger.debug("Starting receiver")
        self._receive_loop_task = self._loop.create_task(
            self._receive_loop(ws, dispatcher)
        )

        return self._receive_loop_task

    async def stop(self) -> None:
        """Stop the receiver."""
        self._logger.debug("Stopping receiver")

        if self._receive_loop_task:
            self._receive_loop_task.cancel()

            try:
                await self._receive_loop_task
            except asyncio.CancelledError:
                self._logger.debug("Receiver stopped")
                raise

    async def _receive_loop(
        self, ws: aiohttp.ClientWebSocketResponse, dispatcher: GatewayEventDispatcher
    ) -> None:
        """
        Receive messages from the websocket until cancelled and pass them on to
        the dispatcher.

        :param ws: The websocket to receive from.
        :param dispatcher: The dispatcher to pass messages to.
        """
        while True:
            message = await ws.receive()

            if message.type == aiohttp.WSMsgType.TEXT:
                self._logger.debug(f"Received message: {message}")
                json_data = message.json()
                await dispatcher.dispatch(json_data)
            else:
                self._logger.info(f"Received unexpected message: {message}")
                break
