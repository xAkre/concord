import typing

from ..common import Iso8601Timestamp, Snowflake
from .guild import PartialGuild
from .user import User

__all__ = ("GuildTemplate",)


class GuildTemplate(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/guild-template)
    for Discord's documentation.
    """

    code: str
    name: str
    description: str | None
    creator_id: Snowflake
    creator: User
    created_at: Iso8601Timestamp
    updated_at: Iso8601Timestamp
    source_guild_id: Snowflake
    serialized_source_guild: PartialGuild
    is_dirty: bool | None
