import enum

__all__ = ("Sentinel",)


class Sentinel(enum.Enum):
    NOT_GIVEN = object()
