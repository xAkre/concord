from __future__ import annotations

import collections.abc
import enum
import typing

from ..common import Iso8601Timestamp

__all__ = (
    "Poll",
    "PollCreate",
    "PollAnswer",
    "PollAnswerCreate",
    "PollLayoutType",
    "PollMediaObject",
    "PollResults",
    "PollAnswerCount",
)


class Poll(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/poll)
    for Discord's documentation.
    """

    question: PollMediaObject
    answers: collections.abc.Sequence[PollAnswer]
    expiry: typing.NotRequired[Iso8601Timestamp]
    allow_multiselect: typing.NotRequired[bool]
    layout_type: typing.NotRequired[PollLayoutType]
    results: typing.NotRequired[collections.abc.Sequence[PollAnswer]]


class PollCreate(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/poll#poll-create-request-object)
    for Discord's documentation.
    """

    question: PollMediaObject
    answers: collections.abc.Sequence[PollAnswerCreate]
    duration: typing.NotRequired[int]
    allow_multiselect: typing.NotRequired[bool]
    layout_type: typing.NotRequired[PollLayoutType]


class PollMediaObject(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/poll#poll-media-object-poll-media-object-structure)
    for Discord's documentation.
    """

    text: typing.NotRequired[str]
    emoji: typing.NotRequired[str]
    """ID or name of the emoji."""


class PollAnswer(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/poll#poll-answer-object)
    for Discord's documentation.
    """

    answer_id: int
    poll_media: PollMediaObject


class PollAnswerCreate(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/poll#poll-answer-object)
    for Discord's documentation.
    """

    poll_media: PollMediaObject


class PollLayoutType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/poll#layout-type)
    for Discord's documentation.
    """

    DEFAULT = 1


class PollResults(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/poll#poll-results-object)
    for Discord's documentation.
    """

    is_finalized: bool


class PollAnswerCount(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/poll#poll-results-object-poll-answer-count-object-structure)
    for Discord's documentation.
    """

    answer_id: int
    count: int
    me_voted: bool
