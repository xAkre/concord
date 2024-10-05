from __future__ import annotations

import enum
import typing

from ..common import Snowflake
from .user import User

__all__ = (
    "Sticker",
    "StickerType",
    "StickerFormatType",
)


class Sticker(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/sticker)
    for Discord's documentation.
    """

    id: Snowflake
    pack_id: typing.NotRequired[Snowflake]
    name: str
    description: str | None
    tags: str
    type: StickerType
    format_type: StickerFormatType
    available: typing.NotRequired[bool]
    guild_id: typing.NotRequired[Snowflake]
    user: typing.NotRequired[User]
    sort_value: typing.NotRequired[int]


class StickerType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/sticker#sticker-object-sticker-types)
    for Discord's documentation.
    """

    STANDARD = 1
    GUILD = 2


class StickerFormatType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/sticker#sticker-object-sticker-format-types)
    for Discord's documentation.
    """

    PNG = 1
    APNG = 2
    LOTTIE = 3
    GIF = 4
