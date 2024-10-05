from __future__ import annotations

import enum
import typing

from ..common import LanguageCode

__all__ = (
    "ApplicationRoleConnectionMetadata",
    "ApplicationRoleConnectionMetadataType",
)


class ApplicationRoleConnectionMetadata(typing.TypedDict):
    """
    See [here](https://discord.com/developers/docs/resources/application-role-connection-metadata)
    for Discord's documentation.
    """

    type: ApplicationRoleConnectionMetadataType
    key: str
    name: str
    name_localizations: typing.Optional[typing.Mapping[LanguageCode, str]]
    description: str
    description_localizations: typing.Optional[typing.Mapping[LanguageCode, str]]


class ApplicationRoleConnectionMetadataType(enum.IntEnum):
    """
    See [here](https://discord.com/developers/docs/resources/application-role-connection-metadata#application-role-connection-metadata-object-application-role-connection-metadata-type)
    for Discord's documentation.
    """

    INTEGER_LESS_THAN_OR_EQUAL = 1
    INTEGER_GREATER_THAN_OR_EQUAL = 2
    INTEGER_EQUAL = 3
    INTEGER_NOT_EQUAL = 4
    DATETIME_LESS_THAN_OR_EQUAL = 5
    DATETIME_GREATER_THAN_OR_EQUAL = 6
    BOOLEAN_EQUAL = 7
    BOOLEAN_NOT_EQUAL = 8
