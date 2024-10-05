# mypy: disable-error-code="misc"
# This is needed because Mypy complains when overriding fields in a TypedDict.

from __future__ import annotations

import enum
import typing

from ..common import Snowflake

__all__ = (
    "PartialUser",
    "User",
    "UserPremiumType",
    "UserFlags",
    "AvatarDecoration",
)


class PartialUser(typing.TypedDict):
    """
    Represents a partial user object in Discord.

    A partial user is guaranteed to contain only an ID. While not explicitly
    documented in the official docs, this assumption is recommended by users in
    the Discord Developers server.

    Other fields may be present but should not be relied upon in a partial user object.
    """

    id: Snowflake
    username: typing.NotRequired[str]
    discriminator: typing.NotRequired[str]
    avatar: typing.NotRequired[str | None]
    bot: typing.NotRequired[bool]
    system: typing.NotRequired[bool]
    mfa_enabled: typing.NotRequired[bool]
    banner: typing.NotRequired[str | None]
    accent_color: typing.NotRequired[int | None]
    locale: typing.NotRequired[str]
    verified: typing.NotRequired[bool]
    email: typing.NotRequired[str | None]
    flags: typing.NotRequired[int]
    premium_type: typing.NotRequired[UserPremiumType]
    public_flags: typing.NotRequired[int]
    avatar_decoration_data: typing.NotRequired[AvatarDecoration | None]


class User(PartialUser):
    """
    See [here](https://discord.com/developers/docs/resources/user)
    for Discord's documentation.
    """

    id: Snowflake
    username: str
    discriminator: str
    avatar: str | None


class UserPremiumType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/user#user-object-premium-types)
    for Discord's documentation.
    """

    NONE = 0
    NITRO_CLASSIC = 1
    NITRO = 2
    NITRO_BASIC = 3


class UserFlags(enum.IntFlag):
    """
    See [here](https://discord.com/developers/docs/resources/user#user-object-user-flags)
    for Discord's documentation.
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


class AvatarDecoration(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/user#avatar-decoration-data-object)
    for Discord's documentation.
    """

    asset: str
    sku_id: Snowflake
