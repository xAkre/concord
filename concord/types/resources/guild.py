from __future__ import annotations

import enum
import typing

from ..common import LanguageCode, Snowflake
from .emoji import Emoji
from .role import Role
from .sticker import Sticker

__all__ = (
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
)


class Guild(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/guild)
    for Discord's documentation.
    """

    id: Snowflake
    name: str
    icon: str | None
    icon_hash: typing.NotRequired[str]
    splash: str | None
    discovery_splash: str | None
    owner: typing.NotRequired[bool]
    owner_id: Snowflake
    permissions: typing.NotRequired[str]
    afk_channel_id: Snowflake | None
    afk_timeout: int
    widget_enabled: typing.NotRequired[bool]
    widget_channel_id: typing.NotRequired[Snowflake | None]
    verification_level: GuildVerificationLevel
    default_message_notifications: GuildDefaultMessageNotificationLevel
    explicit_content_filter: GuildExplicitContentFilterLevel
    roles: typing.List[Role]
    emojis: typing.List[Emoji]
    features: typing.List[GuildFeature]
    mfa_level: GuildMfaLevel
    application_id: Snowflake | None
    system_channel_id: Snowflake | None
    system_channel_flags: int
    rules_channel_id: Snowflake | None
    max_presences: typing.NotRequired[int | None]
    max_members: typing.NotRequired[int]
    vanity_url_code: str | None
    description: str | None
    banner: str | None
    premium_tier: GuildPremiumTier
    premium_subscription_count: typing.NotRequired[int]
    preferred_locale: LanguageCode
    public_updates_channel_id: Snowflake | None
    max_video_channel_users: typing.NotRequired[int]
    max_stage_video_channel_users: typing.NotRequired[int]
    approximate_member_count: typing.NotRequired[int]
    approximate_presence_count: typing.NotRequired[int]
    welcome_screen: typing.NotRequired[GuildWelcomeScreen]
    nsfw_level: GuildNsfwLevel
    stickers: typing.NotRequired[typing.List[Sticker]]
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
    welcome_channels: typing.NotRequired[typing.List[GuildWelcomeScreenChannel]]
