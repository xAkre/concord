import typing

from .common import GatewayEventPayload, GatewayReceiveOpcode

__all__ = ("HelloPayloadData", "HelloPayload", "ReconnectPayload")


class HelloPayloadData(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#hello)
    for Discord's documentation.
    """

    heartbeat_interval: int


HelloPayload = GatewayEventPayload[
    typing.Literal[GatewayReceiveOpcode.HELLO], HelloPayloadData
]

ReconnectPayload = GatewayEventPayload[
    typing.Literal[GatewayReceiveOpcode.RECONNECT], typing.Literal[None]
]
