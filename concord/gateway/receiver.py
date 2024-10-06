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
        logger: logging.Logger = logging.getLogger(__name__),
    ) -> None:
        """
        Initialize the receiver.

        :param logger: The logger to use. Defaults to the logger of this module.
        """
        self._logger = logger
        self._receive_loop_task: asyncio.Task | None = None

    async def start(
        self, ws: aiohttp.ClientWebSocketResponse, dispatcher: GatewayEventDispatcher
    ) -> None:
        """
        Start the receiver with the given websocket and dispatcher.

        :param ws: The websocket to receive from.
        :param dispatcher: The dispatcher to pass messages to.
        """
        self._receive_loop_task = asyncio.create_task(
            self._receive_loop(ws, dispatcher)
        )

    async def stop(self) -> None:
        """Stop the receiver."""
        if self._receive_loop_task:
            self._receive_loop_task.cancel()
            await self._receive_loop_task

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
            self._logger.debug(f"Received message: {message}")
            json = message.json()
            await dispatcher.dispatch(json["op"], json)
