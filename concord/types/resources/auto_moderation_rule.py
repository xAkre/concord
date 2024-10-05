from __future__ import annotations

import collections.abc
import enum
import typing

from ..common import Snowflake

__all__ = ("AutoModerationRule",)


class AutoModerationRule(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-rule-object)
    for Discord's documentation.
    """

    id: Snowflake
    guild_id: Snowflake
    name: str
    creator_id: Snowflake
    event_type: AutoModerationRuleEventType
    trigger_type: AutoModerationRuleTriggerType
    trigger_metadata: typing.NotRequired[AutoModerationRuleTriggerMetadata]
    actions: collections.abc.Sequence[AutoModerationAction]
    enabled: bool
    exempt_roles: collections.abc.Sequence[Snowflake]
    exempt_channels: collections.abc.Sequence[Snowflake]


class AutoModerationRuleEventType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-rule-object-event-types)
    for Discord's documentation.
    """

    MESSAGE_SEND = 1
    MESSAGE_UPDATE = 2


class AutoModerationRuleTriggerType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-rule-object-trigger-types)
    for Discord's documentation.
    """

    KEYWORD = 1
    SPAM = 3
    KEYWORD_PRESET = 4
    MENTION_SPAM = 5
    MEMBER_PROFILE = 6


class AutoModerationRuleTriggerMetadata(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-rule-object-trigger-metadata)
    for Discord's documentation.
    """

    keyword_filter: collections.abc.Sequence[str]
    regex_patterns: collections.abc.Sequence[str]
    presets: collections.abc.Sequence[AutoModerationRuleKeywordPresetType]
    allow_list: collections.abc.Sequence[str]
    mention_total_limit: int
    mention_raid_protection_enabled: bool


class AutoModerationRuleKeywordPresetType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-rule-object-keyword-preset-types)
    for Discord's documentation.
    """

    PROFANITY = 1
    SEXUALLY_EXPLICIT = 2
    SLURS = 3


class AutoModerationAction(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-action-object)
    for Discord's documentation.
    """

    type: AutoModerationActionType
    metadata: typing.NotRequired[AutoModerationActionMetadata]


class AutoModerationActionType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-action-object-action-types)
    for Discord's documentation.
    """

    BLOCK_MESSAGE = 1
    SEND_ALERT_MESSAGE = 2
    TIMEOUT = 3
    BLOCK_MEMBER_INTERACTION = 4


class AutoModerationActionMetadata(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/auto-moderation#auto-moderation-action-object-action-types)
    for Discord's documentation.
    """

    channel_id: typing.NotRequired[Snowflake]
    duration_seconds: typing.NotRequired[int]
    custom_message: typing.NotRequired[str]
