from typing import TYPE_CHECKING
from rule_builder.rules import CanReachRegion, Has
from worlds.deltarune.Items import ItemIDs, items
from worlds.deltarune.Locations import LocationIDs, locations
from worlds.deltarune.Regions import Regions

if TYPE_CHECKING:
    from .. import DeltaruneWorld


def set_rules(world: "DeltaruneWorld"):
    world.set_rule(
        world.get_location(locations[LocationIDs.ch1_bake_sale_repair_door_key]),
        Has(items[ItemIDs.broken_key_a]) & Has(items[ItemIDs.broken_key_b]) & Has(items[ItemIDs.broken_key_c]),
    )
    world.set_rule(
        world.get_location(locations[LocationIDs.ch1_seam_seap_talk_about_strange_prisoner]),
        CanReachRegion(Regions.ch1_card_castle),
    )

    # Cake quest
    world.set_rule(
        world.get_location(locations[LocationIDs.ch1_bake_sale_repair_top_cake]), Has(items[ItemIDs.brokencake])
    )
    world.set_rule(world.get_location(locations[LocationIDs.ch1_field_return_top_cake]), Has(items[ItemIDs.top_cake]))

    # Manuals
    world.set_rule(world.get_location(locations[LocationIDs.ch1_throw_away_manual]), Has(items[ItemIDs.manual]))
    world.set_rule(
        world.get_location(locations[LocationIDs.ch1_throw_away_manual_again]), Has(items[ItemIDs.manual], 2)
    )

def handle_locked_items(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld

    if not world.is_secret_bosses_randomized():
        multiworld.get_location(locations[LocationIDs.ch1_card_castle_jevil_1], player).place_locked_item(
            world.create_item(items[ItemIDs.jevilstail])
        )
        multiworld.get_location(locations[LocationIDs.ch1_card_castle_jevil_2], player).place_locked_item(
            world.create_item(items[ItemIDs.devilsknife])
        )
        multiworld.get_location(locations[LocationIDs.ch1_card_castle_jevil_3], player).place_locked_item(
            world.create_item(items[ItemIDs.shadowcrystal])
        )

    # Hidden items
    if not world.is_hidden_items_randomized():
        multiworld.get_location(locations[LocationIDs.ch1_forest_man], player).place_locked_item(
            world.create_item(items[ItemIDs.chapter_1_egg])
        )
        multiworld.get_location(locations[LocationIDs.ch1_card_castle_moss], player).place_locked_item(
            world.create_item(items[ItemIDs.castle_moss])
        )
        multiworld.get_location(
            locations[LocationIDs.ch1_seam_seap_talk_about_strange_prisoner], player
        ).place_locked_item(world.create_item(items[ItemIDs.broken_key_a]))

        multiworld.get_location(locations[LocationIDs.ch1_forest_hidden_chest_near_dancers], player).place_locked_item(
            world.create_item(items[ItemIDs.broken_key_b])
        )
        multiworld.get_location(locations[LocationIDs.ch1_field_chest_before_great_board], player).place_locked_item(
            world.create_item(items[ItemIDs.broken_key_c])
        )
        multiworld.get_location(locations[LocationIDs.ch1_bake_sale_repair_door_key], player).place_locked_item(
            world.create_item(items[ItemIDs.door_key])
        )
