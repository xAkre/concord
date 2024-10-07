import asyncio
import typing

from .types.receive import (
    GatewayEventPayload,
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

    def __init__(self) -> None:
        """Initialize the dispatcher."""
        self.handlers: typing.Dict[
            GatewayReceiveOpcode,
            typing.List[
                typing.Callable[
                    [GatewayEventPayload[GatewayReceiveOpcode, typing.Any]],
                    typing.Awaitable[None],
                ]
            ],
        ] = {}

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

    def register_handler(
        self,
        opcode: GatewayReceiveOpcode,
        handler: typing.Callable[
            [GatewayEventPayload[typing.Any, typing.Any]],
            typing.Awaitable[None],
        ],
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

        if not opcode in GatewayReceiveOpcode:
            return

        if opcode in self.handlers:
            for handler in self.handlers[opcode]:
                if asyncio.iscoroutinefunction(handler):
                    await handler(payload)
                else:
                    handler(payload)
