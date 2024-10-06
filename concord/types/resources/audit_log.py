from __future__ import annotations

import collections.abc
import enum
import typing

from ..common import Snowflake
from .application_command import ApplicationCommand
from .auto_moderation_rule import AutoModerationRule
from .channel import Channel, PermissionOverwriteType
from .guild import PartialGuildIntegration
from .guild_scheduled_event import GuildScheduledEvent
from .user import User
from .webhook import Webhook

__all__ = (
    "AuditLog",
    "AuditLogChange",
    "AuditLogEntry",
    "AuditLogEvent",
    "AuditLogEntryInfo",
)


class AuditLog(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/audit-log)
    for Discord's documentation.
    """

    application_commands: collections.abc.Sequence[ApplicationCommand]
    audit_log_entries: collections.abc.Sequence[AuditLogEntry]
    auto_moderation_rules: collections.abc.Sequence[AutoModerationRule]
    guild_scheduled_events: collections.abc.Sequence[GuildScheduledEvent]
    integrations: collections.abc.Sequence[PartialGuildIntegration]
    threads: collections.abc.Sequence[Channel]
    users: collections.abc.Sequence[User]
    webhooks: collections.abc.Sequence[Webhook]


class AuditLogEntry(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/audit-log#audit-log-entry-object)
    for Discord's documentation.
    """

    target_id: Snowflake
    changes: typing.NotRequired[collections.abc.Sequence[AuditLogChange]]
    user_id: Snowflake | None
    id: Snowflake
    action_type: AuditLogEvent
    options: typing.NotRequired[AuditLogEntryInfo]
    reason: typing.NotRequired[str]


class AuditLogChange(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/audit-log#audit-log-change-object-audit-log-change-structure)
    for Discord's documentation.
    """

    new_value: typing.NotRequired[typing.Any]
    old_value: typing.NotRequired[typing.Any]
    key: str
    # TODO: Add the other change types.


class AuditLogEvent(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/audit-log#audit-log-entry-object-audit-log-events)
    for Discord's documentation.
    """

    GUILD_UPDATE = 1
    CHANNEL_CREATE = 10
    CHANNEL_UPDATE = 11
    CHANNEL_DELETE = 12
    CHANNEL_OVERWRITE_CREATE = 13
    CHANNEL_OVERWRITE_UPDATE = 14
    CHANNEL_OVERWRITE_DELETE = 15
    MEMBER_KICK = 20
    MEMBER_PRUNE = 21
    MEMBER_BAN_ADD = 22
    MEMBER_BAN_REMOVE = 23
    MEMBER_UPDATE = 24
    MEMBER_ROLE_UPDATE = 25
    MEMBER_MOVE = 26
    MEMBER_DISCONNECT = 27
    BOT_ADD = 28
    ROLE_CREATE = 30
    ROLE_UPDATE = 31
    ROLE_DELETE = 32
    INVITE_CREATE = 40
    INVITE_UPDATE = 41
    INVITE_DELETE = 42
    WEBHOOK_CREATE = 50
    WEBHOOK_UPDATE = 51
    WEBHOOK_DELETE = 52
    EMOJI_CREATE = 60
    EMOJI_UPDATE = 61
    EMOJI_DELETE = 62
    MESSAGE_DELETE = 72
    MESSAGE_BULK_DELETE = 73
    MESSAGE_PIN = 74
    MESSAGE_UNPIN = 75
    INTEGRATION_CREATE = 80
    INTEGRATION_UPDATE = 81
    INTEGRATION_DELETE = 82
    STAGE_INSTANCE_CREATE = 83
    STAGE_INSTANCE_UPDATE = 84
    STAGE_INSTANCE_DELETE = 85
    STICKER_CREATE = 90
    STICKER_UPDATE = 91
    STICKER_DELETE = 92
    GUILD_SCHEDULED_EVENT_CREATE = 100
    GUILD_SCHEDULED_EVENT_UPDATE = 101
    GUILD_SCHEDULED_EVENT_DELETE = 102
    THREAD_CREATE = 110
    THREAD_UPDATE = 111
    THREAD_DELETE = 112
    APPLICATION_COMMAND_PERMISSION_UPDATE = 121
    SOUNDBOARD_SOUND_CREATE = 130
    SOUNDBOARD_SOUND_UPDATE = 131
    SOUNDBOARD_SOUND_DELETE = 132
    AUTO_MODERATION_RULE_CREATE = 140
    AUTO_MODERATION_RULE_UPDATE = 141
    AUTO_MODERATION_RULE_DELETE = 142
    AUTO_MODERATION_BLOCK_MESSAGE = 143
    AUTO_MODERATION_FLAG_TO_CHANNEL = 144
    AUTO_MODERATION_USER_COMMUNICATION_DISABLED = 145
    CREATOR_MONETIZATION_REQUEST_CREATED = 150
    CREATOR_MONETIZATION_TERMS_ACCEPTED = 151
    ONBOARDING_PROMPT_CREATE = 163
    ONBOARDING_PROMPT_UPDATE = 164
    ONBOARDING_PROMPT_DELETE = 165
    ONBOARDING_CREATE = 166
    ONBOARDING_UPDATE = 167
    HOME_SETTINGS_CREATE = 190
    HOME_SETTINGS_UPDATE = 191


class AuditLogEntryInfo(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/audit-log#audit-log-entry-object-optional-audit-entry-info)
    for Discord's documentation.
    """

    application_id: typing.NotRequired[Snowflake]
    auto_moderation_rule_name: typing.NotRequired[str]
    auto_moderation_rule_trigger_type: typing.NotRequired[int]
    channel_id: typing.NotRequired[Snowflake]
    count: typing.NotRequired[str]
    delete_member_days: typing.NotRequired[str]
    id: typing.NotRequired[Snowflake]
    members_removed: typing.NotRequired[str]
    message_id: typing.NotRequired[Snowflake]
    role_name: typing.NotRequired[str]
    type: typing.NotRequired[PermissionOverwriteType]
    integration_type: typing.NotRequired[str]
