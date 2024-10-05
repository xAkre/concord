import typing

__all__ = ("VoiceRegion",)


class VoiceRegion(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/voice#voice-region-object)
    for Discord's documentation.
    """

    id: str
    name: str
    optimal: bool
    deprecated: bool
    custom: bool
