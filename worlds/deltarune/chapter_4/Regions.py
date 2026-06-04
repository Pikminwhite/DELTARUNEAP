from typing import TYPE_CHECKING

from BaseClasses import Region
from rule_builder.field_resolvers import FromOption
from rule_builder.options import OptionFilter
from rule_builder.rules import CanReachLocation, Has
from worlds.deltarune.Options import (
    MacGuffinChapter4,
    RandomizeSecretBosses,
)
from worlds.deltarune.Regions import Regions, add_location_to_region
from worlds.deltarune.chapter_4.Locations import chapter4_locations
from worlds.deltarune.Rules import have_kris_susie_or_ralsei, have_kris_or_susie
from worlds.deltarune.Items import items, ItemIDs, glitched_item_name
from worlds.deltarune.Locations import locations, LocationIDs

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

    # Require at least one character until you go for no-hit
    castle_town.connect(mike_room, "Mike Room Entrance", have_kris_susie_or_ralsei | Has(glitched_item_name))
    # Require at least one character for Guei fight
    castle_town.connect(dark_sanctuary, "Dark Sanctuary Entrance", have_kris_susie_or_ralsei)
    # If you get the claimbclaws, you can recreate a save to skip Dark Sanctuary but require Kris or Susie for Wingblade fight
    castle_town.connect(
        second_sanctuary,
        "Second Sanctuary Early Entrance",
        Has(items[ItemIDs.claimbclaws]) & have_kris_or_susie & Has(glitched_item_name),
    )
    # If you can go to the Second Sanctuary with the previous rule, then you can Wrong Warp to skip Second Sanctuary
    castle_town.connect(
        third_sanctuary,
        "Third Sanctuary Early Entrance (Skipping Second Sanctuary)",
        Has(items[ItemIDs.claimbclaws]) & Has(glitched_item_name),
    )

    dark_sanctuary.connect(dark_sanctuary_claimbclaws, "ClaimbClaws Required", Has(items[ItemIDs.claimbclaws]))
    # Require Kris or Susie for the Wingblade fight
    dark_sanctuary_claimbclaws.connect(
        second_sanctuary, "Second Sanctuary Entrance", Has(items[ItemIDs.sheetmusic]) & have_kris_or_susie
    )

    second_sanctuary.connect(third_sanctuary)

    secret_boss_mandatory = CanReachLocation(
        locations[LocationIDs.ch4_dark_sanctuary_hammer_of_justice_defeat_item_1]
    ) | [OptionFilter(RandomizeSecretBosses, RandomizeSecretBosses.option_mandatory, operator="ne")]

    # As you can access Third Sanctuary out of logic without any character, it's required for Titan
    third_sanctuary.connect(
        titan_fight,
        "Access to Chapter 4 Completion",
        secret_boss_mandatory
        & Has(items[ItemIDs.combination_lock_digit], FromOption(MacGuffinChapter4))
        & have_kris_susie_or_ralsei,
    )
    titan_fight.connect(light_world)
