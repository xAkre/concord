import typing

from ..common import GatewayEventPayload, GatewayReceiveOpcode

__all__ = ("HelloPayloadData", "HelloPayload")


class HelloPayloadData(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#hello)
    for Discord's documentation.
    """

    heartbeat_interval: int


class HelloPayload(
    GatewayEventPayload[typing.Literal[GatewayReceiveOpcode.HELLO], HelloPayloadData]
):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#hello)
    for Discord's documentation.
    """

    pass
