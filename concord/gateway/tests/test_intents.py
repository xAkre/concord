import typing

import pytest

from .. import intents


class TestIntents:
    """Test suite for the `Intents` class."""

    @pytest.mark.parametrize(
        "intents_list",
        [
            [intents.GatewayIntents.GUILDS],
            [intents.GatewayIntents.GUILDS, intents.GatewayIntents.GUILD_MEMBERS],
            [
                intents.GatewayIntents.GUILD_EXPRESSIONS,
                intents.GatewayIntents.GUILD_MESSAGE_POLLS,
                intents.GatewayIntents.GUILD_SCHEDULED_EVENTS,
            ],
            [
                intents.GatewayIntents.GUILDS,
                intents.GatewayIntents.GUILD_MEMBERS,
                intents.GatewayIntents.GUILD_MODERATION,
                intents.GatewayIntents.GUILD_EXPRESSIONS,
                intents.GatewayIntents.GUILD_INTEGRATIONS,
                intents.GatewayIntents.GUILD_WEBHOOKS,
                intents.GatewayIntents.GUILD_INVITES,
                intents.GatewayIntents.GUILD_VOICE_STATES,
                intents.GatewayIntents.GUILD_PRESENCES,
                intents.GatewayIntents.GUILD_MESSAGES,
                intents.GatewayIntents.GUILD_MESSAGE_REACTIONS,
                intents.GatewayIntents.GUILD_MESSAGE_TYPING,
                intents.GatewayIntents.DIRECT_MESSAGES,
                intents.GatewayIntents.DIRECT_MESSAGE_REACTIONS,
                intents.GatewayIntents.DIRECT_MESSAGE_TYPING,
                intents.GatewayIntents.MESSAGE_CONTENT,
                intents.GatewayIntents.GUILD_SCHEDULED_EVENTS,
                intents.GatewayIntents.AUTO_MODERATION_CONFIGURATION,
                intents.GatewayIntents.AUTO_MODERATION_EXECUTION,
                intents.GatewayIntents.GUILD_MESSAGE_POLLS,
                intents.GatewayIntents.DIRECT_MESSAGE_POLLS,
            ],
        ],
    )
    def test_should_parse_intents_from_bitmask(
        self, intents_list: typing.List[intents.GatewayIntents]
    ) -> None:
        """Test that the from_bitmask method correctly parses intents from a bitmask."""
        bit_mask = sum(intents_list)
        intents_instance = intents.Intents.from_bitmask(bit_mask)
        assert len(intents_instance.intents) == len(intents_list)
        assert all(intent in intents_instance.intents for intent in intents_list)
