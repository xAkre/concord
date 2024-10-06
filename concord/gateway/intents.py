from __future__ import annotations

import typing

from .types.common import GatewayIntents

__all__ = ("Intents",)


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

        for intent in GatewayIntents:
            if bitmask_integer & intent:
                intents.append(intent)

        return cls(*intents)

    def add(self, *intents: GatewayIntents) -> None:
        """
        Add intents to the intents.

        :param intents: The intents to add.
        """
        self.intents = tuple(set((*self.intents, *intents)))

    def remove(self, *intents: GatewayIntents) -> None:
        """
        Remove intents from the intents.

        :param intents: The intents to remove.
        """
        self.intents = tuple(filter(lambda i: i not in intents, self.intents))

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
