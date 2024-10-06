import typing

from .common import GatewayEventPayload, GatewayReceiveOpcode

__all__ = (
    "GatewayHelloEventPayloadData",
    "GatewayHelloEventPayload",
    "GatewayReconnectEventPayload",
)


class GatewayHelloEventPayloadData(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#hello)
    for Discord's documentation.
    """

    heartbeat_interval: int


GatewayHelloEventPayload = GatewayEventPayload[
    typing.Literal[GatewayReceiveOpcode.HELLO], GatewayHelloEventPayloadData
]

GatewayReconnectEventPayload = GatewayEventPayload[
    typing.Literal[GatewayReceiveOpcode.RECONNECT], typing.Literal[None]
]
