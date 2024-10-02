import typing

from concord.types import Snowflake


class AvatarDecorationData(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/user#avatar-decoration-data-object)
    for Discord's documentation
    """

    asset: str
    sku_id: Snowflake


class User(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/user#user-object)
    for Discord's documentation
    """

    id: Snowflake
    username: str
    discriminator: str
    global_name: str | None
    avatar: str | None
    bot: typing.NotRequired[bool]
    system: typing.NotRequired[bool]
    mfa_enabled: typing.NotRequired[bool]
    banner: typing.NotRequired[str | None]
    accent_color: typing.NotRequired[int | None]
    locale: typing.NotRequired[str]
    verified: typing.NotRequired[bool]
    email: typing.NotRequired[str | None]
    flags: typing.NotRequired[int]
    avatar_decoration_data: typing.NotRequired[AvatarDecorationData | None]
