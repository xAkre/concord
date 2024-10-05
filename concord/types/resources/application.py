from __future__ import annotations

import enum
import typing

from ..common import Snowflake
from ..enums import OAuth2Scopes
from .guild import Guild
from .team import Team
from .user import User

__all__ = (
    "Application",
    "ApplicationFlags",
    "ApplicationInstallParams",
    "ApplicationIntegrationType",
    "ApplicationIntegrationTypeConfiguration",
)


class Application(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/application)
    for Discord's documentation.
    """

    id: Snowflake
    name: str
    icon: str | None
    description: str
    rpc_origins: typing.NotRequired[typing.List[str]]
    bot_public: bool
    bot_require_code_grant: bool
    bot: typing.NotRequired[User]
    """Partial user object."""
    terms_of_service_url: typing.NotRequired[str]
    privacy_policy_url: typing.NotRequired[str]
    owner: typing.NotRequired[User]
    """Partial user object."""
    verify_key: str
    team: Team | None
    guild_id: typing.NotRequired[Snowflake]
    guild: typing.NotRequired[Guild]
    """Partial guild object."""
    primary_sku_id: typing.NotRequired[Snowflake]
    slug: typing.NotRequired[str]
    cover_image: typing.NotRequired[str]
    flags: typing.NotRequired[int]
    approximate_guild_count: typing.NotRequired[int]
    approximate_user_install_count: typing.NotRequired[int]
    redirect_uris: typing.NotRequired[typing.List[str]]
    interactions_endpoint_url: typing.NotRequired[str | None]
    role_connections_verification_url: typing.NotRequired[str | None]
    tags: typing.NotRequired[typing.List[str]]
    install_params: typing.NotRequired[ApplicationInstallParams]
    integration_types_config: typing.NotRequired[
        typing.Mapping[
            ApplicationIntegrationType, ApplicationIntegrationTypeConfiguration
        ]
    ]
    custom_install_url: typing.NotRequired[str]


class ApplicationFlags(enum.IntFlag):
    """
    See [here](https://discord.com/developers/docs/resources/application#application-object-application-flags)
    for Discord's documentation.
    """

    APPLICATION_AUTO_MODERATION_RULE_CREATE_BADGE = 1 << 6
    GATEWAY_PRESENCE = 1 << 12
    GATEWAY_PRESENCE_LIMITED = 1 << 13
    GATEWAY_GUILD_MEMBERS = 1 << 14
    GATEWAY_GUILD_MEMBERS_LIMITED = 1 << 15
    VERIFICATION_PENDING_GUILD_LIMIT = 1 << 16
    EMBEDDED = 1 << 17
    GATEWAY_MESSAGE_CONTENT = 1 << 18
    GATEWAY_MESSAGE_CONTENT_LIMITED = 1 << 19
    APPLICATION_COMMAND_BADGE = 1 << 23


class ApplicationInstallParams(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/application#install-params-object)
    for Discord's documentation.
    """

    scopes: typing.List[OAuth2Scopes]
    permissions: typing.List[typing.List[str]]


class ApplicationIntegrationType(enum.StrEnum):
    """
    See [here](https://discord.com/developers/docs/resources/application#application-object-application-integration-types)
    for Discord's documentation.
    """

    GUILD_INSTALL = "GUILD_INSTALL"
    USER_INSTALL = "USER_INSTALL"


class ApplicationIntegrationTypeConfiguration(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/application#application-object-application-integration-type-configuration-object)
    for Discord's documentation.
    """

    oauth2_install_params: typing.NotRequired[ApplicationInstallParams]
