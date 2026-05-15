from rule_builder.field_resolvers import FromOption
from rule_builder.options import OptionFilter
from rule_builder.rules import CanReachLocation, CanReachRegion, Has
from worlds.deltarune.Options import (
    IncludeShadowMantle,
    MacGuffinChapter3,
    RandomizeChapters,
    RandomizeMANTLE,
    RandomizeSecretBosses,
)
from worlds.generic.Rules import set_rule
from BaseClasses import CollectionState
from typing import TYPE_CHECKING
from .LocationsAndRegions import Ch3Entrances, Ch3Regions, Ch3Locations
from .Items import Ch3Items
from ..cross_chapter.LocationsAndRegions import CCEntrances
from ..cross_chapter.Items import CCItems
from ..Items import glitched_item_name
from ..Rules import have_kris_susie_or_ralsei, have_kris_susie_and_ralsei

if TYPE_CHECKING:
    from .. import DeltaruneWorld


def set_rules(world: "DeltaruneWorld"):
    world.set_rule(
        world.get_entrance(CCEntrances.chapter_3_entrance),
        Has(
            Ch3Items.chapter_3_unlock,
            options=[OptionFilter(RandomizeChapters, RandomizeChapters.option_all_unlocked, operator="ne")],
            filtered_resolution=True,
        ),
    )

    # Character requirement
    world.set_rule(world.get_entrance(Ch3Entrances.board_1_entrance), have_kris_susie_or_ralsei)
    world.set_rule(world.get_entrance(Ch3Entrances.doom_board_entrance), have_kris_susie_and_ralsei)

    # Region Blockers
    world.set_rule(world.get_entrance(Ch3Entrances.board_2_entrance), Has(Ch3Items.board_2_cartridge))
    world.set_rule(world.get_entrance(Ch3Entrances.tv_world_entrance), Has(Ch3Items.vip_pass))

    mantle_mandatory = CanReachLocation(
        Ch3Locations.mantle_defeat,
        options=[
            OptionFilter(RandomizeSecretBosses, RandomizeSecretBosses.option_mandatory),
            OptionFilter(RandomizeMANTLE, RandomizeMANTLE.option_mantleless, operator="ne"),
        ],
        filtered_resolution=True,
    )

    shadow_mantle = (
        Has(Ch3Items.shadowmantle)
        | [OptionFilter(IncludeShadowMantle, IncludeShadowMantle.option_false)]
        | Has(glitched_item_name)
    )

    world.set_rule(
        world.get_entrance(Ch3Entrances.cold_place_entrance),
        mantle_mandatory & shadow_mantle & Has(Ch3Items.remote_battery, FromOption(MacGuffinChapter3)),
    )

    if world.is_all_routes():
        # Special rules for lost in all routes
        world.set_rule(
            world.get_location(Ch3Locations.lost_shadowguy),
            CanReachRegion(Ch3Regions.tv_world) | Has(glitched_item_name),
        )
        world.set_rule(
            world.get_location(Ch3Locations.lost_pippins), CanReachRegion(Ch3Regions.tv_world) | Has(glitched_item_name)
        )
        world.set_rule(
            world.get_location(Ch3Locations.lost_shuttah), CanReachRegion(Ch3Regions.tv_world) | Has(glitched_item_name)
        )
        world.set_rule(
            world.get_location(Ch3Locations.lost_water_cooler),
            CanReachRegion(Ch3Regions.tv_world) | Has(glitched_item_name),
        )
        world.set_rule(
            world.get_location(Ch3Locations.lost_zapper), CanReachRegion(Ch3Regions.tv_world) | Has(glitched_item_name)
        )

    # ORIGINAL GAME
    world.set_rule(world.get_location(Ch3Locations.mantle_out_of_bounds_chest), Has(Ch3Items.odd_controller))
    world.set_rule(
        world.get_location(Ch3Locations.mantle_northern_light_item),
        CanReachLocation(Ch3Locations.mantle_out_of_bounds_chest) & Has(Ch3Items.ice_key),
    )
    if not world.is_mantleless():
        world.set_rule(
            world.get_location(Ch3Locations.mantle_defeat),
            CanReachLocation(Ch3Locations.mantle_northern_light_item) & Has(Ch3Items.shelter_key),
        )
        world.set_rule(
            world.get_location(Ch3Locations.s_rank_room_susie_gift),
            CanReachLocation(Ch3Locations.mantle_northern_light_item) & Has(Ch3Items.shelter_key),
        )

    if world.is_not_weird_route_only():
        world.set_rule(world.get_location(Ch3Locations.tv_world_man), Has(Ch3Items.tripticket))

def handle_locked_items(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld

    # MANTLE
    if not (world.is_mantle_randomized() or world.is_mantleless()):
        if world.is_shadow_mantle_included():
            multiworld.get_location(Ch3Locations.mantle_defeat, player).place_locked_item(
                world.create_item(Ch3Items.shadowmantle)
            )
        multiworld.get_location(Ch3Locations.s_rank_room_susie_gift, player).place_locked_item(
            world.create_item(Ch3Items.flatsoda)
        )
        multiworld.get_location(Ch3Locations.mantle_out_of_bounds_chest, player).place_locked_item(
            world.create_item(Ch3Items.ice_key)
        )
        multiworld.get_location(Ch3Locations.mantle_northern_light_item, player).place_locked_item(
            world.create_item(Ch3Items.shelter_key)
        )
        multiworld.get_location(Ch3Locations.s_rank_room_oddcontroller, player).place_locked_item(
            world.create_item(Ch3Items.odd_controller)
        )

    # Secret Bosses
    if not world.is_secret_bosses_randomized():
        multiworld.get_location(Ch3Locations.cold_place_knight_defeat_item_1, player).place_locked_item(
            world.create_item(Ch3Items.blackshard)
        )
        multiworld.get_location(Ch3Locations.cold_place_knight_defeat_item_2, player).place_locked_item(
            world.create_item(CCItems.shadowcrystal)
        )

    # Hidden items
    if not world.is_hidden_items_randomized():
        multiworld.get_location(Ch3Locations.board_2_moss, player).place_locked_item(
            world.create_item(Ch3Items.board_moss)
        )
        multiworld.get_location(Ch3Locations.b_rank_room_golden_prize_1, player).place_locked_item(
            world.create_item(CCItems.execbuffet)
        )
        multiworld.get_location(Ch3Locations.b_rank_room_golden_prize_2, player).place_locked_item(
            world.create_item(Ch3Items.tennatie)
        )
        multiworld.get_location(Ch3Locations.b_rank_room_golden_prize_3, player).place_locked_item(
            world.create_item(Ch3Items.tensionmax)
        )
        multiworld.get_location(Ch3Locations.b_rank_room_golden_prize_4, player).place_locked_item(
            world.create_item(Ch3Items.blue_ribbon)
        )
        multiworld.get_location(Ch3Locations.b_rank_room_golden_prize_5, player).place_locked_item(
            world.create_item(CCItems.revivemint)
        )
        # Location not available in weird route to avoid potential soft-lock due to Zapper Lost
        if world.is_not_weird_route_only():
            multiworld.get_location(Ch3Locations.tv_world_man, player).place_locked_item(
                world.create_item(Ch3Items.egg)
            )
            multiworld.get_location(Ch3Locations.tv_world_tripticket, player).place_locked_item(
                world.create_item(Ch3Items.tripticket)
            )
