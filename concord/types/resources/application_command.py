from __future__ import annotations

import collections.abc
import enum
import re
import typing

from ..common import LanguageCode, Snowflake
from .application import ApplicationIntegrationType
from .channel import ChannelType

__all__ = (
    "ApplicationCommand",
    "ApplicationCommandType",
    "ApplicationCommandOption",
    "ApplicationCommandOptionType",
    "ApplicationCommandOptionChoice",
    "InteractionContextType",
    "EntryPointCommandHandlerType",
)


APPLICATION_COMMAND_NAME_REGEX = re.compile(r"^[\w-]{1,32}$")


class ApplicationCommand(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/interactions/application-commands#application-command-object)
    for Discord's documentation.
    """

    id: Snowflake
    type: typing.NotRequired[ApplicationCommandType]
    application_id: Snowflake
    guild_id: typing.NotRequired[Snowflake]
    name: str
    name_localizations: typing.NotRequired[typing.Mapping[LanguageCode, str]]
    description: typing.NotRequired[str]
    description_localizations: typing.NotRequired[typing.Mapping[LanguageCode, str]]
    options: typing.NotRequired[collections.abc.Sequence[ApplicationCommandOption]]
    default_member_permissions: str | None
    default_permission: typing.NotRequired[bool | None]
    nsfw: typing.NotRequired[bool]
    integration_types: typing.NotRequired[
        collections.abc.Sequence[ApplicationIntegrationType]
    ]
    contexts: typing.NotRequired[collections.abc.Sequence[InteractionContextType]]
    version: Snowflake
    handler: typing.NotRequired[EntryPointCommandHandlerType]


class ApplicationCommandType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-types)
    for Discord's documentation.
    """

    CHAT_INPUT = 1
    DEFAULT = 1
    USER = 2
    MESSAGE = 3
    PRIMARY_ENTRY_POINT = 4


class ApplicationCommandOption(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-structure)
    for Discord's documentation.
    """

    type: ApplicationCommandOptionType
    name: str
    name_localizations: typing.NotRequired[typing.Mapping[LanguageCode, str]]
    description: str
    description_localizations: typing.NotRequired[typing.Mapping[LanguageCode, str]]
    required: typing.NotRequired[bool]
    choices: typing.NotRequired[
        collections.abc.Sequence[ApplicationCommandOptionChoice]
    ]
    options: typing.NotRequired[collections.abc.Sequence[ApplicationCommandOption]]
    channel_types: typing.NotRequired[collections.abc.Sequence[ChannelType]]
    min_value: typing.NotRequired[int | float]
    max_value: typing.NotRequired[int | float]
    min_length: typing.NotRequired[int]
    max_length: typing.NotRequired[int]
    autocomplete: typing.NotRequired[bool]


class ApplicationCommandOptionType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-type)
    for Discord's documentation.
    """

    SUB_COMMAND = 1
    SUB_COMMAND_GROUP = 2
    STRING = 3
    INTEGER = 4
    BOOLEAN = 5
    USER = 6
    CHANNEL = 7
    ROLE = 8
    MENTIONABLE = 9
    NUMBER = 10
    ATTACHMENT = 11


class ApplicationCommandOptionChoice(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/interactions/application-commands#application-command-object-application-command-option-choice-structure)
    for Discord's documentation.
    """

    name: str
    name_localizations: typing.NotRequired[typing.Mapping[LanguageCode, str]]
    value: str | int | float


class InteractionContextType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-interaction-context-types)
    for Discord's documentation.
    """

    GUILD = 0
    BOT_DM = 1
    PRIVATE_CHANNEL = 2


class EntryPointCommandHandlerType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/interactions/application-commands#application-command-object-entry-point-command-handler-types)
    for Discord's documentation.
    """

    APP_HANDLER = 1
    DISCORD_LAUNCH_ACTIVITY = 2
