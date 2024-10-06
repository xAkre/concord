from __future__ import annotations

import enum
import typing

from ..common import Snowflake
from .channel import PartialChannel
from .guild import PartialGuild
from .user import User

__all__ = ("Webhook", "WebhookType")


class Webhook(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/webhook#webhook-resource)
    for Discord's documentation.
    """

    id: Snowflake
    type: WebhookType
    guild_id: typing.NotRequired[Snowflake | None]
    channel_id: Snowflake | None
    user: typing.NotRequired[User]
    name: str | None
    avatar: str | None
    token: typing.NotRequired[str]
    application_id: Snowflake | None
    source_guild: typing.NotRequired[PartialGuild]
    source_channel: typing.NotRequired[PartialChannel]
    url: typing.NotRequired[str]


class WebhookType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/webhook#webhook-object-webhook-types)
    for Discord's documentation.
    """

    INCOMING = 1
    CHANNEL_FOLLOW = 2
