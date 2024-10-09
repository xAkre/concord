import asyncio
import logging
import typing

from .dispatcher import GatewayEventDispatcher
from .errors import GatewayException
from .sender import GatewayMessageSender
from .types.receive import (
    GatewayDispatchEventPayload,
    GatewayHeartbeatAcknowledgeEventPayload,
    GatewayHeartbeatEventPayload,
    GatewayReceiveOpcode,
)
from .types.send import GatewayHeartbeatMessage

__all__ = ("GatewayHeartbeatHandler",)


class GatewayHeartbeatHandler:
    """This class is responsible for handling heartbeats for a gateway client."""

    def __init__(
        self,
        loop: asyncio.AbstractEventLoop,
        logger: logging.Logger = logging.getLogger(__name__),
    ) -> None:
        """
        Initialize the heartbeat handler.

        :param loop: The event loop to use.
        :param logger: The logger to use. Defaults to the logger of this module.
        """
        self._loop = loop
        self._logger = logger
        self._heartbeat_interval_ms: float | None = None
        self._last_sequence_number: int | None = None
        self._last_heartbeat_acknowledged: bool = True
        self._heartbeat_loop_task: asyncio.Task[None] | None = None
        self._dispatcher: GatewayEventDispatcher | None = None
        self._sender: GatewayMessageSender | None = None

    def start(
        self,
        interval_ms: float,
        dispatcher: GatewayEventDispatcher,
        sender: GatewayMessageSender,
    ) -> asyncio.Task[None]:
        """
        Start the handler.

        :param interval_ms: The interval in milliseconds at which to send heartbeats.
        :param dispatcher: The dispatcher to use to register event handlers
                           required for the handler to work.
        :param sender: The sender to use to send heartbeat messages.
        :return: The task running the heartbeat loop.
        """
        self._logger.debug("Starting heartbeat handler")

        self._heartbeat_interval_ms = interval_ms
        self._dispatcher = dispatcher
        self._sender = sender

        self._register_handlers()
        self._heartbeat_loop_task = self._loop.create_task(self._heartbeat_loop())

        return self._heartbeat_loop_task

    async def stop(self) -> None:
        """Stop the handler."""
        if (
            self._heartbeat_loop_task is not None
            and not self._heartbeat_loop_task.done()
        ):
            self._logger.debug("Stopping heartbeat handler")
            self._heartbeat_loop_task.cancel()

            try:
                await self._heartbeat_loop_task
            except asyncio.CancelledError:
                self._logger.debug("Stopped heartbeat handler")
                raise

    def _register_handlers(self) -> None:
        """Register the handlers required for the handler to work."""
        if self._dispatcher is None:
            raise GatewayException("Dispatcher not set")

        self._dispatcher.register_handler(
            GatewayReceiveOpcode.HEARTBEAT, self._on_heartbeat
        )
        self._dispatcher.register_handler(
            GatewayReceiveOpcode.HEARTBEAT_ACK, self._on_heartbeat_acknowledge
        )
        self._dispatcher.register_handler(
            GatewayReceiveOpcode.DISPATCH, self._on_dispatch
        )

    async def _heartbeat_loop(self) -> None:
        """Send heartbeats at the specified interval."""
        if self._heartbeat_interval_ms is None:
            raise GatewayException("Heartbeat interval not set")

        self._logger.debug("Starting heartbeat loop")

        while True:
            if not self._last_heartbeat_acknowledged:
                self._logger.debug("Heartbeat not acknowledged, stopping")
                break

            await self._send_heartbeat()
            self._last_heartbeat_acknowledged = False

            await asyncio.sleep(self._heartbeat_interval_ms / 1000)

    async def _send_heartbeat(self) -> None:
        """Send a heartbeat to the gateway."""
        if self._sender is None:
            raise GatewayException("Sender not set")

        self._logger.debug("Sending heartbeat")
        await self._sender.send(
            GatewayHeartbeatMessage(data=self._last_sequence_number)
        )

    async def _on_heartbeat(self, _: GatewayHeartbeatEventPayload) -> None:
        """Handle a heartbeat event by sending a heartbeat back."""
        await self._send_heartbeat()

    async def _on_heartbeat_acknowledge(
        self, _: GatewayHeartbeatAcknowledgeEventPayload
    ) -> None:
        """
        Handle a heartbeat acknowledge event by setting the last heartbeat to
        acknowledged.
        """
        self._logger.debug("Received heartbeat acknowledge")
        self._last_heartbeat_acknowledged = True

    async def _on_dispatch(
        self, payload: GatewayDispatchEventPayload[typing.Any]
    ) -> None:
        """Handle a dispatch event by updating the last sequence number."""
        self._last_sequence_number = payload["s"]
