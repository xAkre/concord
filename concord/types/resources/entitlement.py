from __future__ import annotations

import enum
import typing

from ..common import Iso8601Timestamp, Snowflake

__all__ = ("Entitlement", "EntitlementType")


class Entitlement(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/entitlement)
    for Discord's documentation.
    """

    id: Snowflake
    sku_id: Snowflake
    application_id: Snowflake
    user_id: typing.NotRequired[Snowflake]
    type: EntitlementType
    deleted: bool
    starts_at: typing.NotRequired[Iso8601Timestamp]
    ends_at: typing.NotRequired[Iso8601Timestamp]
    guild_id: typing.NotRequired[Snowflake]
    consumed: typing.NotRequired[bool]


class EntitlementType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/entitlement#entitlement-object-entitlement-types)
    for Discord's documentation.
    """

    PURCHASE = 1
    PREMIUM_SUBSCRIPTION = 2
    DEVELOPER_GIFT = 3
    TEST_MODE_PURCHASE = 4
    FREE_PURCHASE = 5
    USER_GIFT = 6
    PREMIUM_PURCHASE = 7
    APPLICATION_SUBSCRIPTION = 8
