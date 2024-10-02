from concord.gateway.client import GatewayClient
from concord.gateway.enums import DiscordAPIVersion, GatewayReceiveOpcode
from concord.gateway.intents import Intents
from concord.gateway.types import GatewayDispatchEventPayload


class DispatchClient:
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

    async def _handle_dispatch(self, payload: GatewayDispatchEventPayload) -> None:
        event_name = payload["t"]
        event_data = payload["d"]


__all__ = ["DispatchClient"]
