from typing import TYPE_CHECKING

from rule_builder.rules import Has

from worlds.deltarune.Locations import locations, LocationIDs
from worlds.deltarune.Items import items, ItemIDs, glitched_item_name
from worlds.deltarune.Rules import have_susie, have_kris_susie_or_ralsei

if TYPE_CHECKING:
    from .. import DeltaruneWorld


def set_rules(world: "DeltaruneWorld"):
    world.set_rule(
        world.get_location(locations[LocationIDs.ch4_dark_sanctuary_hammer_of_justice_defeat_item_1]),
        have_susie | Has(glitched_item_name),
    )
    world.set_rule(
        world.get_location(locations[LocationIDs.ch4_dark_sanctuary_hammer_of_justice_defeat_item_2]),
        have_susie | Has(glitched_item_name),
    )

    world.set_rule(
        world.get_location(locations[LocationIDs.ch4_third_sanctuary_annoying_dog]), Has(items[ItemIDs.sheetmusic])
    )

    world.set_rule(world.get_location(locations[LocationIDs.ch4_recruit_organikk]), have_kris_susie_or_ralsei)
    world.set_rule(world.get_location(locations[LocationIDs.ch4_recruit_wicabel]), have_kris_susie_or_ralsei)
    world.set_rule(world.get_location(locations[LocationIDs.ch4_recruit_winglade]), have_kris_susie_or_ralsei)
    world.set_rule(world.get_location(locations[LocationIDs.ch4_lost_organikk]), have_kris_susie_or_ralsei)
    world.set_rule(world.get_location(locations[LocationIDs.ch4_lost_wicabel]), have_kris_susie_or_ralsei)
    world.set_rule(world.get_location(locations[LocationIDs.ch4_lost_winglade]), have_kris_susie_or_ralsei)


def handle_locked_items(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld

    if not world.is_secret_bosses_randomized():
        multiworld.get_location(
            locations[LocationIDs.ch4_dark_sanctuary_hammer_of_justice_defeat_item_1], player
        ).place_locked_item(world.create_item(items[ItemIDs.justiceaxe]))
        multiworld.get_location(
            locations[LocationIDs.ch4_dark_sanctuary_hammer_of_justice_defeat_item_2], player
        ).place_locked_item(world.create_item(items[ItemIDs.shadowcrystal]))

    # Hidden Items
    if not world.is_hidden_items_randomized():
        multiworld.get_location(locations[LocationIDs.ch4_second_sanctuary_man], player).place_locked_item(
            world.create_item(items[ItemIDs.chapter_4_egg])
        )
        multiworld.get_location(locations[LocationIDs.ch4_second_sanctuary_moss], player).place_locked_item(
            world.create_item(items[ItemIDs.sacred_moss])
        )
