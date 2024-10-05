import typing

from ..common import Snowflake
from .user import User

__all__ = ("Emoji",)


class Emoji(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/emoji)
    for Discord's documentation.
    """

    id: Snowflake | None
    name: str | None
    roles: typing.NotRequired[typing.List[Snowflake]]
    user: typing.NotRequired[User]
    """Partial user object."""
    require_colons: typing.NotRequired[bool]
    managed: typing.NotRequired[bool]
    animated: typing.NotRequired[bool]
    available: typing.NotRequired[bool]
