from __future__ import annotations

import enum
import typing

from ..common import Snowflake

__all__ = ("StageInstance", "StageInstancePrivacyLevel")


class StageInstance(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/stage-instance#stage-instance-object) for
    Discord's documentation.
    """

    id: Snowflake
    guild_id: Snowflake
    channel_id: Snowflake
    topic: str
    privacy_level: StageInstancePrivacyLevel
    discoverable_disabled: bool
    guild_scheduled_event_id: Snowflake | None


class StageInstancePrivacyLevel(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/stage-instance#stage-instance-object-privacy-level) for
    Discord's documentation.
    """

    GUILD_ONLY = 2
