from __future__ import annotations

import collections.abc
import enum
import typing

from ..common import Snowflake
from .channel import ChannelType
from .emoji import PartialEmoji

__all__ = (
    "ComponentType",
    "ActionRow",
    "Button",
    "ButtonStyle",
    "SelectMenu",
    "SelectMenuOption",
    "SelectMenuDefaultValue",
    "SelectMenuDefaultValueType",
    "TextInput",
    "TextInputStyle",
    "MessageComponent",
)


class ComponentType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/interactions/message-components#component-object-component-types)
    for Discord's documentation.
    """

    ACTION_ROW = 1
    BUTTON = 2
    STRING_SELECT = 3
    TEXT_INPUT = 4
    USER_SELECT = 5
    ROLE_SELECT = 6
    MENTIONABLE_SELECT = 7
    CHANNEL_SELECT = 8


class ActionRow(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/interactions/message-components#action-rows)
    for Discord's documentation.
    """

    type: typing.Literal[ComponentType.ACTION_ROW]
    components: collections.abc.Sequence[Button | SelectMenu | TextInput]


class Button(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/interactions/message-components#button-object)
    for Discord's documentation.
    """

    type: typing.Literal[ComponentType.BUTTON]
    style: ButtonStyle
    label: typing.NotRequired[str]
    emoji: typing.NotRequired[PartialEmoji]
    custom_id: typing.NotRequired[str]
    sku_id: typing.NotRequired[str]
    url: typing.NotRequired[str]
    disabled: typing.NotRequired[bool]


class ButtonStyle(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/interactions/message-components#button-object-button-styles)
    for Discord's documentation.
    """

    PRIMARY = 1
    SECONDARY = 2
    SUCCESS = 3
    DANGER = 4
    LINK = 5
    PREMIUM = 6


class SelectMenu(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/interactions/message-components#select-menu-object)
    for Discord's documentation.
    """

    type: (
        typing.Literal[ComponentType.TEXT_INPUT]
        | typing.Literal[ComponentType.STRING_SELECT]
        | typing.Literal[ComponentType.ROLE_SELECT]
        | typing.Literal[ComponentType.MENTIONABLE_SELECT]
        | typing.Literal[ComponentType.CHANNEL_SELECT]
    )
    custom_id: str
    options: typing.NotRequired[collections.abc.Sequence[SelectMenuOption]]
    channel_types: typing.NotRequired[collections.abc.Sequence[ChannelType]]
    placeholder: typing.NotRequired[str]
    default_values: typing.NotRequired[collections.abc.Sequence[SelectMenuDefaultValue]]
    min_values: typing.NotRequired[int]
    max_values: typing.NotRequired[int]
    disabled: typing.NotRequired[bool]


class SelectMenuOption(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/interactions/message-components#select-menu-object-select-option-structure)
    for Discord's documentation.
    """

    label: str
    value: str
    description: typing.NotRequired[str]
    emoji: typing.NotRequired[PartialEmoji]
    """ID, name, and animated"""
    default: typing.NotRequired[bool]


class SelectMenuDefaultValue(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/interactions/message-components#select-menu-object-select-default-value-structure)
    for Discord's documentation.
    """

    id: Snowflake
    type: SelectMenuDefaultValueType


class SelectMenuDefaultValueType(enum.StrEnum):
    """
    See [here](https://discord.com/developers/docs/interactions/message-components#select-menu-object-select-default-value-structure)
    for Discord's documentation.
    """

    USER = "user"
    ROLE = "role"
    CHANNEL = "channel"


class TextInput(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/interactions/message-components#text-input-object)
    for Discord's documentation.
    """

    type: typing.Literal[ComponentType.TEXT_INPUT]
    custom_id: str
    style: TextInputStyle
    label: str
    min_length: typing.NotRequired[int]
    max_length: typing.NotRequired[int]
    required: typing.NotRequired[bool]
    value: typing.NotRequired[str]
    placeholder: typing.NotRequired[str]


class TextInputStyle(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/interactions/message-components#text-input-object-text-input-styles)
    for Discord's documentation.
    """

    SHORT = 1
    PARAGRAPH = 2


MessageComponent: typing.TypeAlias = ActionRow | Button | SelectMenu | TextInput
"""
See [here](https://discord.com/developers/docs/interactions/message-components)
for Discord's documentation.
"""
