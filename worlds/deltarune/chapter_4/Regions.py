from typing import TYPE_CHECKING

from BaseClasses import Region
from rule_builder.field_resolvers import FromOption
from rule_builder.rules import Has
from worlds.deltarune.Options import (
    MacGuffinChapter4,
)
from worlds.deltarune.Regions import Regions, add_location_to_region
from worlds.deltarune.chapter_4.Locations import chapter4_locations
from worlds.deltarune.Rules import have_kris_susie_or_ralsei, have_kris_or_susie
from worlds.deltarune.Items import items, ItemIDs, glitched_item_name

if TYPE_CHECKING:
    from worlds.deltarune import DeltaruneWorld


def create_regions(world: "DeltaruneWorld"):
    castle_town = Region(Regions.ch4_castle_town, world.player, world.multiworld)
    mike_room = Region(Regions.ch4_mike_room, world.player, world.multiworld)
    dark_sanctuary = Region(Regions.ch4_dark_sanctuary, world.player, world.multiworld)
    dark_sanctuary_claimbclaws = Region(Regions.ch4_dark_sanctuary_claimbclaws, world.player, world.multiworld)
    second_sanctuary = Region(Regions.ch4_second_sanctuary, world.player, world.multiworld)
    third_sanctuary = Region(Regions.ch4_third_sanctuary, world.player, world.multiworld)
    titan_fight = Region(Regions.ch4_titan_fight, world.player, world.multiworld)
    light_world = Region(Regions.ch4_light_world, world.player, world.multiworld)

    regions = [
        castle_town,
        mike_room,
        dark_sanctuary,
        dark_sanctuary_claimbclaws,
        second_sanctuary,
        third_sanctuary,
        titan_fight,
        light_world,
    ]

    for region in regions:
        if region.name in chapter4_locations:
            add_location_to_region(region, chapter4_locations[region.name], world)
        world.multiworld.regions.append(region)

    world.get_region(Regions.chapter_4).connect(castle_town)
    castle_town.connect(mike_room, "Mike Room Entrance", have_kris_susie_or_ralsei | Has(glitched_item_name))
    castle_town.connect(
        second_sanctuary,
        "Second Sanctuary Early Entrance",
        Has(items[ItemIDs.claimbclaws]) & Has(glitched_item_name) & have_kris_or_susie,
    )
    castle_town.connect(
        third_sanctuary,
        "Third Sanctuary Early Entrance (Skipping Second Sanctuary)",
        Has(items[ItemIDs.claimbclaws]) & Has(glitched_item_name),
    )
    castle_town.connect(dark_sanctuary, "Dark Sanctuary Entrance", have_kris_susie_or_ralsei)
    dark_sanctuary.connect(dark_sanctuary_claimbclaws, "ClaimbClaws Required", Has(items[ItemIDs.claimbclaws]))
    dark_sanctuary_claimbclaws.connect(
        second_sanctuary, "Second Sanctuary Entrance", Has(items[ItemIDs.sheetmusic]) & have_kris_or_susie
    )
    second_sanctuary.connect(third_sanctuary)
    third_sanctuary.connect(
        titan_fight,
        "Access to Chapter 4 Completion",
        Has(items[ItemIDs.combination_lock_digit], FromOption(MacGuffinChapter4)) & have_kris_susie_or_ralsei,
    )
    titan_fight.connect(light_world)
