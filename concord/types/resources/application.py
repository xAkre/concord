# mypy: disable-error-code="misc"
# This is needed because Mypy complains when overriding fields in a TypedDict.

from __future__ import annotations

import collections.abc
import enum
import typing

from ..common import OAuth2Scopes, Snowflake
from .guild import PartialGuild
from .team import Team
from .user import PartialUser

__all__ = (
    "PartialApplication",
    "Application",
    "ApplicationFlags",
    "ApplicationInstallParams",
    "ApplicationIntegrationType",
    "ApplicationIntegrationTypeConfiguration",
)


class PartialApplication(typing.TypedDict):
    """
    Represents a partial application object in Discord.

    A partial application is guaranteed to contain only an ID. While not explicitly
    documented in the official docs, this assumption is recommended by users in
    the Discord Developers server.

    Other fields may be present but should not be relied upon in a partial application
    object.
    """

    id: Snowflake
    name: typing.NotRequired[str]
    icon: typing.NotRequired[str | None]
    description: typing.NotRequired[str]
    rpc_origins: typing.NotRequired[collections.abc.Sequence[str]]
    bot_public: typing.NotRequired[bool]
    bot_require_code_grant: typing.NotRequired[bool]
    bot: typing.NotRequired[PartialUser]
    terms_of_service_url: typing.NotRequired[str]
    privacy_policy_url: typing.NotRequired[str]
    owner: typing.NotRequired[PartialUser]
    verify_key: typing.NotRequired[str]
    team: typing.NotRequired[Team | None]
    guild_id: typing.NotRequired[Snowflake]
    guild: typing.NotRequired[PartialGuild]
    primary_sku_id: typing.NotRequired[Snowflake]
    slug: typing.NotRequired[str]
    cover_image: typing.NotRequired[str]
    flags: typing.NotRequired[int]
    approximate_guild_count: typing.NotRequired[int]
    approximate_user_install_count: typing.NotRequired[int]
    redirect_uris: typing.NotRequired[collections.abc.Sequence[str]]
    interactions_endpoint_url: typing.NotRequired[str | None]
    role_connections_verification_url: typing.NotRequired[str | None]
    tags: typing.NotRequired[collections.abc.Sequence[str]]
    install_params: typing.NotRequired[ApplicationInstallParams]
    integration_types_config: typing.NotRequired[
        typing.Mapping[
            ApplicationIntegrationType, ApplicationIntegrationTypeConfiguration
        ]
    ]
    custom_install_url: typing.NotRequired[str]


class Application(PartialApplication):
    """
    See [here](https://discord.com/developers/docs/resources/application)
    for Discord's documentation.
    """

    id: Snowflake
    name: str
    icon: str | None
    description: str
    bot_public: bool
    bot_require_code_grant: bool
    verify_key: str
    team: Team | None


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

    scopes: collections.abc.Sequence[OAuth2Scopes]
    permissions: collections.abc.Sequence[collections.abc.Sequence[str]]


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
