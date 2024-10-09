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
    """This class is responsible for dispatching gateway events to multiple handlers."""

    def __init__(
        self,
        loop: asyncio.AbstractEventLoop,
        logger: logging.Logger = logging.getLogger(__name__),
    ) -> None:
        """
        Initialize the dispatcher.

        :param loop: The event loop to use.
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
        self.one_time_handlers: typing.Dict[
            GatewayReceiveOpcode,
            typing.List[
                typing.Callable[
                    [GatewayEventPayload[GatewayReceiveOpcode, typing.Any]],
                    typing.Awaitable[None],
                ]
            ],
        ] = {}
        self.one_time_futures: typing.Dict[
            GatewayReceiveOpcode, typing.List[asyncio.Future[typing.Any]]
        ] = {}
        self._loop = loop
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

    @typing.overload
    def on_next(
        self,
        opcode: typing.Literal[GatewayReceiveOpcode.HELLO],
        handler: typing.Callable[[GatewayHelloEventPayload], typing.Awaitable[None]],
    ) -> None: ...

    @typing.overload
    def on_next(
        self,
        opcode: typing.Literal[GatewayReceiveOpcode.RECONNECT],
        handler: typing.Callable[
            [GatewayReconnectEventPayload], typing.Awaitable[None]
        ],
    ) -> None: ...

    @typing.overload
    def on_next(
        self,
        opcode: typing.Literal[GatewayReceiveOpcode.HEARTBEAT],
        handler: typing.Callable[
            [GatewayHeartbeatEventPayload], typing.Awaitable[None]
        ],
    ) -> None: ...

    @typing.overload
    def on_next(
        self,
        opcode: typing.Literal[GatewayReceiveOpcode.HEARTBEAT_ACK],
        handler: typing.Callable[
            [GatewayHeartbeatAcknowledgeEventPayload], typing.Awaitable[None]
        ],
    ) -> None: ...

    @typing.overload
    def on_next(
        self,
        opcode: typing.Literal[GatewayReceiveOpcode.DISPATCH],
        handler: typing.Callable[
            [GatewayDispatchEventPayload[typing.Any]],
            typing.Awaitable[None],
        ],
    ) -> None: ...

    def on_next(
        self,
        opcode: GatewayReceiveOpcode,
        handler: typing.Any,
    ) -> None:
        """
        Register a one-time handler for an event. This handler will be called once
        and then removed.

        :param opcode: The opcode of the event to register the handler for.
        :param handler: The handler to register.
        """
        if opcode not in self.one_time_handlers:
            self.one_time_handlers[opcode] = []

        self.one_time_handlers[opcode].append(handler)

    @typing.overload
    def next(
        self,
        opcode: typing.Literal[GatewayReceiveOpcode.HELLO],
    ) -> typing.Awaitable[GatewayHelloEventPayload]: ...

    @typing.overload
    def next(
        self,
        opcode: typing.Literal[GatewayReceiveOpcode.RECONNECT],
    ) -> typing.Awaitable[GatewayReconnectEventPayload]: ...

    @typing.overload
    def next(
        self,
        opcode: typing.Literal[GatewayReceiveOpcode.HEARTBEAT],
    ) -> typing.Awaitable[GatewayHeartbeatEventPayload]: ...

    @typing.overload
    def next(
        self,
        opcode: typing.Literal[GatewayReceiveOpcode.HEARTBEAT_ACK],
    ) -> typing.Awaitable[GatewayHeartbeatAcknowledgeEventPayload]: ...

    @typing.overload
    def next(
        self,
        opcode: typing.Literal[GatewayReceiveOpcode.DISPATCH],
    ) -> typing.Awaitable[GatewayDispatchEventPayload[typing.Any]]: ...

    def next(
        self,
        opcode: typing.Any,
    ) -> typing.Awaitable[typing.Any]:
        """
        Wait for the next event of the given opcode and return the payload.

        :param opcode: The opcode of the event to wait for.
        """
        future = self._loop.create_future()

        if opcode not in self.one_time_futures:
            self.one_time_futures[opcode] = []

        self.one_time_futures[opcode].append(future)

        return future

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

        if opcode in self.one_time_handlers:
            for handler in self.one_time_handlers[opcode]:
                self._logger.debug(
                    f"Dispatching event {opcode} to one-time handler {handler}"
                )

                if asyncio.iscoroutinefunction(handler):
                    await handler(payload)
                else:
                    handler(payload)

            self.one_time_handlers.pop(opcode)

        if opcode in self.one_time_futures:
            for future in self.one_time_futures[opcode]:
                self._logger.debug(
                    f"Dispatching event {opcode} to one-time future {future}"
                )

                future.set_result(payload)

            self.one_time_futures.pop(opcode)
