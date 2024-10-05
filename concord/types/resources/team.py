from __future__ import annotations

import enum
import typing

from ..common import Snowflake
from .user import User

__all__ = (
    "Team",
    "TeamMember",
    "TeamMembershipState",
    "TeamMemberRoleType",
)


class Team(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/teams#data-models-team-object)
    for Discord's documentation.
    """

    icon: str | None
    id: Snowflake
    members: typing.List[TeamMember]
    name: str
    owner_user_id: Snowflake


class TeamMember(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/topics/teams#data-models-team-member-object)
    for Discord's documentation.
    """

    membership_state: TeamMembershipState
    team_id: Snowflake
    user: User
    """Partial user object."""
    role: TeamMemberRoleType


class TeamMembershipState(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/topics/teams#data-models-membership-state-enum)
    for Discord's documentation.
    """

    INVITED = 1
    ACCEPTED = 2


class TeamMemberRoleType(enum.StrEnum):
    """
    See [here](https://discord.com/developers/docs/topics/teams#team-member-roles-team-member-role-types)
    for Discord's documentation.
    """

    ADMIN = "admin"
    DEVELOPER = "developer"
    READ_ONLY = "read_only"
