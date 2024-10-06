from __future__ import annotations

import typing

from ..common import Snowflake
from .user import User

__all__ = ("SoundboardSound",)


class SoundboardSound(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/soundboard#soundboard-sound-object) for
    Discord's documentation.
    """

    name: str
    sound_id: Snowflake
    volume: float
    emoji_id: Snowflake | None
    emoji_name: str | None
    guild_id: typing.NotRequired[Snowflake]
    available: bool
    user: typing.NotRequired[User]
