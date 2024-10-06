from __future__ import annotations

import collections.abc
import enum
import typing

from ..common import Iso8601Timestamp, Snowflake
from .user import User

__all__ = (
    "GuildScheduledEvent",
    "GuildScheduledEventPrivacyLevel",
    "GuildScheduledEventStatus",
    "GuildScheduledEventEntityType",
    "GuildScheduledEventEntityMetadata",
    "GuildScheduledEventRecurrenceRule",
    "GuildScheduledEventRecurrenceRuleFrequency",
    "GuildScheduledEventRecurrenceRuleWeekday",
    "GuildScheduledEventRecurrenceRuleNthWeekday",
    "GuildScheduledEventRecurrenceRuleMonth",
)


class GuildScheduledEvent(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-object)
    for Discord's documentation.
    """

    id: Snowflake
    guild_id: Snowflake
    channel_id: Snowflake | None
    creator_id: typing.NotRequired[Snowflake | None]
    name: str
    description: str | None
    scheduled_start_time: Iso8601Timestamp
    scheduled_end_time: Iso8601Timestamp | None
    privacy_level: GuildScheduledEventPrivacyLevel
    status: GuildScheduledEventStatus
    entity_type: GuildScheduledEventEntityType
    entity_id: Snowflake | None
    entity_metadata: GuildScheduledEventEntityMetadata | None
    creator: typing.NotRequired[User | None]
    user_count: typing.NotRequired[int]
    image: typing.NotRequired[str | None]
    recurrence_rule: GuildScheduledEventRecurrenceRule | None


class GuildScheduledEventPrivacyLevel(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-object-guild-scheduled-event-privacy-level)
    for Discord's documentation.
    """

    GUILD_ONLY = 2


class GuildScheduledEventStatus(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-object-guild-scheduled-event-status)
    for Discord's documentation.
    """

    SCHEDULED = 1
    ACTIVE = 2
    COMPLETED = 3
    CANCELED = 4


class GuildScheduledEventEntityType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-object-guild-scheduled-event-entity-types)
    for Discord's documentation.
    """

    STAGE_INSTANCE = 1
    VOICE = 2
    EXTERNAL = 3


class GuildScheduledEventEntityMetadata(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-object-guild-scheduled-event-entity-metadata)
    for Discord's documentation.
    """

    location: typing.NotRequired[str]


class GuildScheduledEventRecurrenceRule(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-recurrence-rule-object)
    for Discord's documentation.
    """

    start: Iso8601Timestamp
    end: Iso8601Timestamp | None
    frequency: GuildScheduledEventRecurrenceRuleFrequency
    interval: int
    by_weekday: (
        collections.abc.Sequence[GuildScheduledEventRecurrenceRuleWeekday] | None
    )
    by_n_weekday: (
        collections.abc.Sequence[GuildScheduledEventRecurrenceRuleNthWeekday] | None
    )
    by_month: collections.abc.Sequence[GuildScheduledEventRecurrenceRuleMonth] | None
    by_month_day: collections.abc.Sequence[int] | None
    by_year_day: collections.abc.Sequence[int] | None
    count: int | None


class GuildScheduledEventRecurrenceRuleFrequency(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-recurrence-rule-object-guild-scheduled-event-recurrence-rule-frequency)
    for Discord's documentation.
    """

    YEARLY = 0
    MONTHLY = 1
    WEEKLY = 2
    DAILY = 3


class GuildScheduledEventRecurrenceRuleWeekday(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-recurrence-rule-object-guild-scheduled-event-recurrence-rule-weekday)
    for Discord's documentation.
    """

    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


class GuildScheduledEventRecurrenceRuleNthWeekday(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-recurrence-rule-object-guild-scheduled-event-recurrence-rule-nweekday-structure)
    for Discord's documentation.
    """

    n: int
    weekday: GuildScheduledEventRecurrenceRuleWeekday


class GuildScheduledEventRecurrenceRuleMonth(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/guild-scheduled-event#guild-scheduled-event-recurrence-rule-object-guild-scheduled-event-recurrence-rule-month)
    for Discord's documentation.
    """

    JANUARY = 1
    FEBRUARY = 2
    MARCH = 3
    APRIL = 4
    MAY = 5
    JUNE = 6
    JULY = 7
    AUGUST = 8
    SEPTEMBER = 9
    OCTOBER = 10
    NOVEMBER = 11
    DECEMBER = 12
