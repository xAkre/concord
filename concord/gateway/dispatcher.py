import asyncio
import typing

from concord.errors import ConcordException

from .client import GatewayClient
from .enums import (
    DiscordAPIVersion,
    GatewayDispatchEvent,
    GatewayDispatchEventCallbackName,
    GatewayReceiveOpcode,
)
from .intents import Intents
from .types import GatewayDispatchEventPayload, GatewayReadyEventPayload


class GatewayDispatcher:
    def __init__(
        self,
        intents: Intents,
        api_version: DiscordAPIVersion = DiscordAPIVersion.LATEST,
        reconnect_attempts: int = 5,
    ):
        self._gateway = GatewayClient(
            intents=intents,
            api_version=api_version,
            reconnect_attempts=reconnect_attempts,
        )
        self._gateway.hook_into(GatewayReceiveOpcode.DISPATCH, self._handle_dispatch)

    async def start(self, token: str) -> None:
        await self._gateway.start(token)

    async def _handle_dispatch(self, payload: GatewayDispatchEventPayload) -> None:
        event_name = payload["t"]
        event_data = payload["d"]

        callback_name = GatewayDispatchEventCallbackName[event_name]

        if hasattr(self, callback_name):
            if not asyncio.iscoroutinefunction(getattr(self, callback_name)):
                raise ConcordException(
                    f"Callback {callback_name} is not a coroutine function."
                )

            await getattr(self, callback_name)(event_data)

    def on(
        self, event: typing.Literal[GatewayDispatchEvent.READY]
    ) -> typing.Callable[
        [typing.Callable[[GatewayReadyEventPayload], typing.Coroutine]], typing.Callable
    ]:
        def decorator(
            func: typing.Callable[[GatewayReadyEventPayload], typing.Coroutine]
        ) -> typing.Callable[[GatewayReadyEventPayload], typing.Coroutine]:
            setattr(self, GatewayDispatchEventCallbackName.READY, func)
            return func

        return decorator


__all__ = ["GatewayDispatcher"]
