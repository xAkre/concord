from __future__ import annotations

import enum
import typing

from ..common import Snowflake

__all__ = (
    "Role",
    "RoleTags",
    "RoleFlags",
)


class Role(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/permissions#role-object)
    for Discord's documentation.
    """

    id: Snowflake
    name: str
    color: int
    hoist: bool
    icon: typing.NotRequired[str | None]
    unicode_emoji: typing.NotRequired[str | None]
    position: int
    permissions: int
    managed: bool
    mentionable: bool
    tags: typing.NotRequired[RoleTags]
    flags: typing.NotRequired[int]


class RoleTags(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/permissions#role-object-role-tags-structure)
    for Discord's documentation.
    """

    bot_id: typing.NotRequired[Snowflake]
    integration_id: typing.NotRequired[Snowflake]
    premium_subscriber: typing.NotRequired[None]
    subscription_listing_id: typing.NotRequired[Snowflake]
    available_for_purchase: typing.NotRequired[None]
    guild_connections: typing.NotRequired[None]


class RoleFlags(enum.IntFlag):
    """
    See [here](https://discord.com/developers/docs/topics/permissions#role-object-role-flags)
    for Discord's documentation.
    """

    IN_PROMPT = 1 << 0
