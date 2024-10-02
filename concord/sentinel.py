import enum


class Sentinel(enum.Enum):
    NOT_GIVEN = object()


__all__ = ["Sentinel"]
