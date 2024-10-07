# mypy: disable-error-code="misc"
# This is needed because Mypy complains when overriding fields in a TypedDict.

import collections.abc
import typing

from ..common import Snowflake
from .user import PartialUser

__all__ = (
    "PartialEmoji",
    "Emoji",
)


class PartialEmoji(typing.TypedDict):
    """
    Represents a partial emoji in Discord.

    A partial emoji is guaranteed to contain only an ID. While not explicitly
    documented in the official docs, this assumption is recommended by users in
    the Discord Developers server.

    Other fields may be present but should not be relied upon in a partial emoji object.
    """

    id: Snowflake | None
    name: typing.NotRequired[str | None]
    roles: typing.NotRequired[collections.abc.Sequence[Snowflake]]
    user: typing.NotRequired[PartialUser]
    require_colons: typing.NotRequired[bool]
    managed: typing.NotRequired[bool]
    animated: typing.NotRequired[bool]
    available: typing.NotRequired[bool]


class Emoji(PartialEmoji):
    """
    See [here](https://discord.com/developers/docs/resources/emoji)
    for Discord's documentation.
    """

    id: Snowflake | None
    name: str | None
