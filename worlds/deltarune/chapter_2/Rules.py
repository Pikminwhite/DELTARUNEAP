from BaseClasses import LocationProgressType
from rule_builder.rules import Has

from typing import TYPE_CHECKING
from worlds.deltarune.Locations import locations, LocationIDs
from worlds.deltarune.Items import ItemIDs, items, glitched_item_name
from worlds.deltarune.Rules import have_kris_susie_or_ralsei, have_noelle, have_thornring, can_snowgrave

if TYPE_CHECKING:
    from .. import DeltaruneWorld


def set_rules(world: "DeltaruneWorld"):
    # Character requirement
    world.set_rule(
        world.get_location(locations[LocationIDs.ch2_castle_town_jigsaw_joe_challenge]), have_kris_susie_or_ralsei
    )
    world.set_rule(
        world.get_location(locations[LocationIDs.ch2_castle_town_clover_rematch_challenge]), have_kris_susie_or_ralsei
    )

    # Weird Route
    if world.is_weird_route():
        # Lost recruits
        world.set_rule(
            world.get_location(locations[LocationIDs.ch2_lost_ambyu_lance]),
            have_noelle | Has(glitched_item_name),
        )
        world.set_rule(
            world.get_location(locations[LocationIDs.ch2_lost_poppup]),
            have_noelle | Has(glitched_item_name),
        )
        world.set_rule(world.get_location(locations[LocationIDs.ch2_lost_maus]), have_noelle | Has(glitched_item_name))
        world.set_rule(
            world.get_location(locations[LocationIDs.ch2_lost_mauswheel]),
            can_snowgrave | Has(glitched_item_name),
        )
        world.set_rule(
            world.get_location(locations[LocationIDs.ch2_lost_tasque_manager]),
            can_snowgrave | Has(glitched_item_name),
        )
        world.set_rule(
            world.get_location(locations[LocationIDs.ch2_lost_werewerewire]),
            can_snowgrave | Has(glitched_item_name),
        )
        if world.options.include_lose_swatchling.value == 1:
            world.set_rule(
                world.get_location(locations[LocationIDs.ch2_lost_swatchlings]),
                can_snowgrave | Has(glitched_item_name),
            )

    if world.is_all_recruits():
        # Recruit recruits
        world.set_rule(
            world.get_location(locations[LocationIDs.ch2_recruit_mauswheel]),
            Has(items[ItemIDs.mansion_reservation]) | Has(glitched_item_name),
        )
        world.set_rule(
            world.get_location(locations[LocationIDs.ch2_recruit_tasque_manager]),
            Has(items[ItemIDs.mansion_reservation]) | Has(glitched_item_name),
        )
        world.set_rule(
            world.get_location(locations[LocationIDs.ch2_recruit_werewerewire]),
            Has(items[ItemIDs.mansion_reservation]) | Has(glitched_item_name),
        )
        world.set_rule(
            world.get_location(locations[LocationIDs.ch2_recruit_swatchling]),
            Has(items[ItemIDs.mansion_reservation]) | Has(glitched_item_name),
        )

        if world.options.exclude_post_chapter_2_locations.value == 1:
            world.get_location(locations[LocationIDs.ch2_castle_town_tasque_manager_says_challenge]).progress_type = (
                LocationProgressType.EXCLUDED
            )
            world.get_location(locations[LocationIDs.ch2_castle_town_all_stars_challenge]).progress_type = (
                LocationProgressType.EXCLUDED
            )


def handle_locked_items(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld

    if not world.is_secret_bosses_randomized():
        multiworld.get_location(locations[LocationIDs.ch2_mansion_spamton_neo_defeat_item_1], player).place_locked_item(
            world.create_item(items[ItemIDs.puppetscarf])
        )
        multiworld.get_location(locations[LocationIDs.ch2_mansion_spamton_neo_defeat_item_2], player).place_locked_item(
            world.create_item(items[ItemIDs.shadowcrystal])
        )
        if world.is_not_weird_route_only():
            multiworld.get_location(
                locations[LocationIDs.ch2_mansion_spamton_neo_defeat_item_3], player
            ).place_locked_item(world.create_item(items[ItemIDs.dealmaker]))

    # Hidden items
    if not world.is_hidden_items_randomized():
        if world.is_not_weird_route_only():
            multiworld.get_location(locations[LocationIDs.ch2_spamton_shop_1], player).place_locked_item(
                world.create_item(items[ItemIDs.keygen])
            )
            multiworld.get_location(locations[LocationIDs.ch2_mansion_basement_mechanism], player).place_locked_item(
                world.create_item(items[ItemIDs.emptydisk])
            )
            multiworld.get_location(locations[LocationIDs.ch2_cyber_city_man], player).place_locked_item(
                world.create_item(items[ItemIDs.chapter_2_egg])
            )
            multiworld.get_location(locations[LocationIDs.ch2_cyber_city_moss], player).place_locked_item(
                world.create_item(items[ItemIDs.city_moss])
            )
            multiworld.get_location(locations[LocationIDs.ch2_cyber_city_annoying_dog], player).place_locked_item(
                world.create_item(items[ItemIDs.dogdollar])
            )
