from typing import TYPE_CHECKING
from BaseClasses import LocationProgressType
from rule_builder.rules import CanReachRegion, Has

from worlds.deltarune.Locations import locations, LocationIDs
from worlds.deltarune.Items import items, ItemIDs, glitched_item_name
from worlds.deltarune.Regions import Regions
from worlds.deltarune.Rules import can_recruit, have_kris_susie_or_ralsei

if TYPE_CHECKING:
    from .. import DeltaruneWorld


def set_rules(world: "DeltaruneWorld"):
    if world.is_all_recruits():
        world.set_rule(world.get_location(locations[LocationIDs.ch3_recruit_shadowguy]), can_recruit)
        world.set_rule(world.get_location(locations[LocationIDs.ch3_recruit_pippins]), can_recruit)
        world.set_rule(world.get_location(locations[LocationIDs.ch3_recruit_shuttah]), can_recruit)
        world.set_rule(world.get_location(locations[LocationIDs.ch3_recruit_water_cooler]), can_recruit)
        world.set_rule(world.get_location(locations[LocationIDs.ch3_recruit_zapper]), can_recruit)
        world.set_rule(world.get_location(locations[LocationIDs.ch3_recruit_shadowguy]), can_recruit)

    if world.is_weird_route() and not world.is_all_routes():
        world.set_rule(world.get_location(locations[LocationIDs.ch3_lost_shadowguy]), have_kris_susie_or_ralsei)
        world.set_rule(world.get_location(locations[LocationIDs.ch3_lost_pippins]), have_kris_susie_or_ralsei)
        world.set_rule(world.get_location(locations[LocationIDs.ch3_lost_shuttah]), have_kris_susie_or_ralsei)
        world.set_rule(world.get_location(locations[LocationIDs.ch3_lost_water_cooler]), have_kris_susie_or_ralsei)
        world.set_rule(world.get_location(locations[LocationIDs.ch3_lost_zapper]), have_kris_susie_or_ralsei)
        world.set_rule(world.get_location(locations[LocationIDs.ch3_lost_shadowguy]), have_kris_susie_or_ralsei)

    if world.is_all_routes():
        world.set_rule(
            world.get_location(locations[LocationIDs.ch3_lost_shadowguy]),
            have_kris_susie_or_ralsei & (CanReachRegion(Regions.ch3_tv_world) | Has(glitched_item_name)),
        )
        world.set_rule(
            world.get_location(locations[LocationIDs.ch3_lost_pippins]),
            have_kris_susie_or_ralsei & (CanReachRegion(Regions.ch3_tv_world) | Has(glitched_item_name)),
        )
        world.set_rule(
            world.get_location(locations[LocationIDs.ch3_lost_shuttah]),
            have_kris_susie_or_ralsei & (CanReachRegion(Regions.ch3_tv_world) | Has(glitched_item_name)),
        )
        world.set_rule(
            world.get_location(locations[LocationIDs.ch3_lost_water_cooler]),
            have_kris_susie_or_ralsei & (CanReachRegion(Regions.ch3_tv_world) | Has(glitched_item_name)),
        )
        world.set_rule(
            world.get_location(locations[LocationIDs.ch3_lost_zapper]),
            have_kris_susie_or_ralsei & (CanReachRegion(Regions.ch3_tv_world) | Has(glitched_item_name)),
        )
        world.set_rule(
            world.get_location(locations[LocationIDs.ch3_lost_shadowguy]),
            have_kris_susie_or_ralsei & (CanReachRegion(Regions.ch3_tv_world) | Has(glitched_item_name)),
        )

    if world.is_not_weird_route_only():
        world.set_rule(world.get_location(locations[LocationIDs.ch3_tv_world_man]), Has(items[ItemIDs.tripticket]))

    if world.is_t_rank_excluded():
        world.get_location(locations[LocationIDs.ch3_board_1_t_rank]).progress_type = LocationProgressType.EXCLUDED
        world.get_location(locations[LocationIDs.ch3_board_2_t_rank]).progress_type = LocationProgressType.EXCLUDED

    if world.is_t_rank_excluded():
        world.get_location(locations[LocationIDs.ch3_board_1_z_rank]).progress_type = LocationProgressType.EXCLUDED
        world.get_location(locations[LocationIDs.ch3_board_2_z_rank]).progress_type = LocationProgressType.EXCLUDED

def handle_locked_items(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld

    # MANTLE
    if not (world.is_mantle_randomized() or world.is_mantleless()):
        if world.is_shadow_mantle_included():
            multiworld.get_location(locations[LocationIDs.ch3_mantle_defeat], player).place_locked_item(
                world.create_item(items[ItemIDs.shadowmantle])
            )
        multiworld.get_location(locations[LocationIDs.ch3_s_rank_room_susie_gift], player).place_locked_item(
            world.create_item(items[ItemIDs.flatsoda])
        )
        multiworld.get_location(locations[LocationIDs.ch3_mantle_out_of_bounds_chest], player).place_locked_item(
            world.create_item(items[ItemIDs.ice_key])
        )
        multiworld.get_location(locations[LocationIDs.ch3_mantle_northern_light_item], player).place_locked_item(
            world.create_item(items[ItemIDs.shelter_key])
        )
        multiworld.get_location(locations[LocationIDs.ch3_s_rank_room_oddcontroller], player).place_locked_item(
            world.create_item(items[ItemIDs.odd_controller])
        )

    # Secret Bosses
    if not world.is_secret_bosses_randomized():
        multiworld.get_location(locations[LocationIDs.ch3_cold_place_knight_defeat_item_1], player).place_locked_item(
            world.create_item(items[ItemIDs.blackshard])
        )
        multiworld.get_location(locations[LocationIDs.ch3_cold_place_knight_defeat_item_2], player).place_locked_item(
            world.create_item(items[ItemIDs.shadowcrystal])
        )

    # Hidden items
    if not world.is_hidden_items_randomized():
        multiworld.get_location(locations[LocationIDs.ch3_board_2_moss], player).place_locked_item(
            world.create_item(items[ItemIDs.board_moss])
        )
        multiworld.get_location(locations[LocationIDs.ch3_b_rank_room_golden_prize_1], player).place_locked_item(
            world.create_item(items[ItemIDs.execbuffet])
        )
        multiworld.get_location(locations[LocationIDs.ch3_b_rank_room_golden_prize_2], player).place_locked_item(
            world.create_item(items[ItemIDs.tennatie])
        )
        multiworld.get_location(locations[LocationIDs.ch3_b_rank_room_golden_prize_3], player).place_locked_item(
            world.create_item(items[ItemIDs.tensionmax])
        )
        multiworld.get_location(locations[LocationIDs.ch3_b_rank_room_golden_prize_4], player).place_locked_item(
            world.create_item(items[ItemIDs.blue_ribbon])
        )
        multiworld.get_location(locations[LocationIDs.ch3_b_rank_room_golden_prize_5], player).place_locked_item(
            world.create_item(items[ItemIDs.revivemint])
        )
        # Location not available in weird route to avoid potential soft-lock due to Zapper Lost
        if world.is_not_weird_route_only():
            multiworld.get_location(locations[LocationIDs.ch3_tv_world_man], player).place_locked_item(
                world.create_item(items[ItemIDs.chapter_3_egg])
            )
            multiworld.get_location(locations[LocationIDs.ch3_tv_world_tripticket], player).place_locked_item(
                world.create_item(items[ItemIDs.tripticket])
            )
