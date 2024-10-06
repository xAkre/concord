from __future__ import annotations

import collections.abc
import enum
import typing

from ..common import (
    Iso8601Timestamp,
    LanguageCode,
    OAuth2Scopes,
    Snowflake,
    UnparsedPermissionBitSet,
)
from .emoji import Emoji
from .role import Role
from .sticker import Sticker
from .user import AvatarDecoration, User

__all__ = (
    "PartialGuild",
    "Guild",
    "GuildFeature",
    "GuildVerificationLevel",
    "GuildDefaultMessageNotificationLevel",
    "GuildExplicitContentFilterLevel",
    "GuildMfaLevel",
    "GuildSystemChannelFlags",
    "GuildPremiumTier",
    "GuildNsfwLevel",
    "GuildWelcomeScreen",
    "GuildWelcomeScreenChannel",
    "GuildMember",
    "GuildMemberFlags",
)


class PartialGuild(typing.TypedDict):
    """
    Represents a partial guild object in Discord.

    A partial guild is guaranteed to contain only an ID. While not explicitly
    documented in the official docs, this assumption is recommended by users in
    the Discord Developers server.

    Other fields may be present but should not be relied upon in a partial guild object.
    """

    id: Snowflake
    name: typing.NotRequired[str]
    icon: typing.NotRequired[str | None]
    icon_hash: typing.NotRequired[str]
    splash: typing.NotRequired[str | None]
    discovery_splash: typing.NotRequired[str | None]
    owner: typing.NotRequired[bool]
    owner_id: typing.NotRequired[Snowflake]
    permissions: typing.NotRequired[str]
    afk_channel_id: typing.NotRequired[Snowflake | None]
    afk_timeout: typing.NotRequired[int]
    widget_enabled: typing.NotRequired[bool]
    widget_channel_id: typing.NotRequired[Snowflake | None]
    verification_level: typing.NotRequired[GuildVerificationLevel]
    default_message_notifications: typing.NotRequired[
        GuildDefaultMessageNotificationLevel
    ]
    explicit_content_filter: typing.NotRequired[GuildExplicitContentFilterLevel]
    roles: typing.NotRequired[collections.abc.Sequence[Role]]
    emojis: typing.NotRequired[collections.abc.Sequence[Emoji]]
    features: typing.NotRequired[collections.abc.Sequence[GuildFeature]]
    mfa_level: typing.NotRequired[GuildMfaLevel]
    application_id: typing.NotRequired[Snowflake | None]
    system_channel_id: typing.NotRequired[Snowflake | None]
    system_channel_flags: typing.NotRequired[int]
    rules_channel_id: typing.NotRequired[Snowflake | None]
    max_presences: typing.NotRequired[int | None]
    max_members: typing.NotRequired[int]
    vanity_url_code: typing.NotRequired[str | None]
    description: typing.NotRequired[str | None]
    banner: typing.NotRequired[str | None]
    premium_tier: typing.NotRequired[GuildPremiumTier]
    premium_subscription_count: typing.NotRequired[int]
    preferred_locale: typing.NotRequired[LanguageCode]
    public_updates_channel_id: typing.NotRequired[Snowflake | None]
    max_video_channel_users: typing.NotRequired[int]
    max_stage_video_channel_users: typing.NotRequired[int]
    approximate_member_count: typing.NotRequired[int]
    approximate_presence_count: typing.NotRequired[int]
    welcome_screen: typing.NotRequired[GuildWelcomeScreen]
    nsfw_level: typing.NotRequired[GuildNsfwLevel]
    stickers: typing.NotRequired[collections.abc.Sequence[Sticker]]
    premium_progress_bar_enabled: typing.NotRequired[bool]
    safety_alerts_channel_id: typing.NotRequired[Snowflake | None]


class Guild(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/guild)
    for Discord's documentation.
    """

    id: Snowflake
    name: str
    icon: str | None
    splash: str | None
    discovery_splash: str | None
    owner_id: Snowflake
    afk_channel_id: Snowflake | None
    afk_timeout: int
    verification_level: GuildVerificationLevel
    default_message_notifications: GuildDefaultMessageNotificationLevel
    explicit_content_filter: GuildExplicitContentFilterLevel
    roles: collections.abc.Sequence[Role]
    emojis: collections.abc.Sequence[Emoji]
    features: collections.abc.Sequence[GuildFeature]
    mfa_level: GuildMfaLevel
    application_id: Snowflake | None
    system_channel_id: Snowflake | None
    system_channel_flags: int
    rules_channel_id: Snowflake | None
    vanity_url_code: str | None
    description: str | None
    banner: str | None
    premium_tier: GuildPremiumTier
    preferred_locale: LanguageCode
    public_updates_channel_id: Snowflake | None
    nsfw_level: GuildNsfwLevel
    premium_progress_bar_enabled: bool
    safety_alerts_channel_id: Snowflake | None


class GuildFeature(enum.StrEnum):
    """
    See [here](https://discord.com/developers/docs/resources/guild#guild-object-guild-features)
    for Discord's documentation.
    """

    ANIMATED_BANNER = "ANIMATED_BANNER"
    ANIMATED_ICON = "ANIMATED_ICON"
    APPLICATION_COMMAND_PERMISSIONS_V2 = "APPLICATION_COMMAND_PERMISSIONS_V2"
    AUTO_MODERATION = "AUTO_MODERATION"
    BANNER = "BANNER"
    COMMUNITY = "COMMUNITY"
    CREATOR_MONETIZABLE_PROVISIONAL = "CREATOR_MONETIZABLE_PROVISIONAL"
    CREATOR_STORE_PAGE = "CREATOR_STORE_PAGE"
    DEVELOPER_SUPPORT_SERVER = "DEVELOPER_SUPPORT_SERVER"
    DISCOVERABLE = "DISCOVERABLE"
    FEATURABLE = "FEATURABLE"
    INVITES_ENABLED = "INVITES_ENABLED"
    INVITE_SPLASH = "INVITE_SPLASH"
    MEMBER_VERIFICATION_GATE_ENABLED = "MEMBER_VERIFICATION_GATE_ENABLED"
    MORE_SOUNDBOARD = "MORE_SOUNDBOARD"
    MORE_STICKERS = "MORE_STICKERS"
    NEWS = "NEWS"
    PARTNERED = "PARTNERED"
    PREVIEW_ENABLED = "PREVIEW_ENABLED"
    RAID_ALERTS_DISABLED = "RAID_ALERTS_DISABLED"
    ROLE_ICONS = "ROLE_ICONS"
    ROLE_SUBSCRIPTIONS_AVAILABLE_FOR_PURCHASE = (
        "ROLE_SUBSCRIPTIONS_AVAILABLE_FOR_PURCHASE"
    )
    ROLE_SUBSCRIPTIONS_ENABLED = "ROLE_SUBSCRIPTIONS_ENABLED"
    SOUNDBOARD = "SOUNDBOARD"
    TICKETED_EVENTS_ENABLED = "TICKETED_EVENTS_ENABLED"
    VANITY_URL = "VANITY_URL"
    VERIFIED = "VERIFIED"
    VIP_REGIONS = "VIP_REGIONS"
    WELCOME_SCREEN_ENABLED = "WELCOME_SCREEN_ENABLED"


class GuildVerificationLevel(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/guild#guild-object-verification-level)
    for Discord's documentation.
    """

    NONE = 0
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    VERY_HIGH = 4


class GuildDefaultMessageNotificationLevel(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/guild#guild-object-default-message-notification-level)
    for Discord's documentation.
    """

    ALL_MESSAGES = 0
    ONLY_MENTIONS = 1


class GuildExplicitContentFilterLevel(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/guild#guild-object-explicit-content-filter-level)
    for Discord's documentation.
    """

    DISABLED = 0
    MEMBERS_WITHOUT_ROLES = 1
    ALL_MEMBERS = 2


# Other Guild-related enums
class GuildMfaLevel(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/guild#guild-object-mfa-level)
    for Discord's documentation.
    """

    NONE = 0
    ELEVATED = 1


class GuildSystemChannelFlags(enum.IntFlag):
    """
    See [here](https://discord.com/developers/docs/resources/guild#guild-object-system-channel-flags)
    for Discord's documentation.
    """

    SUPPRESS_JOIN_NOTIFICATIONS = 1 << 0
    SUPPRESS_PREMIUM_SUBSCRIPTIONS = 1 << 1
    SUPPRESS_GUILD_REMINDER_NOTIFICATIONS = 1 << 2
    SUPPRESS_JOIN_NOTIFICATION_REPLIES = 1 << 3
    SUPPRESS_ROLE_SUBSCRIPTION_PURCHASE_NOTIFICATIONS = 1 << 4
    SUPPRESS_ROLE_SUBSCRIPTION_PURCHASE_NOTIFICATION_REPLIES = 1 << 5


class GuildPremiumTier(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/guild#guild-object-premium-tier)
    for Discord's documentation.
    """

    NONE = 0
    TIER_1 = 1
    TIER_2 = 2
    TIER_3 = 3


class GuildNsfwLevel(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/guild#guild-object-guild-nsfw-level)
    for Discord's documentation.
    """

    DEFAULT = 0
    EXPLICIT = 1
    SAFE = 2
    AGE_RESTRICTED = 3


class GuildWelcomeScreenChannel(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/guild#welcome-screen-object-welcome-screen-channel-structure)
    for Discord's documentation.
    """

    channel_id: Snowflake
    description: str
    emoji_id: Snowflake | None
    emoji_name: str | None


class GuildWelcomeScreen(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/guild#welcome-screen-object-welcome-screen-structure)
    for Discord's documentation.
    """

    description: typing.NotRequired[str]
    welcome_channels: typing.NotRequired[
        collections.abc.Sequence[GuildWelcomeScreenChannel]
    ]


class GuildMember(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/guild#guild-member-object)
    for Discord's documentation.
    """

    user: typing.NotRequired[User]
    nick: typing.NotRequired[str | None]
    avatar: typing.NotRequired[str | None]
    roles: collections.abc.Sequence[Snowflake]
    joined_at: Iso8601Timestamp
    premium_since: typing.NotRequired[Iso8601Timestamp | None]
    deaf: bool
    mute: bool
    flags: int
    pending: typing.NotRequired[bool]
    permission: typing.NotRequired[UnparsedPermissionBitSet]
    communication_disabled_until: typing.NotRequired[Iso8601Timestamp | None]
    avatar_decoration_data: typing.NotRequired[AvatarDecoration | None]


class GuildMemberFlags(enum.IntFlag):
    """
    See [here](https://discord.com/developers/docs/resources/guild#guild-member-object-guild-member-flags)
    for Discord's documentation.
    """

    DID_REJOIN = 1 << 0
    COMPLETED_ONBOARDING = 1 << 1
    BYPASSES_VERIFICATION = 1 << 2
    STARTED_ONBOARDING = 1 << 3
    IS_GUEST = 1 << 4
    STARTED_HOME_ACTIONS = 1 << 5
    COMPLETED_HOME_ACTIONS = 1 << 6
    AUTOMOD_QUARANTINED_USERNAME = 1 << 7
    DM_SETTINGS_UPSELL_ACKNOWLEDGED = 1 << 8


class GuildIntegration(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/guild#integration-object)
    for Discord's documentation.
    """

    id: Snowflake
    name: str
    type: GuildIntegrationType
    enabled: bool
    syncing: typing.NotRequired[bool]
    role_id: typing.NotRequired[Snowflake]
    enable_emoticons: typing.NotRequired[bool]
    expire_behavior: typing.NotRequired[GuildIntegrationExpireBehavior]
    expire_grace_period: typing.NotRequired[int]
    user: typing.NotRequired[User]
    account: typing.NotRequired[GuildIntegrationAccount]
    synced_at: typing.NotRequired[Iso8601Timestamp]
    subscriber_count: typing.NotRequired[int]
    revoked: typing.NotRequired[bool]
    application: typing.NotRequired[GuildIntegrationApplication]
    scopes: typing.NotRequired[collections.abc.Sequence[OAuth2Scopes]]


class GuildIntegrationType(enum.StrEnum):
    """
    See [here](https://discord.com/developers/docs/resources/guild#integration-object)
    for Discord's documentation.
    """

    TWITCH = "twitch"
    YOUTUBE = "youtube"
    DISCORD = "discord"
    GUILD_SUBSCRIPTION = "guild_subscription"


class GuildIntegrationExpireBehavior(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/guild#integration-object-integration-expire-behaviors)
    for Discord's documentation.
    """

    REMOVE_ROLE = 0
    KICK = 1


class GuildIntegrationAccount(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/guild#integration-account-object)
    for Discord's documentation.
    """

    id: Snowflake
    name: str


class GuildIntegrationApplication(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/guild#integration-application-object)
    for Discord's documentation.
    """

    id: Snowflake
    name: str
    icon: str | None
    description: str
    bot: typing.NotRequired[User]
