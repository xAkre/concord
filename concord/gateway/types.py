# mypy: disable-error-code="misc"
# This is needed because mypy complains when child TypedDict classes override
# parent TypedDict classes.

import typing

from .enums import GatewayDispatchEvent, GatewayReceiveOpcode, GatewaySendOpcode
from .resources import PartialApplication, UnavailableGuild, User

# Input (Received) Event Payloads


class GatewayHeartbeatEventPayload:
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#heartbeat)
    for Discord's documentation
    """

    op: typing.Literal[GatewayReceiveOpcode.HEARTBEAT]
    d: None


class GatewayHeartbeatAcknowledgementEventPayload:
    """
    See [here](https://discord.com/developers/docs/topics/gateway#heartbeat-interval-example-heartbeat-ack)
    for Discord's documentation
    """

    op: typing.Literal[GatewayReceiveOpcode.HEARTBEAT_ACKNOWLEDGMENT]


class BaseGatewayEventPayload(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#payload-structure)
    for Discord's documentation
    """

    op: GatewayReceiveOpcode
    d: typing.Any


class GatewayHelloEventPayloadData(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#hello)
    for Discord's documentation
    """

    heartbeat_interval: int


class GatewayHelloEventPayload(BaseGatewayEventPayload):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#hello)
    for Discord's documentation
    """

    op: typing.Literal[GatewayReceiveOpcode.HELLO]
    d: GatewayHelloEventPayloadData


class GatewayDispatchEventPayload(BaseGatewayEventPayload):
    """
    See [here](https://discord.com/developers/docs/topics/opcodes-and-status-codes#gateway-gateway-opcodes)
    for Discord's documentation
    """

    op: typing.Literal[GatewayReceiveOpcode.DISPATCH]
    d: typing.Any
    s: int | None
    t: GatewayDispatchEvent


class GatewayReadyEventPayload(BaseGatewayEventPayload):
    v: int
    user: User
    guilds: typing.List[UnavailableGuild]
    session_id: str
    resume_gateway_url: str
    shard: typing.NotRequired[typing.Tuple[int, int]]
    application: PartialApplication


# Output (Sent) Message Types


class GatewayMessage(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#payload-structure)
    for Discord's documentation
    """

    op: GatewaySendOpcode
    d: typing.Any


class GatewayHeartbeatMessage(GatewayMessage):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#heartbeat)
    for Discord's documentation
    """

    op: typing.Literal[GatewaySendOpcode.HEARTBEAT]
    d: int | None


class GatewayIdentifyConnectionProperties(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#identify-identify-connection-properties)
    for Discord's documentation
    """

    os: str
    browser: str
    device: str


class GatewayIdentifyMessageData(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#identify-identify-structure)
    for Discord's documentation
    """

    token: str
    properties: GatewayIdentifyConnectionProperties
    compress: typing.NotRequired[bool]
    large_threshold: typing.NotRequired[int]
    shard: typing.NotRequired[typing.Tuple[int, int]]
    presence: typing.NotRequired[typing.Any]  # TODO: Define this
    intents: int


class GatewayIdentifyMessage(GatewayMessage):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#identify)
    for Discord's documentation
    """

    op: typing.Literal[GatewaySendOpcode.IDENTIFY]
    d: GatewayIdentifyMessageData


__all__ = [
    "BaseGatewayEventPayload",
    "GatewayEventPayload",
    "GatewayHelloEventPayloadData",
    "GatewayHelloEventPayload",
    "GatewayDispatchEventPayload",
    "GatewayMessage",
    "GatewayHeartbeatMessage",
    "GatewayIdentifyConnectionProperties",
    "GatewayIdentifyMessageData",
    "GatewayIdentifyMessage",
]
