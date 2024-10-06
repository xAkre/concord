# mypy: disable-error-code="misc"
# This is needed because Mypy complains when overriding fields in a TypedDict.

from __future__ import annotations

import collections.abc
import enum
import typing

from ..common import Iso8601Timestamp, Snowflake
from .application import ApplicationIntegrationType, PartialApplication
from .channel import Channel, ChannelType, PartialChannel
from .emoji import PartialEmoji
from .guild import PartialGuildMember
from .interaction import InteractionType
from .message_component import MessageComponent
from .poll import Poll
from .role import Role
from .sticker import Sticker, StickerItem
from .user import User

__all__ = (
    "PartialMessage",
    "Message",
    "ChannelMention",
    "MessageAttachment",
    "MessageAttachmentFlags",
    "MessageEmbed",
    "MessageEmbedType",
    "MessageEmbedFooter",
    "MessageEmbedImage",
    "MessageEmbedThumbnail",
    "MessageEmbedVideo",
    "MessageEmbedProvider",
    "MessageEmbedAuthor",
    "MessageEmbedField",
    "MessageReaction",
    "MessageReactionCountDetails",
    "MessageType",
    "MessageActivity",
    "MessageActivityType",
    "MessageFlags",
    "MessageReference",
    "MessageReferenceType",
    "MessageSnapshot",
    "MessageInteractionMetadata",
    "MessageRoleSubscriptionData",
    "MessageResolvedData",
    "MessageCall",
)


class PartialMessage(typing.TypedDict):
    """
    Represents a partial message object in Discord.

    A partial message is guaranteed to contain only an ID. While not explicitly
    documented in the official docs, this assumption is recommended by users in
    the Discord Developers server.

    Other fields may be present but should not be relied upon in a partial message
    object.
    """

    id: Snowflake
    channel_id: typing.NotRequired[Snowflake]
    author: typing.NotRequired[User]
    content: typing.NotRequired[str]
    timestamp: typing.NotRequired[Iso8601Timestamp]
    edited_timestamp: typing.NotRequired[Iso8601Timestamp | None]
    tts: typing.NotRequired[bool]
    mention_everyone: typing.NotRequired[bool]
    mentions: typing.NotRequired[collections.abc.Sequence[User]]
    mention_roles: typing.NotRequired[collections.abc.Sequence[Snowflake]]
    mention_channels: typing.NotRequired[collections.abc.Sequence[ChannelMention]]
    attachments: typing.NotRequired[collections.abc.Sequence[MessageAttachment]]
    embeds: typing.NotRequired[collections.abc.Sequence[MessageEmbed]]
    reactions: typing.NotRequired[collections.abc.Sequence[MessageReaction]]
    nonce: typing.NotRequired[str | int]
    pinned: typing.NotRequired[bool]
    webhook_id: typing.NotRequired[Snowflake]
    type: typing.NotRequired[MessageType]
    activity: typing.NotRequired[MessageActivity]
    application: typing.NotRequired[PartialApplication]
    application_id: typing.NotRequired[Snowflake]
    flags: typing.NotRequired[int]
    message_reference: typing.NotRequired[MessageReference]
    message_snapshots: typing.NotRequired[collections.abc.Sequence[MessageSnapshot]]
    referenced_message: typing.NotRequired[Message]
    thread: typing.NotRequired[Channel]
    components: typing.NotRequired[collections.abc.Sequence[MessageComponent]]
    sticker_items: typing.NotRequired[collections.abc.Sequence[StickerItem]]
    stickers: typing.NotRequired[collections.abc.Sequence[Sticker]]
    position: typing.NotRequired[int]
    role_subscription_data: typing.NotRequired[MessageRoleSubscriptionData]
    resolved: typing.NotRequired[MessageResolvedData]
    poll: typing.NotRequired[Poll]
    call: typing.NotRequired[MessageCall]


class Message(PartialMessage):
    """
    See [here](https://discord.com/developers/docs/resources/message)
    for Discord's documentation.
    """

    id: Snowflake
    channel_id: Snowflake
    author: User
    content: str
    timestamp: Iso8601Timestamp
    edited_timestamp: Iso8601Timestamp | None
    tts: bool
    mention_everyone: bool
    mentions: collections.abc.Sequence[User]
    mention_roles: collections.abc.Sequence[Snowflake]
    pinned: bool
    type: MessageType


class ChannelMention(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/message#channel-mention-object)
    for Discord's documentation.
    """

    id: Snowflake
    guild_id: Snowflake
    type: ChannelType
    name: str


class MessageAttachment(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/message#attachment-object)
    for Discord's documentation.
    """

    id: Snowflake
    filename: str
    title: typing.NotRequired[str]
    description: typing.NotRequired[str]
    content_type: typing.NotRequired[str]
    size: int
    url: str
    proxy_url: str
    height: typing.NotRequired[int]
    width: typing.NotRequired[int]
    ephemeral: typing.NotRequired[bool]
    duration_secs: typing.NotRequired[int]
    waveform: typing.NotRequired[str]
    flags: typing.NotRequired[int]


class MessageAttachmentFlags(enum.IntFlag):
    """
    See [here](https://discord.com/developers/docs/resources/message#attachment-object-attachment-flags)
    for Discord's documentation.
    """

    IS_REMIX = 1 << 2


class MessageEmbed(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/message#embed-object)
    for Discord's documentation.
    """

    title: typing.NotRequired[str]
    type: typing.NotRequired[MessageEmbedType]
    description: typing.NotRequired[str]
    url: typing.NotRequired[str]
    timestamp: typing.NotRequired[Iso8601Timestamp]
    color: typing.NotRequired[int]
    footer: typing.NotRequired[MessageEmbedFooter]
    image: typing.NotRequired[MessageEmbedImage]
    thumbnail: typing.NotRequired[MessageEmbedThumbnail]
    video: typing.NotRequired[MessageEmbedVideo]
    provider: typing.NotRequired[MessageEmbedProvider]
    author: typing.NotRequired[MessageEmbedAuthor]
    fields: typing.NotRequired[collections.abc.Sequence[MessageEmbedField]]


class MessageEmbedType(enum.StrEnum):
    """
    See [here](https://discord.com/developers/docs/resources/message#embed-object-embed-types)
    for Discord's documentation.
    """

    RICH = "rich"
    IMAGE = "image"
    VIDEO = "video"
    GIFV = "gifv"
    ARTICLE = "article"
    LINK = "link"
    POLL_RESULT = "poll_result"


class MessageEmbedFooter(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/message#embed-object-embed-footer-structure)
    for Discord's documentation.
    """

    text: str
    icon_url: typing.NotRequired[str]
    proxy_icon_url: typing.NotRequired[str]


class MessageEmbedImage(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/message#embed-object-embed-image-structure)
    for Discord's documentation.
    """

    url: str
    proxy_url: typing.NotRequired[str]
    height: typing.NotRequired[int]
    width: typing.NotRequired[int]


class MessageEmbedThumbnail(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/message#embed-object-embed-thumbnail-structure)
    for Discord's documentation.
    """

    url: str
    proxy_url: typing.NotRequired[str]
    height: typing.NotRequired[int]
    width: typing.NotRequired[int]


class MessageEmbedVideo(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/message#embed-object-embed-video-structure)
    for Discord's documentation.
    """

    url: typing.NotRequired[str]
    proxy_url: typing.NotRequired[str]
    height: typing.NotRequired[int]
    width: typing.NotRequired[int]


class MessageEmbedProvider(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/message#embed-object-embed-provider-structure)
    for Discord's documentation.
    """

    name: typing.NotRequired[str]
    url: typing.NotRequired[str]


class MessageEmbedAuthor(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/message#embed-object-embed-author-structure)
    for Discord's documentation.
    """

    name: str
    url: typing.NotRequired[str]
    icon_url: typing.NotRequired[str]
    proxy_icon_url: typing.NotRequired[str]


class MessageEmbedField(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/message#embed-object-embed-field-structure)
    for Discord's documentation.
    """

    name: str
    value: str
    inline: typing.NotRequired[bool]


class MessageReaction(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/message#reaction-object)
    for Discord's documentation.
    """

    count: int
    count_details: MessageReactionCountDetails
    me: bool
    me_burst: bool
    emoji: PartialEmoji
    burst_colors: collections.abc.Sequence[int]


class MessageReactionCountDetails(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/message#reaction-count-details-object
    for Discord's documentation.
    """

    burst: int
    normal: int


class MessageType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/message#message-object-message-types)
    for Discord's documentation.
    """

    DEFAULT = 0
    RECIPIENT_ADD = 1
    RECIPIENT_REMOVE = 2
    CALL = 3
    CHANNEL_NAME_CHANGE = 4
    CHANNEL_ICON_CHANGE = 5
    CHANNEL_PINNED_MESSAGE = 6
    USER_JOIN = 7
    GUILD_BOOST = 8
    GUILD_BOOST_TIER_1 = 9
    GUILD_BOOST_TIER_2 = 10
    GUILD_BOOST_TIER_3 = 11
    CHANNEL_FOLLOW_ADD = 12
    GUILD_DISCOVERY_DISQUALIFIED = 14
    GUILD_DISCOVERY_REQUALIFIED = 15
    GUILD_DISCOVERY_GRACE_PERIOD_INITIAL_WARNING = 16
    GUILD_DISCOVERY_GRACE_PERIOD_FINAL_WARNING = 17
    THREAD_CREATED = 18
    REPLY = 19
    CHAT_INPUT_COMMAND = 20
    THREAD_STARTER_MESSAGE = 21
    GUILD_INVITE_REMINDER = 22
    CONTEXT_MENU_COMMAND = 23
    AUTO_MODERATION_ACTION = 24
    ROLE_SUBSCRIPTION_PURCHASE = 25
    INTERACTION_PREMIUM_UPSELL = 26
    STAGE_START = 27
    STAGE_END = 28
    STAGE_SPEAKER = 29
    STAGE_TOPIC = 31
    GUILD_APPLICATION_PREMIUM_SUBSCRIPTION = 32
    GUILD_INCIDENT_ALERT_MODE_ENABLED = 36
    GUILD_INCIDENT_ALERT_MODE_DISABLED = 37
    GUILD_INCIDENT_REPORT_RAID = 38
    GUILD_INCIDENT_REPORT_FALSE_ALARM = 39
    PURCHASE_NOTIFICATION = 44
    POLL_RESULT = 46


class MessageActivity(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/message#message-object-message-activity-structure)
    for Discord's documentation.
    """

    type: MessageActivityType
    party_id: typing.NotRequired[str]


class MessageActivityType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/message#message-object-message-activity-types)
    for Discord's documentation.
    """

    JOIN = 1
    SPECTATE = 2
    LISTEN = 3
    JOIN_REQUEST = 5


class MessageFlags(enum.IntFlag):
    """
    See [here](https://discord.com/developers/docs/resources/message#message-object-message-flags)
    for Discord's documentation.
    """

    CROSSPOSTED = 1 << 0
    IS_CROSSPOST = 1 << 1
    SUPPRESS_EMBEDS = 1 << 2
    SOURCE_MESSAGE_DELETED = 1 << 3
    URGENT = 1 << 4
    HAS_THREAD = 1 << 5
    EPHEMERAL = 1 << 6
    LOADING = 1 << 7
    FAILED_TO_MENTION_SOME_ROLES_IN_THREAD = 1 << 8
    SUPPRESS_NOTIFICATIONS = 1 << 12
    IS_VOICE_MESSAGE = 1 << 13


class MessageReference(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/message#message-reference-structure)
    for Discord's documentation.
    """

    type: typing.NotRequired[MessageReferenceType]
    message_id: typing.NotRequired[Snowflake]
    channel_id: typing.NotRequired[Snowflake]
    guild_id: typing.NotRequired[Snowflake]
    fail_if_not_exists: typing.NotRequired[bool]


class MessageReferenceType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/message#message-reference-types)
    for Discord's documentation.
    """

    DEFAULT = 0
    FORWARD = 1


class MessageSnapshot(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/message#message-snapshot-object)
    for Discord's documentation.
    """

    type: MessageType
    content: str
    embeds: typing.NotRequired[collections.abc.Sequence[MessageEmbed]]
    attachments: typing.NotRequired[collections.abc.Sequence[MessageAttachment]]
    timestamp: Iso8601Timestamp
    edited_timestamp: Iso8601Timestamp | None
    flags: typing.NotRequired[int]
    mentions: collections.abc.Sequence[User]
    mention_roles: collections.abc.Sequence[Snowflake]
    stickers: typing.NotRequired[collections.abc.Sequence[Sticker]]
    sticker_items: typing.NotRequired[collections.abc.Sequence[StickerItem]]
    components: typing.NotRequired[collections.abc.Sequence[MessageComponent]]


class MessageInteractionMetadata(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/message#message-interaction-metadata-object-message-interaction-metadata-structure)
    for Discord's documentation.
    """

    id: Snowflake
    type: InteractionType
    user: User
    authorizing_integration_owners: collections.abc.Mapping[
        ApplicationIntegrationType, typing.Any
    ]
    original_response_message_id: typing.NotRequired[Snowflake]
    interacted_message_id: typing.NotRequired[Snowflake]
    triggering_interaction_metadata: typing.NotRequired[MessageInteractionMetadata]


class MessageRoleSubscriptionData(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/message#role-subscription-data-object)
    for Discord's documentation.
    """

    role_subscription_listing_id: Snowflake
    tier_name: str
    total_months_subscribed: int
    is_renewal: bool


class MessageResolvedData(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-resolved-data-structure)
    for Discord's documentation.
    """

    users: typing.NotRequired[collections.abc.Mapping[Snowflake, User]]
    channels: typing.NotRequired[collections.abc.Mapping[Snowflake, PartialGuildMember]]
    roles: typing.NotRequired[collections.abc.Mapping[Snowflake, Role]]
    channels: typing.NotRequired[collections.abc.Mapping[Snowflake, PartialChannel]]
    messages: typing.NotRequired[collections.abc.Mapping[Snowflake, PartialMessage]]
    attachments: typing.NotRequired[
        collections.abc.Mapping[Snowflake, MessageAttachment]
    ]


class MessageCall(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/message#message-call-object)
    for Discord's documentation.
    """

    participants: collections.abc.Sequence[Snowflake]
    ended_timestamp: typing.NotRequired[Iso8601Timestamp | None]
