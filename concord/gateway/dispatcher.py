import asyncio
import logging
import typing

from .types.receive import (
    GatewayDispatchEventPayload,
    GatewayEventPayload,
    GatewayHeartbeatAcknowledgeEventPayload,
    GatewayHeartbeatEventPayload,
    GatewayHelloEventPayload,
    GatewayReceiveOpcode,
    GatewayReconnectEventPayload,
)

__all__ = ("GatewayEventDispatcher",)


class GatewayEventDispatcher:
    """
    This class is responsible for dispatching gateway events to multiple handlers.

    :ivar handlers: A dictionary mapping opcodes to lists of handlers.
    """

    def __init__(self, logger: logging.Logger = logging.getLogger(__name__)) -> None:
        """
        Initialize the dispatcher.

        :param logger: The logger to use. Defaults to the logger of this module.
        """
        self.handlers: typing.Dict[
            GatewayReceiveOpcode,
            typing.List[
                typing.Callable[
                    [GatewayEventPayload[GatewayReceiveOpcode, typing.Any]],
                    typing.Awaitable[None],
                ]
            ],
        ] = {}
        self._logger = logger

    @typing.overload
    def register_handler(
        self,
        opcode: typing.Literal[GatewayReceiveOpcode.HELLO],
        handler: typing.Callable[[GatewayHelloEventPayload], typing.Awaitable[None]],
    ) -> None: ...

    @typing.overload
    def register_handler(
        self,
        opcode: typing.Literal[GatewayReceiveOpcode.RECONNECT],
        handler: typing.Callable[
            [GatewayReconnectEventPayload], typing.Awaitable[None]
        ],
    ) -> None: ...

    @typing.overload
    def register_handler(
        self,
        opcode: typing.Literal[GatewayReceiveOpcode.HEARTBEAT],
        handler: typing.Callable[
            [GatewayHeartbeatEventPayload], typing.Awaitable[None]
        ],
    ) -> None: ...

    @typing.overload
    def register_handler(
        self,
        opcode: typing.Literal[GatewayReceiveOpcode.HEARTBEAT_ACK],
        handler: typing.Callable[
            [GatewayHeartbeatAcknowledgeEventPayload], typing.Awaitable[None]
        ],
    ) -> None: ...

    @typing.overload
    def register_handler(
        self,
        opcode: typing.Literal[GatewayReceiveOpcode.DISPATCH],
        handler: typing.Callable[
            [GatewayDispatchEventPayload[typing.Any]],
            typing.Awaitable[None],
        ],
    ) -> None: ...

    def register_handler(
        self,
        opcode: GatewayReceiveOpcode,
        handler: typing.Any,
    ) -> None:
        """
        Register a handler for an event.

        :param opcode: The opcode of the event to register the handler for.
        :param handler: The handler to register.
        """
        if opcode not in self.handlers:
            self.handlers[opcode] = []

        self.handlers[opcode].append(handler)

    async def dispatch(
        self, payload: GatewayEventPayload[GatewayReceiveOpcode, typing.Any]
    ) -> None:
        """
        Dispatch an event to all registered handlers.

        :param payload: The payload of the event to dispatch.
        """
        opcode = payload["op"]

        if opcode not in GatewayReceiveOpcode:
            return

        if opcode in self.handlers:
            for handler in self.handlers[opcode]:
                self._logger.debug(f"Dispatching event {opcode} to handler {handler}")

                if asyncio.iscoroutinefunction(handler):
                    await handler(payload)
                else:
                    handler(payload)
