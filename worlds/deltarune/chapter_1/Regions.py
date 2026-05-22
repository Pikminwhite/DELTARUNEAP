from typing import TYPE_CHECKING

from BaseClasses import Region
from rule_builder.field_resolvers import FromOption
from rule_builder.options import OptionFilter
from rule_builder.rules import CanReachLocation, Has
from worlds.deltarune.Items import ItemIDs, items
from worlds.deltarune.Options import MacGuffinChapter1, RandomizeSecretBosses
from worlds.deltarune.Regions import add_location_to_region, Regions
from worlds.deltarune.Rules import have_kris_or_ralsei
from worlds.deltarune.Locations import LocationIDs, locations
from worlds.deltarune.chapter_1.Locations import chapter1_locations

if TYPE_CHECKING:
    from worlds.deltarune import DeltaruneWorld


def create_regions(world: "DeltaruneWorld"):
    castle_town = Region(Regions.ch1_castle_town, world.player, world.multiworld)
    fields = Region(Regions.ch1_fields, world.player, world.multiworld)
    fields_post_hathy = Region(Regions.ch1_fields_post_hathy, world.player, world.multiworld)
    forest = Region(Regions.ch1_forest, world.player, world.multiworld)
    bake_sale = Region(Regions.ch1_bake_sale, world.player, world.multiworld)
    card_castle = Region(Regions.ch1_card_castle, world.player, world.multiworld)
    jevil = Region(Regions.ch1_jevil, world.player, world.multiworld)
    light_world = Region(Regions.ch1_light_world, world.player, world.multiworld)

    regions = [castle_town, fields, fields_post_hathy, forest, bake_sale, card_castle, jevil, light_world]

    for region in regions:
        if region.name in chapter1_locations:
            add_location_to_region(region, chapter1_locations[region.name], world)
        world.multiworld.regions.append(region)

    world.get_region(Regions.chapter_1).connect(castle_town)
    castle_town.connect(fields)
    fields.connect(fields_post_hathy, "Fields (Post-Hathy) Entrance", have_kris_or_ralsei)
    fields_post_hathy.connect(forest)
    forest.connect(bake_sale, "Bake Sale Entrance", Has(items[ItemIDs.bake_sale_ticket]))
    bake_sale.connect(card_castle, "Card Castle Entrance", Has(items[ItemIDs.castle_key]))

    secret_boss_mandatory = CanReachLocation(locations[LocationIDs.ch1_card_castle_jevil_1]) | OptionFilter(
        RandomizeSecretBosses, RandomizeSecretBosses.option_mandatory, operator="ne"
    )

    card_castle.connect(
        light_world,
        "Access to chapter 1 completion",
        secret_boss_mandatory & Has(items[ItemIDs.king_shape_key_piece], FromOption(MacGuffinChapter1)),
    )

    card_castle.connect(jevil, "Access to Jevil", Has(items[ItemIDs.door_key]))
