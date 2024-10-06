import enum

__all__ = ("InteractionType",)


class InteractionType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/interactions/receiving-and-responding#interaction-object-interaction-type)
    for Discord's documentation.
    """

    PING = 1
    APPLICATION_COMMAND = 2
    MESSAGE_COMPONENT = 3
    APPLICATION_COMMAND_AUTOCOMPLETE = 4
    MODAL_SUBMIT = 5
