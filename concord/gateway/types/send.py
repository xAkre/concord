from __future__ import annotations

import dataclasses
import enum
import json
import typing

from .common import GatewayPresenceUpdate

__all__ = (
    "GatewaySendOpcode",
    "GatewayMessage",
    "GatewayHeartbeatMessage",
    "GatewayResumeMessageData",
    "GatewayResumeMessage",
    "GatewayIdentifyMessageData",
    "GatewayIdentifyMessageConnectionProperties",
    "GatewayIdentifyMessage",
)


class GatewaySendOpcode(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/topics/opcodes-and-status-codes#gateway)
    for Discord's documentation.
    """

    HEARTBEAT = 1
    IDENTIFY = 2
    PRESENCE_UPDATE = 3
    VOICE_STATE_UPDATE = 4
    RESUME = 6
    REQUEST_GUILD_MEMBERS = 8
    REQUEST_SOUNDBOARD_SOUNDS = 31


@dataclasses.dataclass(kw_only=True)
class GatewayMessage[T]:
    """
    Represents a message to be sent to the gateway.

    See [here](https://discord.com/developers/docs/topics/gateway-events#send-events)
    for Discord's documentation.
    """

    opcode: GatewaySendOpcode
    data: T

    def serialize(self) -> str:
        """Serialize the message to a string that can be sent to the gateway."""
        return json.dumps(
            {
                "op": self.opcode,
                "d": self.data,
            }
        )


class GatewayHeartbeatMessage(GatewayMessage[int | None]):
    """
    Represents a heartbeat message to be sent to the gateway.

    See [here](https://discord.com/developers/docs/topics/gateway-events#heartbeat)
    for Discord's documentation.
    """

    opcode: typing.Literal[GatewaySendOpcode.HEARTBEAT] = GatewaySendOpcode.HEARTBEAT


class GatewayResumeMessageData(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#resume)
    for Discord's documentation.
    """

    token: str
    session_id: str
    seq: int


class GatewayResumeMessage(GatewayMessage[GatewayResumeMessageData]):
    """
    Represents a resume message to be sent to the gateway.

    See [here](https://discord.com/developers/docs/topics/gateway-events#resume-resume-structure)
    for Discord's documentation.
    """

    opcode: typing.Literal[GatewaySendOpcode.RESUME] = GatewaySendOpcode.RESUME


class GatewayIdentifyMessageData(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#identify)
    for Discord's documentation.
    """

    token: str
    properties: GatewayIdentifyMessageConnectionProperties
    compress: typing.NotRequired[bool]
    large_threshold: typing.NotRequired[int]
    shard: typing.NotRequired[typing.Tuple[int, int]]
    presence: typing.NotRequired[GatewayPresenceUpdate]
    intents: typing.NotRequired[int]


class GatewayIdentifyMessageConnectionProperties(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#identify-identify-connection-properties)
    for Discord's documentation.
    """

    os: str
    browser: str
    device: str


@dataclasses.dataclass(kw_only=True)
class GatewayIdentifyMessage(GatewayMessage[GatewayIdentifyMessageData]):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#identify-identify-structure)
    for Discord's documentation.
    """

    opcode: typing.Literal[GatewaySendOpcode.IDENTIFY] = GatewaySendOpcode.IDENTIFY
