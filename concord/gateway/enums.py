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


class UserFlags(enum.IntFlag):
    """
    See [here](https://discord.com/developers/docs/resources/user#user-object-user-flags)
    for Discord's documentation
    """

    STAFF = 1 << 0
    PARTNER = 1 << 1
    HYPESQUAD = 1 << 2
    BUG_HUNTER_LEVEL_1 = 1 << 3
    HYPESQUAD_ONLINE_HOUSE_1 = 1 << 6
    HYPESQUAD_ONLINE_HOUSE_2 = 1 << 7
    HYPESQUAD_ONLINE_HOUSE_3 = 1 << 8
    PERMIUM_EARLY_SUPPORTER = 1 << 9
    TEAM_PSEUDO_USER = 1 << 10
    BUG_HUNTER_LEVEL_2 = 1 << 14
    VERIFIED_BOT = 1 << 16
    VERIFIED_BOT_DEVELOPER = 1 << 17
    CERTIFIED_MODERATOR = 1 << 18
    BOT_HTTP_INTERACTIONS = 1 << 19
    ACTIVE_DEVELOPER = 1 << 22


class ApplicationFlags(enum.IntFlag):
    """
    See [here](https://discord.com/developers/docs/resources/application#application-object-application-flags)
    for Discord's documentation
    """

    APPLICATION_AUTO_MODERATION_RULE_CREATE_BADGE = 1 << 6
    GATEWAY_PRESENCE = 1 << 12
    GATEWAY_PRESENCE_LIMITED = 1 << 13
    GATEWAY_GUILD_MEMBERS = 1 << 14
    GATEWAY_GUILD_MEMBERS_LIMITED = 1 << 15
    VERIFICATION_PENDING_GUILD_LIMIT = 1 << 16
    EMBEDDED = 1 << 17
    GATEWAY_MESSAGE_CONTENT = 1 << 18
    GATEWAY_MESSAGE_CONTENT_LIMITED = 1 << 19
    APPLICATION_COMMAND_BADGE = 1 << 23


class GatewayDispatchEvent(enum.StrEnum):
    """
    See [here](https://discord.com/developers/docs/topics/gateway-events#receive-events)
    for Discord's documentation.
    """

    READY = "READY"
    APPLICATION_COMMAND_PERMISSIONS_UPDATE = "APPLICATION_COMMAND_PERMISSIONS_UPDATE"
    AUTO_MODERATION_RULE_CREATE = "AUTO_MODERATION_RULE_CREATE"
    AUTO_MODERATION_RULE_UPDATE = "AUTO_MODERATION_RULE_UPDATE"
    AUTO_MODERATION_RULE_DELETE = "AUTO_MODERATION_RULE_DELETE"
    AUTO_MODERATION_ACTION_EXECUTION = "AUTO_MODERATION_ACTION_EXECUTION"
    CHANNEL_CREATE = "CHANNEL_CREATE"
    CHANNEL_UPDATE = "CHANNEL_UPDATE"
    CHANNEL_DELETE = "CHANNEL_DELETE"
    CHANNEL_PINS_UPDATE = "CHANNEL_PINS_UPDATE"
    THREAD_CREATE = "THREAD_CREATE"
    THREAD_UPDATE = "THREAD_UPDATE"
    THREAD_DELETE = "THREAD_DELETE"
    THREAD_LIST_SYNC = "THREAD_LIST_SYNC"
    THREAD_MEMBER_UPDATE = "THREAD_MEMBER_UPDATE"
    THREAD_MEMBERS_UPDATE = "THREAD_MEMBERS_UPDATE"
    ENTITLEMENT_CREATE = "ENTITLEMENT_CREATE"
    ENTITLEMENT_UPDATE = "ENTITLEMENT_UPDATE"
    ENTITLEMENT_DELETE = "ENTITLEMENT_DELETE"
    GUILD_CREATE = "GUILD_CREATE"
    GUILD_UPDATE = "GUILD_UPDATE"
    GUILD_DELETE = "GUILD_DELETE"
    GUILD_AUDIT_LOG_ENTRY_CREATE = "GUILD_AUDIT_LOG_ENTRY_CREATE"
    GUILD_BAN_ADD = "GUILD_BAN_ADD"
    GUILD_BAN_REMOVE = "GUILD_BAN_REMOVE"
    GUILD_EMOJIS_UPDATE = "GUILD_EMOJIS_UPDATE"
    GUILD_STICKERS_UPDATE = "GUILD_STICKERS_UPDATE"
    GUILD_INTEGRATIONS_UPDATE = "GUILD_INTEGRATIONS_UPDATE"
    GUILD_MEMBER_ADD = "GUILD_MEMBER_ADD"
    GUILD_MEMBER_REMOVE = "GUILD_MEMBER_REMOVE"
    GUILD_MEMBER_UPDATE = "GUILD_MEMBER_UPDATE"
    GUILD_MEMBERS_CHUNK = "GUILD_MEMBERS_CHUNK"
    GUILD_ROLE_CREATE = "GUILD_ROLE_CREATE"
    GUILD_ROLE_UPDATE = "GUILD_ROLE_UPDATE"
    GUILD_ROLE_DELETE = "GUILD_ROLE_DELETE"
    GUILD_SCHEDULED_EVENT_CREATE = "GUILD_SCHEDULED_EVENT_CREATE"
    GUILD_SCHEDULED_EVENT_UPDATE = "GUILD_SCHEDULED_EVENT_UPDATE"
    GUILD_SCHEDULED_EVENT_DELETE = "GUILD_SCHEDULED_EVENT_DELETE"
    GUILD_SCHEDULED_EVENT_USER_ADD = "GUILD_SCHEDULED_EVENT_USER_ADD"
    GUILD_SCHEDULED_EVENT_USER_REMOVE = "GUILD_SCHEDULED_EVENT_USER_REMOVE"
    GUILD_SOUNDBOARD_SOUND_CREATE = "GUILD_SOUNDBOARD_SOUND_CREATE"
    GUILD_SOUNDBOARD_SOUND_UPDATE = "GUILD_SOUNDBOARD_SOUND_UPDATE"
    GUILD_SOUNDBOARD_SOUND_DELETE = "GUILD_SOUNDBOARD_SOUND_DELETE"
    GUILD_SOUNDBOARD_SOUNDS_UPDATE = "GUILD_SOUNDBOARD_SOUNDS_UPDATE"
    SOUNDBOARD_SOUNDS = "SOUNDBOARD_SOUNDS"
    INTEGRATION_CREATE = "INTEGRATION_CREATE"
    INTEGRATION_UPDATE = "INTEGRATION_UPDATE"
    INTEGRATION_DELETE = "INTEGRATION_DELETE"
    INTERACTION_CREATE = "INTERACTION_CREATE"
    INVITE_CREATE = "INVITE_CREATE"
    INVITE_DELETE = "INVITE_DELETE"
    MESSAGE_CREATE = "MESSAGE_CREATE"
    MESSAGE_UPDATE = "MESSAGE_UPDATE"
    MESSAGE_DELETE = "MESSAGE_DELETE"
    MESSAGE_DELETE_BULK = "MESSAGE_DELETE_BULK"
    MESSAGE_REACTION_ADD = "MESSAGE_REACTION_ADD"
    MESSAGE_REACTION_REMOVE = "MESSAGE_REACTION_REMOVE"
    MESSAGE_REACTION_REMOVE_ALL = "MESSAGE_REACTION_REMOVE_ALL"
    MESSAGE_REACTION_REMOVE_EMOJI = "MESSAGE_REACTION_REMOVE_EMOJI"
    PRESENCE_UPDATE = "PRESENCE_UPDATE"
    STAGE_INSTANCE_CREATE = "STAGE_INSTANCE_CREATE"
    STAGE_INSTANCE_UPDATE = "STAGE_INSTANCE_UPDATE"
    STAGE_INSTANCE_DELETE = "STAGE_INSTANCE_DELETE"
    SUBSCRIPTION_CREATE = "SUBSCRIPTION_CREATE"
    SUBSCRIPTION_UPDATE = "SUBSCRIPTION_UPDATE"
    SUBSCRIPTION_DELETE = "SUBSCRIPTION_DELETE"
    TYPING_START = "TYPING_START"
    USER_UPDATE = "USER_UPDATE"
    VOICE_CHANNEL_EFFECT_SEND = "VOICE_CHANNEL_EFFECT_SEND"
    VOICE_STATE_UPDATE = "VOICE_STATE_UPDATE"
    VOICE_SERVER_UPDATE = "VOICE_SERVER_UPDATE"
    WEBHOOKS_UPDATE = "WEBHOOKS_UPDATE"
    MESSAGE_POLL_VOTE_ADD = "MESSAGE_POLL_VOTE_ADD"
    MESSAGE_POLL_VOTE_REMOVE = "MESSAGE_POLL_VOTE_REMOVE"


class GatewayDispatchEventCallbackName(enum.StrEnum):
    """Callback methods that are called when a dispatch event is received."""

    READY = "on_ready"
    APPLICATION_COMMAND_PERMISSIONS_UPDATE = "on_application_command_permissions_update"
    AUTO_MODERATION_RULE_CREATE = "on_auto_moderation_rule_create"
    AUTO_MODERATION_RULE_UPDATE = "on_auto_moderation_rule_update"
    AUTO_MODERATION_RULE_DELETE = "on_auto_moderation_rule_delete"
    AUTO_MODERATION_ACTION_EXECUTION = "on_auto_moderation_action_execution"
    CHANNEL_CREATE = "on_channel_create"
    CHANNEL_UPDATE = "on_channel_update"
    CHANNEL_DELETE = "on_channel_delete"
    CHANNEL_PINS_UPDATE = "on_channel_pins_update"
    THREAD_CREATE = "on_thread_create"
    THREAD_UPDATE = "on_thread_update"
    THREAD_DELETE = "on_thread_delete"
    THREAD_LIST_SYNC = "on_thread_list_sync"
    THREAD_MEMBER_UPDATE = "on_thread_member_update"
    THREAD_MEMBERS_UPDATE = "on_thread_members_update"
    ENTITLEMENT_CREATE = "on_entitlement_create"
    ENTITLEMENT_UPDATE = "on_entitlement_update"
    ENTITLEMENT_DELETE = "on_entitlement_delete"
    GUILD_CREATE = "on_guild_create"
    GUILD_UPDATE = "on_guild_update"
    GUILD_DELETE = "on_guild_delete"
    GUILD_AUDIT_LOG_ENTRY_CREATE = "on_guild_audit_log_entry_create"
    GUILD_BAN_ADD = "on_guild_ban_add"
    GUILD_BAN_REMOVE = "on_guild_ban_remove"
    GUILD_EMOJIS_UPDATE = "on_guild_emojis_update"
    GUILD_STICKERS_UPDATE = "on_guild_stickers_update"
    GUILD_INTEGRATIONS_UPDATE = "on_guild_integrations_update"
    GUILD_MEMBER_ADD = "on_guild_member_add"
    GUILD_MEMBER_REMOVE = "on_guild_member_remove"
    GUILD_MEMBER_UPDATE = "on_guild_member_update"
    GUILD_MEMBERS_CHUNK = "on_guild_members_chunk"
    GUILD_ROLE_CREATE = "on_guild_role_create"
    GUILD_ROLE_UPDATE = "on_guild_role_update"
    GUILD_ROLE_DELETE = "on_guild_role_delete"
    GUILD_SCHEDULED_EVENT_CREATE = "on_guild_scheduled_event_create"
    GUILD_SCHEDULED_EVENT_UPDATE = "on_guild_scheduled_event_update"
    GUILD_SCHEDULED_EVENT_DELETE = "on_guild_scheduled_event_delete"
    GUILD_SCHEDULED_EVENT_USER_ADD = "on_guild_scheduled_event_user_add"
    GUILD_SCHEDULED_EVENT_USER_REMOVE = "on_guild_scheduled_event_user_remove"
    GUILD_SOUNDBOARD_SOUND_CREATE = "on_guild_soundboard_sound_create"
    GUILD_SOUNDBOARD_SOUND_UPDATE = "on_guild_soundboard_sound_update"
    GUILD_SOUNDBOARD_SOUND_DELETE = "on_guild_soundboard_sound_delete"
    GUILD_SOUNDBOARD_SOUNDS_UPDATE = "on_guild_soundboard_sounds_update"
    SOUNDBOARD_SOUNDS = "on_soundboard_sounds"
    INTEGRATION_CREATE = "on_integration_create"
    INTEGRATION_UPDATE = "on_integration_update"
    INTEGRATION_DELETE = "on_integration_delete"
    INTERACTION_CREATE = "on_interaction_create"
    INVITE_CREATE = "on_invite_create"
    INVITE_DELETE = "on_invite_delete"
    MESSAGE_CREATE = "on_message_create"
    MESSAGE_UPDATE = "on_message_update"
    MESSAGE_DELETE = "on_message_delete"
    MESSAGE_DELETE_BULK = "on_message_delete_bulk"
    MESSAGE_REACTION_ADD = "on_message_reaction_add"
    MESSAGE_REACTION_REMOVE = "on_message_reaction_remove"
    MESSAGE_REACTION_REMOVE_ALL = "on_message_reaction_remove_all"
    MESSAGE_REACTION_REMOVE_EMOJI = "on_message_reaction_remove_emoji"
    PRESENCE_UPDATE = "on_presence_update"
    STAGE_INSTANCE_CREATE = "on_stage_instance_create"
    STAGE_INSTANCE_UPDATE = "on_stage_instance_update"
    STAGE_INSTANCE_DELETE = "on_stage_instance_delete"
    SUBSCRIPTION_CREATE = "on_subscription_create"
    SUBSCRIPTION_UPDATE = "on_subscription_update"
    SUBSCRIPTION_DELETE = "on_subscription_delete"
    TYPING_START = "on_typing_start"
    USER_UPDATE = "on_user_update"
    VOICE_CHANNEL_EFFECT_SEND = "on_voice_channel_effect_send"
    VOICE_STATE_UPDATE = "on_voice_state_update"
    VOICE_SERVER_UPDATE = "on_voice_server_update"
    WEBHOOKS_UPDATE = "on_webhooks_update"
    MESSAGE_POLL_VOTE_ADD = "on_message_poll_vote_add"
    MESSAGE_POLL_VOTE_REMOVE = "on_message_poll_vote_remove"


__all__ = [
    "GatewayOpcode",
    "GatewayReceiveOpcode",
    "GatewaySendOpcode",
    "DiscordAPIVersion",
    "ActiveStatusType",
    "UserFlags",
    "ApplicationFlags",
]
