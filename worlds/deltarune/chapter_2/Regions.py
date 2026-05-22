from typing import TYPE_CHECKING

from BaseClasses import Region
from rule_builder.options import OptionFilter
from rule_builder.rules import CanReachLocation, Has
from worlds.deltarune.Options import ChosenRoute, RandomizeSecretBosses
from worlds.deltarune.Regions import Regions, add_location_to_region
from worlds.deltarune.chapter_2.Locations import chapter2_locations
from worlds.deltarune.Rules import have_actions, have_kris_or_susie, have_thornring
from worlds.deltarune.Items import items, ItemIDs, glitched_item_name
from worlds.deltarune.Locations import LocationIDs, locations

if TYPE_CHECKING:
    from worlds.deltarune import DeltaruneWorld


def create_regions(world: "DeltaruneWorld"):
    castle_town = Region(Regions.ch2_castle_town, world.player, world.multiworld)
    cyber_field = Region(Regions.ch2_cyber_field, world.player, world.multiworld)
    cyber_field_post_dj = Region(Regions.ch2_cyber_field_post_dj, world.player, world.multiworld)
    cyber_city = Region(Regions.ch2_cyber_city, world.player, world.multiworld)
    mansion_lobby = Region(Regions.ch2_mansion_lobby, world.player, world.multiworld)
    mansion = Region(Regions.ch2_mansion, world.player, world.multiworld)
    mansion_weird_route = Region(Regions.ch2_mansion_weird_route, world.player, world.multiworld)
    mansion_basement = Region(Regions.ch2_mansion_basement, world.player, world.multiworld)
    spamton_neo = Region(Regions.ch2_spamton_neo, world.player, world.multiworld)
    post_chapter_castle_town = Region(Regions.ch2_post_chapter_castle_town, world.player, world.multiworld)

    regions = [
        castle_town,
        cyber_field,
        cyber_field_post_dj,
        cyber_city,
        mansion_lobby,
        mansion,
        mansion_weird_route,
        mansion_basement,
        spamton_neo,
        post_chapter_castle_town,
    ]

    for region in regions:
        if region.name in chapter2_locations:
            add_location_to_region(region, chapter2_locations[region.name], world)
        world.multiworld.regions.append(region)

    world.get_region(Regions.chapter_2).connect(castle_town)
    world.get_region(Regions.chapter_2).connect(cyber_field, "Cyber Field Entrance", have_kris_or_susie)
    castle_town.connect(cyber_field)
    cyber_field.connect(cyber_field_post_dj, "Cyber Field (Post-DJ) Entrance", have_actions | Has(glitched_item_name))
    cyber_field_post_dj.connect(
        cyber_city, "Cyber City Entrance", Has(items[ItemIDs.safety_vest]) | Has(glitched_item_name)
    )
    cyber_city.connect(mansion_lobby)
    mansion_lobby.connect(mansion, "Mansion Entrance", Has(items[ItemIDs.mansion_reservation]))
    mansion.connect(mansion_basement, "Mansion Basement Entrance", Has(items[ItemIDs.keygen]))
    mansion_basement.connect(spamton_neo, "Spamton Neo Entrance", Has(items[ItemIDs.emptydisk]))
    mansion_lobby.connect(mansion_weird_route)

    secret_boss_mandatory = CanReachLocation(locations[LocationIDs.ch2_mansion_spamton_neo_defeat_item_1]) | [
        OptionFilter(RandomizeSecretBosses, RandomizeSecretBosses.option_mandatory, operator="ne")
    ]

    mansion.connect(
        post_chapter_castle_town,
        "Access to chapter 2 completion",
        secret_boss_mandatory & Has(items[ItemIDs.keygen_2_segment]),
    )

    mansion_weird_route.connect(
        post_chapter_castle_town,
        "Access to chapter 2 completion Weird Route",
        Has(items[ItemIDs.keygen_2_segment]),
    )

    mansion_lobby.connect(
        spamton_neo,
        "Spamton Neo Weird Route",
        OptionFilter(ChosenRoute, [ChosenRoute.option_all_routes, ChosenRoute.option_weird_route], operator="in")
        & have_thornring,
    )
