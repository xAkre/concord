# mypy: disable-error-code="misc"
# This is needed because Mypy complains when overriding fields in a TypedDict.

import collections.abc
import enum
import typing

from concord.types.resources.application import PartialApplication
from concord.types.resources.guild import UnavailableGuild
from concord.types.resources.user import User

__all__ = (
    "GatewayReceiveOpcode",
    "GatewayCloseEventCode",
    "GatewayReconnectableCloseEventCode",
    "GatewayEventPayload",
    "GatewayHelloEventPayloadData",
    "GatewayHelloEventPayload",
    "GatewayHeartbeatEventPayload",
    "GatewayHeartbeatAcknowledgeEventPayload",
    "GatewayReconnectEventPayload",
    "GatewayDispatchEventPayload",
    "GatewayReadyEventPayloadData",
    "GatewayReadyEventPayload",
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


class GatewayCloseEventCode(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/topics/opcodes-and-status-codes#gateway-gateway-close-event-codes)
    for Discord's documentation.
    """

    UNKNOWN_ERROR = 4000
    UNKNOWN_OPCODE = 4001
    DECODE_ERROR = 4002
    NOT_AUTHENTICATED = 4003
    AUTHENTICATION_FAILED = 4004
    ALREADY_AUTHENTICATED = 4005
    INVALID_SEQ = 4007
    RATE_LIMITED = 4008
    SESSION_TIMEOUT = 4009
    INVALID_SHARD = 4010
    SHARDING_REQUIRED = 4011
    INVALID_API_VERSION = 4012
    INVALID_INTENT = 4013
    DISALLOWED_INTENT = 4014


class GatewayReconnectableCloseEventCode(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/topics/opcodes-and-status-codes#gateway-gateway-close-event-codes)
    for Discord's documentation.
    """

    UNKNOWN_ERROR = 4000
    UNKNOWN_OPCODE = 4001
    DECODE_ERROR = 4002
    NOT_AUTHENTICATED = 4003
    ALREADY_AUTHENTICATED = 4005
    INVALID_SEQ = 4007
    RATE_LIMITED = 4008
    SESSION_TIMEOUT = 4009


class GatewayEventPayload[Op: GatewayReceiveOpcode, Data](typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#payload-structure)
    for Discord's documentation.
    """

    op: Op
    d: Data
    s: int | None
    t: str | None


class GatewayHelloEventPayloadData(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#hello)
    for Discord's documentation.
    """

    heartbeat_interval: int


GatewayHelloEventPayload = GatewayEventPayload[
    typing.Literal[GatewayReceiveOpcode.HELLO], GatewayHelloEventPayloadData
]
"""
See [here](https://discord.com/developers/docs/topics/gateway-events#hello)
for Discord's documentation.
"""

GatewayHeartbeatEventPayload = GatewayEventPayload[
    typing.Literal[GatewayReceiveOpcode.HEARTBEAT], typing.Literal[None]
]
"""
See [here](https://discord.com/developers/docs/topics/gateway#connection-lifecycle)
for Discord's documentation.
"""

GatewayHeartbeatAcknowledgeEventPayload = GatewayEventPayload[
    typing.Literal[GatewayReceiveOpcode.HEARTBEAT_ACK], typing.Literal[None]
]
"""
See [here](https://discord.com/developers/docs/topics/gateway#connection-lifecycle)
for Discord's documentation.
"""

GatewayReconnectEventPayload = GatewayEventPayload[
    typing.Literal[GatewayReceiveOpcode.RECONNECT], typing.Literal[None]
]
"""
See [here](https://discord.com/developers/docs/topics/gateway-events#reconnect)
for Discord's documentation.
"""


class GatewayDispatchEventPayload[T](
    GatewayEventPayload[typing.Literal[GatewayReceiveOpcode.DISPATCH], T]
):
    """
    See [here](https://discord.com/developers/docs/topics/gateway#dispatch-events)
    for Discord's documentation.
    """

    s: int
    t: str


class GatewayReadyEventPayloadData(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/gateway#ready)
    for Discord's documentation.
    """

    v: int
    user: typing.Dict[str, User]
    guilds: collections.abc.Sequence[UnavailableGuild]
    session_id: str
    resume_gateway_url: str
    shard: typing.NotRequired[typing.Tuple[int, int]]
    application: PartialApplication
    """Contains ID and flags."""


GatewayReadyEventPayload = GatewayDispatchEventPayload[GatewayReadyEventPayloadData]
"""
See [here](https://discord.com/developers/docs/topics/gateway#ready)
for Discord's documentation.
"""
