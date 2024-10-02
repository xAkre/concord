from __future__ import annotations

import typing

from .enums import GatewayIntents


class Intents:
    """Utility class for handling Discord Gateway Intents."""

    def __init__(self, *intents: GatewayIntents) -> None:
        """
        Initialize an Intents instance.

        :param intents: The intents to initialize with.
        """
        self.intents = intents

    @classmethod
    def from_bitmask(cls, bitmask_integer: int) -> Intents:
        """
        Create an Intents instance from a bitmask integer.

        :param bitmask_integer: The bitmask integer to convert to an Intents instance.
        :return: An Intents instance.
        """
        intents = []
        index = 0  # To keep track of the bit position

        while bitmask_integer > 0:
            if bitmask_integer & 0x1:
                if 2**index in GatewayIntents:
                    intents.append(GatewayIntents(2**index))

            bitmask_integer >>= 1
            index += 1

        return cls(*intents)

    def add(self, intent: GatewayIntents) -> None:
        """
        Add an intent to the intents.

        :param intent: The intent to add.
        """
        self.intents = (*self.intents, intent)

    def __repr__(self) -> str:
        return f"Intents({', '.join(map(str, self.intents))})"

    def __int__(self) -> int:
        """Convert the intents to an integer."""
        return sum(self.intents)

    def __contains__(self, intent: GatewayIntents | int) -> bool:
        """Check whether an intent is enabled."""
        return intent in self.intents

    def __iter__(self) -> typing.Iterator[GatewayIntents]:
        """Iterate over the intents."""
        return iter(self.intents)


__all__ = ["Intents"]
