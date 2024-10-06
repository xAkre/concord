from __future__ import annotations

import enum
import typing

from ..common import Iso8601Timestamp
from .application import PartialApplication
from .channel import PartialChannel
from .guild import PartialGuild
from .guild_scheduled_event import GuildScheduledEvent
from .user import User

__all__ = ("Invite", "InviteType", "InviteTargetType")


class Invite(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/invite)
    for Discord's documentation.
    """

    type: InviteType
    code: str
    guild: typing.NotRequired[PartialGuild]
    channel: PartialChannel | None
    inviter: typing.NotRequired[User]
    target_type: typing.NotRequired[InviteTargetType]
    target_user: typing.NotRequired[User]
    target_application: typing.NotRequired[PartialApplication]
    approximate_presence_count: typing.NotRequired[int]
    approximate_member_count: typing.NotRequired[int]
    expires_at: typing.NotRequired[Iso8601Timestamp | None]
    guild_scheduled_event: typing.NotRequired[GuildScheduledEvent]


class InviteType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/invite#invite-object-invite-types)
    for Discord's documentation.
    """

    GUILD = 0
    GROUP_DM = 1
    FRIEND = 2


class InviteTargetType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/invite#invite-object-invite-target-types)
    for Discord's documentation.
    """

    STREAM = 1
    EMBEDDED_APPLICATION = 2
