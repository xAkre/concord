from __future__ import annotations

import collections.abc
import enum
import typing

from concord.types.common import Snowflake
from concord.types.resources.emoji import Emoji

__all__ = (
    "GatewayOpcode",
    "GatewayIntents",
)


class GatewayOpcode(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/topics/opcodes-and-status-codes#gateway)
    for Discord's documentation.
    """

    DISPATCH = 0
    HEARTBEAT = 1
    IDENTIFY = 2
    PRESENCE_UPDATE = 3
    VOICE_STATE_UPDATE = 4
    RESUME = 6
    RECONNECT = 7
    REQUEST_GUILD_MEMBERS = 8
    INVALID_SESSION = 9
    HELLO = 10
    HEARTBEAT_ACK = 11
    REQUEST_SOUNDBOARD_SOUNDS = 31


class GatewayIntents(enum.IntFlag):
    """
    See [here](https://discord.com/developers/docs/topics/gateway#gateway-intents)
    for Discord's documentation.
    """

    GUILDS = 1 << 0
    GUILD_MEMBERS = 1 << 1
    GUILD_MODERATION = 1 << 2
    GUILD_EXPRESSIONS = 1 << 3
    GUILD_INTEGRATIONS = 1 << 4
    GUILD_WEBHOOKS = 1 << 5
    GUILD_INVITES = 1 << 6
    GUILD_VOICE_STATES = 1 << 7
    GUILD_PRESENCES = 1 << 8
    GUILD_MESSAGES = 1 << 9
    GUILD_MESSAGE_REACTIONS = 1 << 10
    GUILD_MESSAGE_TYPING = 1 << 11
    DIRECT_MESSAGES = 1 << 12
    DIRECT_MESSAGE_REACTIONS = 1 << 13
    DIRECT_MESSAGE_TYPING = 1 << 14
    MESSAGE_CONTENT = 1 << 15
    GUILD_SCHEDULED_EVENTS = 1 << 16
    AUTO_MODERATION_CONFIGURATION = 1 << 20
    AUTO_MODERATION_EXECUTION = 1 << 21
    GUILD_MESSAGE_POLLS = 1 << 24
    DIRECT_MESSAGE_POLLS = 1 << 25


class GatewayPresenceUpdate(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#update-presence-gateway-presence-update-structure)
    for Discord's documentation.
    """

    since: int
    activities: typing.List[GatewayActivity]
    status: GatewayPresenceStatus
    afk: bool


class GatewayActivity(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#activity-object-activity-structure)
    for Discord's documentation.
    """

    name: str
    type: GatewayActivityType
    url: typing.NotRequired[str | None]
    created_at: int
    timestamps: typing.NotRequired[GatewayActivityTimestamps]
    application_id: typing.NotRequired[Snowflake]
    details: typing.NotRequired[str]
    state: typing.NotRequired[str]
    emoji: typing.NotRequired[Emoji]
    party: typing.NotRequired[GatewayActivityParty]
    assets: typing.NotRequired[GatewayActivityAssets]
    secrets: typing.NotRequired[GatewayActivitySecrets]
    instance: typing.NotRequired[bool]
    flags: typing.NotRequired[int]
    buttons: typing.NotRequired[collections.abc.Sequence[GatewayActivityButton]]


class GatewayActivityType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#activity-object-activity-types)
    for Discord's documentation.
    """

    PLAYING = 0
    STREAMING = 1
    LISTENING = 2
    WATCHING = 3
    CUSTOM = 4
    COMPETING = 5


class GatewayActivityTimestamps(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#activity-object-activity-timestamps)
    for Discord's documentation.
    """

    start: typing.NotRequired[int]
    end: typing.NotRequired[int]


class GatewayActivityParty(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#activity-object-activity-party)
    for Discord's documentation.
    """

    id: typing.NotRequired[str]
    size: typing.NotRequired[typing.Tuple[int, int]]


class GatewayActivityAssets(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#activity-object-activity-assets)
    for Discord's documentation.
    """

    large_image: typing.NotRequired[str]
    large_text: typing.NotRequired[str]
    small_image: typing.NotRequired[str]
    small_text: typing.NotRequired[str]


class GatewayActivitySecrets(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#activity-object-activity-secrets)
    for Discord's documentation.
    """

    join: typing.NotRequired[str]
    spectate: typing.NotRequired[str]
    match: typing.NotRequired[str]


class GatewayActivityFlags(enum.IntFlag):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#activity-object-activity-flags)
    for Discord's documentation.
    """

    INSTANCE = 1 << 0
    JOIN = 1 << 1
    SPECTATE = 1 << 2
    JOIN_REQUEST = 1 << 3
    SYNC = 1 << 4
    PLAY = 1 << 5
    PARTY_PRIVACY_FRIENDS = 1 << 6
    PARTY_PRIVACY_VOICE_CHANNEL = 1 << 7
    EMBEDDED = 1 << 8


class GatewayActivityButton(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#activity-object-activity-buttons)
    for Discord's documentation.
    """

    label: str
    url: str


class GatewayPresenceStatus(enum.StrEnum):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#update-presence-status-types)
    for Discord's documentation.
    """

    ONLINE = "online"
    IDLE = "idle"
    DO_NOT_DISTURB = "dnd"
    INVISIBLE = "invisible"
    OFFLINE = "offline"
