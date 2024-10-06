from __future__ import annotations

import collections.abc
import enum
import typing

from ..common import Iso8601Timestamp, Snowflake

__all__ = (
    "Subscription",
    "SubscriptionStatus",
)


class Subscription(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/subscription) for
    Discord's documentation.
    """

    id: Snowflake
    user_id: Snowflake
    sku_ids: collections.abc.Sequence[Snowflake]
    entitlement_ids: collections.abc.Sequence[Snowflake]
    current_period_start: Iso8601Timestamp
    current_period_end: Iso8601Timestamp
    status: SubscriptionStatus
    canceled_at: Iso8601Timestamp | None
    country: typing.NotRequired[str]


class SubscriptionStatus(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/subscription#subscription-statuses)
    for Discord's documentation.
    """

    ACTIVE = 1
    ENDING = 2
    INACTIVE = 3
