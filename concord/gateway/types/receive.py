import enum
import typing

from .common import GatewayEventPayload

__all__ = (
    "GatewayReceiveOpcode",
    "GatewayHelloEventPayloadData",
    "GatewayHelloEventPayload",
    "GatewayReconnectEventPayload",
)


class GatewayReceiveOpcode(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/topics/opcodes-and-status-codes#gateway)
    for Discord's documentation.
    """

    DISPATCH = 0
    HEARTBEAT = 1
    RECONNECT = 7
    INVALID_SESSION = 9
    HELLO = 10
    HEARTBEAT_ACK = 11


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
