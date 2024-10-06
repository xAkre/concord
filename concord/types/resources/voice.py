import typing

from ..common import Snowflake
from .guild import GuildMember

__all__ = (
    "VoiceState",
    "VoiceRegion",
)


class VoiceState(typing.TypedDict):
    guild_id: typing.NotRequired[Snowflake]
    channel_id: Snowflake | None
    user_id: Snowflake
    member: typing.NotRequired[GuildMember]
    session_id: str
    deaf: bool
    mute: bool
    self_deaf: bool
    self_mute: bool
    self_stream: typing.NotRequired[bool | None]
    self_video: bool
    suppress: bool
    request_to_speak_timestamp: str | None


class VoiceRegion(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/voice#voice-region-object)
    for Discord's documentation.
    """

    id: str
    name: str
    optimal: bool
    deprecated: bool
    custom: bool
