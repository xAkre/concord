import enum

__all__ = ("Sentinel",)


class Sentinel(enum.Enum):
    """Sentinel values for special meanings."""

    NOT_GIVEN = object()
