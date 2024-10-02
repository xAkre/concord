import enum


class GatewayOpcode(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#gateway-events)
    for Discord's documentation
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
    HEARTBEAT_ACKNOWLEDGMENT = 11
    REQUEST_SOUNDBOARD_SOUNDS = 31


class GatewayReceiveOpcode(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#receive-events)
    for Discord's documentation
    """

    DISPATCH = 0
    HEARTBEAT = 1
    RECONNECT = 7
    INVALID_SESSION = 9
    HELLO = 10
    HEARTBEAT_ACKNOWLEDGMENT = 11


class GatewaySendOpcode(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#send-events)
    for Discord's documentation
    """

    HEARTBEAT = 1
    IDENTIFY = 2
    PRESENCE_UPDATE = 3
    VOICE_STATE_UPDATE = 4
    RESUME = 6
    REQUEST_GUILD_MEMBERS = 8
    REQUEST_SOUNDBOARD_SOUNDS = 31


class DiscordAPIVersion(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/reference#api-reference-api-versions)
    for Discord's documentation
    """

    _10 = 10
    LATEST = 10
    _9 = 9
    _8 = 8
    """Not supported"""
    _7 = 7
    """Not supported"""
    _6 = 6
    """Not supported"""
    DISCORD_DEFAULT = 6
    """Not supported"""


class ActiveStatusType(enum.StrEnum):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#update-presence-status-types)
    for Discord's documentation
    """

    ONLINE = "online"
    DND = "dnd"
    AFK = "idle"
    INVISIBLE = "invisible"
    OFFLINE = "offline"


class GatewayIntents(enum.IntFlag):
    """
    See [here](https://discord.com/developers/docs/topics/gateway#gateway-intents)
    for Discord's documentation
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


__all__ = [
    "GatewayOpcode",
    "GatewayReceiveOpcode",
    "GatewaySendOpcode",
    "DiscordAPIVersion",
    "ActiveStatusType",
]
