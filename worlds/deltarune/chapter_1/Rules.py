from rule_builder.field_resolvers import FromOption
from rule_builder.options import OptionFilter
from rule_builder.rules import CanReachLocation, CanReachRegion, Has
from worlds.deltarune.Options import MacGuffinChapter1, RandomizeChapters, RandomizeSecretBosses
from worlds.generic.Rules import set_rule
from typing import TYPE_CHECKING
from .LocationsAndRegions import Ch1Entrances, Ch1Regions, Ch1Locations
from .Items import Ch1Items
from ..cross_chapter.LocationsAndRegions import CCEntrances
from ..cross_chapter.Items import CCItems
from ..Rules import have_kris_or_ralsei

if TYPE_CHECKING:
    from .. import DeltaruneWorld


def set_rules(world: "DeltaruneWorld"):
    world.set_rule(
        world.get_entrance(CCEntrances.chapter_1_entrance),
        Has(Ch1Items.chapter_1_unlock) | [OptionFilter(RandomizeChapters, RandomizeChapters.option_all_unlocked)],
    )

    world.set_rule(world.get_entrance(Ch1Entrances.fields_post_hathy_entrance), have_kris_or_ralsei)

    # Region blockers
    world.set_rule(world.get_entrance(Ch1Entrances.bake_sale_entrance), Has(Ch1Items.bake_sale_ticket))
    world.set_rule(world.get_entrance(Ch1Entrances.card_castle_entrance), Has(Ch1Items.castle_key))

    secret_boss_mandatory = CanReachLocation(Ch1Locations.card_castle_jevil_1) | [
        OptionFilter(RandomizeSecretBosses, RandomizeSecretBosses.option_mandatory, operator="ne")
    ]

    world.set_rule(
        world.get_entrance(Ch1Entrances.light_world_entrance),
        secret_boss_mandatory & Has(Ch1Items.king_shape_key_piece, FromOption(MacGuffinChapter1)),
    )

    # Jevil quest
    world.set_rule(
        world.get_location(Ch1Locations.bake_sale_repair_door_key),
        Has(Ch1Items.broken_key_a) & Has(Ch1Items.broken_key_b) & Has(Ch1Items.broken_key_c),
    )
    world.set_rule(world.get_location(Ch1Locations.card_castle_jevil_1), Has(Ch1Items.door_key))
    world.set_rule(world.get_location(Ch1Locations.card_castle_jevil_2), Has(Ch1Items.door_key))
    world.set_rule(world.get_location(Ch1Locations.card_castle_jevil_3), Has(Ch1Items.door_key))
    world.set_rule(
        world.get_location(Ch1Locations.seam_seap_talk_about_strange_prisoner), CanReachRegion(Ch1Regions.castle_town)
    )

    # Cake quest
    world.set_rule(world.get_location(Ch1Locations.bake_sale_repair_top_cake), Has(Ch1Items.brokencake))
    world.set_rule(world.get_location(Ch1Locations.field_return_top_cake), Has(Ch1Items.top_cake))

    # Manuals
    world.set_rule(world.get_location(Ch1Locations.throw_away_manual), Has(Ch1Items.manual))
    world.set_rule(world.get_location(Ch1Locations.throw_away_manual_again), Has(Ch1Items.manual, 2))

def handle_locked_items(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld

    if not world.is_secret_bosses_randomized():
        multiworld.get_location(Ch1Locations.card_castle_jevil_1, player).place_locked_item(
            world.create_item(Ch1Items.jevilstail)
        )
        multiworld.get_location(Ch1Locations.card_castle_jevil_2, player).place_locked_item(
            world.create_item(Ch1Items.devilsknife)
        )
        multiworld.get_location(Ch1Locations.card_castle_jevil_3, player).place_locked_item(
            world.create_item(CCItems.shadowcrystal)
        )

    # Hidden items
    if not world.is_hidden_items_randomized():
        multiworld.get_location(Ch1Locations.forest_man, player).place_locked_item(world.create_item(Ch1Items.egg))
        multiworld.get_location(Ch1Locations.card_castle_moss, player).place_locked_item(
            world.create_item(Ch1Items.castle_moss)
        )
        multiworld.get_location(Ch1Locations.seam_seap_talk_about_strange_prisoner, player).place_locked_item(
            world.create_item(Ch1Items.broken_key_a)
        )
        multiworld.get_location(Ch1Locations.forest_hidden_chest_near_dancers, player).place_locked_item(
            world.create_item(Ch1Items.broken_key_b)
        )
        multiworld.get_location(Ch1Locations.field_chest_before_great_board, player).place_locked_item(
            world.create_item(Ch1Items.broken_key_c)
        )
        multiworld.get_location(Ch1Locations.bake_sale_repair_door_key, player).place_locked_item(
            world.create_item(Ch1Items.door_key)
        )
