# mypy: disable-error-code="misc"
# This is needed because Mypy complains when overriding fields in a TypedDict.

from __future__ import annotations

import collections.abc
import enum
import typing

from concord.types.resources.guild import GuildMember

from ..common import Iso8601Timestamp, Snowflake, UnparsedPermissionBitSet
from .guild import GuildMember
from .user import User

__all__ = (
    "PartialChannel",
    "Channel",
    "ChannelType",
    "Overwrite",
    "OverwriteType",
    "ThreadMetadata",
    "ThreadMember",
    "ChannelFlags",
    "ForumTag",
    "DefaultReaction",
    "ChannelSortOrderType",
    "ForumLayoutType",
)


class PartialChannel(typing.TypedDict):
    """
    Represents a partial channel object in Discord.

    A partial channel is guaranteed to contain only an ID. While not explicitly
    documented in the official docs, this assumption is recommended by users in
    the Discord Developers server.

    Other fields may be present but should not be relied upon in a partial channel object.
    """

    id: Snowflake
    type: typing.NotRequired[ChannelType]
    guild_id: typing.NotRequired[Snowflake]
    position: typing.NotRequired[int]
    permission_overwrites: typing.NotRequired[collections.abc.Sequence[Overwrite]]
    name: typing.NotRequired[str | None]
    topic: typing.NotRequired[str | None]
    nsfw: typing.NotRequired[bool]
    last_message_id: typing.NotRequired[Snowflake | None]
    bitrate: typing.NotRequired[int]
    user_limit: typing.NotRequired[int]
    recipients: typing.NotRequired[collections.abc.Sequence[User]]
    icon: typing.NotRequired[str | None]
    owner_id: typing.NotRequired[Snowflake]
    application_id: typing.NotRequired[Snowflake]
    managed: typing.NotRequired[bool]
    parent_id: typing.NotRequired[Snowflake | None]
    last_pin_timestamp: typing.NotRequired[Iso8601Timestamp | None]
    rtc_region: typing.NotRequired[str | None]
    video_quality_mode: typing.NotRequired[int]
    message_count: typing.NotRequired[int]
    member_count: typing.NotRequired[int]
    thread_metadata: typing.NotRequired[ThreadMetadata]
    member: typing.NotRequired[ThreadMember]
    default_auto_archive_duration: typing.NotRequired[int]
    permissions: typing.NotRequired[str]
    flags: typing.NotRequired[int]
    total_message_sent: typing.NotRequired[int]
    available_tags: typing.NotRequired[collections.abc.Sequence[ForumTag]]
    applied_tags: typing.NotRequired[collections.abc.Sequence[Snowflake]]
    default_reaction_emoji: typing.NotRequired[DefaultReaction]
    default_thread_rate_limit_per_user: typing.NotRequired[int]
    default_sort_order: typing.NotRequired[ChannelSortOrderType | None]
    default_forum_layout: typing.NotRequired[ForumLayoutType]


class Channel(PartialChannel):
    """
    See [here](https://discord.com/developers/docs/resources/channel#channels-resource)
    for Discord's documentation.
    """

    id: Snowflake
    type: ChannelType


class ChannelType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/channel#overwrite-object)
    for Discord's documentation.
    """

    ROLE = 0
    MEMBER = 1


class Overwrite(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/channel#overwrite-object)
    for Discord's documentation.
    """

    id: Snowflake
    type: int
    allow: UnparsedPermissionBitSet
    deny: UnparsedPermissionBitSet


class OverwriteType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/channel#overwrite-object-overwrite-types)
    for Discord's documentation.
    """

    ROLE = 0
    MEMBER = 1


class ThreadMetadata(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/channel#thread-metadata-object)
    for Discord's documentation.
    """

    archived: bool
    auto_archive_duration: int
    archive_timestamp: Iso8601Timestamp
    locked: bool
    invitable: typing.NotRequired[bool]
    create_timestamp: typing.NotRequired[Iso8601Timestamp | None]


class ThreadMember(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/channel#thread-member-object)
    for Discord's documentation.
    """

    id: typing.NotRequired[Snowflake]
    user_id: typing.NotRequired[Snowflake]
    join_timestamp: Iso8601Timestamp
    flags: int  # TODO: Find out what these can be
    member: typing.NotRequired[GuildMember]


class ChannelFlags(enum.IntFlag):
    """
    See [here](https://discord.com/developers/docs/resources/channel#channel-object-channel-flags)
    for Discord's documentation.
    """

    PINNED = 1 << 1
    REQUIRE_TAG = 1 << 4
    HIDE_MEDIA_DOWNLOAD_OPTIONS = 1 << 15


class ForumTag(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/channel#forum-tag-object)
    for Discord's documentation.
    """

    id: Snowflake
    name: str
    moderated: bool
    emoji_id: Snowflake | None
    emoji_name: str | None


class DefaultReaction(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/channel#default-reaction-object)
    for Discord's documentation.
    """

    emoji_id: Snowflake | None
    emoji_name: str | None


class ChannelSortOrderType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/channel#channel-object-sort-order-types)
    for Discord's documentation.
    """

    LATEST_ACTIVITY = 0
    CREATION_DATE = 1


class ForumLayoutType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/channel#channel-object-forum-layout-types)
    for Discord's documentation.
    """

    NOT_SET = 0
    DEFAULT = 0
    LIST_VIEW = 1
    GALLERY_VIEW = 2
