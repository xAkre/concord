from __future__ import annotations

import enum
import typing

from ..common import Snowflake

__all__ = ("Sku", "SkuType", "SkuFlags")


class Sku(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/sku) for
    Discord's documentation.
    """

    id: Snowflake
    type: SkuType
    application_id: Snowflake
    name: str
    slug: str
    flags: int


class SkuType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/sku#sku-object-sku-types)
    for Discord's documentation.
    """

    DURABLE = 2
    CONSUMABLE = 3
    SUBSCRIPTION = 5
    SUBSCRIPTION_GROUP = 6


class SkuFlags(enum.IntFlag):
    """
    See [here](https://discord.com/developers/docs/resources/sku#sku-object-sku-flags)
    for Discord's documentation.
    """

    AVAILABLE = 1 << 2
    GUILD_SUBSCRIPTION = 1 << 7
    USER_SUBSCRIPTION = 1 << 8
