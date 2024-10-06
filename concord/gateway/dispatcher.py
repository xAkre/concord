import asyncio
import typing

from .types.common import GatewayEventPayload, GatewayReceiveOpcode
from .types.receive import GatewayHelloEventPayload, GatewayReconnectEventPayload

__all__ = ("GatewayEventDispatcher",)


class GatewayEventDispatcher:
    """
    This class is responsible for dispatching gateway events to multiple handlers.

    :ivar handlers: A dictionary mapping opcodes to lists of handlers.
    """

    def __init__(self) -> None:
        """Initialize the dispatcher."""
        self.handlers: typing.Dict[
            GatewayReceiveOpcode, typing.List[typing.Callable]
        ] = {}

    @typing.overload
    def register_handler(
        self,
        opcode: typing.Literal[GatewayReceiveOpcode.HELLO],
        handler: typing.Callable[[GatewayHelloEventPayload], None],
    ) -> None: ...

    @typing.overload
    def register_handler(
        self,
        opcode: typing.Literal[GatewayReceiveOpcode.RECONNECT],
        handler: typing.Callable[[GatewayReconnectEventPayload], None],
    ) -> None: ...

    def register_handler(
        self, opcode: GatewayReceiveOpcode, handler: typing.Callable
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
        self, opcode: GatewayReceiveOpcode, payload: GatewayEventPayload
    ) -> None:
        """
        Dispatch an event to all registered handlers.

        :param opcode: The opcode of the event to dispatch.
        :param payload: The payload of the event to dispatch.
        """
        if opcode in self.handlers:
            for handler in self.handlers[opcode]:
                if asyncio.iscoroutinefunction(handler):
                    await handler(payload)
                else:
                    handler(payload)
