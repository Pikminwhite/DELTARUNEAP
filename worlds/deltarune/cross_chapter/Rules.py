from rule_builder.options import OptionFilter
from rule_builder.rules import Has
from worlds.deltarune.Options import (
    IncludeChapter1,
    IncludeChapter2,
    IncludeChapter3,
    IncludeChapter4,
    RandomizeChapters,
    RemoveStartingEquipment,
)
from worlds.generic.Rules import set_rule

from typing import TYPE_CHECKING

from .Items import CCItems
from .LocationsAndRegions import CCLocations
from ..chapter_1.LocationsAndRegions import Ch1Locations
from ..chapter_1.Items import Ch1Items
from ..chapter_1.LocationsAndRegions import Ch1Locations
from ..chapter_2.Items import Ch2Items
from ..chapter_2.LocationsAndRegions import Ch2Locations
from ..chapter_3.Items import Ch3Items
from ..chapter_3.LocationsAndRegions import Ch3Locations
from ..chapter_4.Items import Ch4Items
from ..chapter_4.LocationsAndRegions import Ch4Locations
from ..chapter_5.Items import Ch5Items
from ..chapter_5.LocationsAndRegions import Ch5Locations
from ..Items import glitched_item_name

if TYPE_CHECKING:
    from .. import DeltaruneWorld


def set_rules(world: "DeltaruneWorld"):
    multiworld = world.multiworld
    player = world.player

    if world.can_access_fusion():
        # have_chapter2_equipment = [
        #     OptionFilter(RemoveStartingEquipment, RemoveStartingEquipment.option_false),
        #     OptionFilter(IncludeChapter2, IncludeChapter2.option_true),
        # ]

        # have_chapter2_equipment_in_order = (
        #     Has(
        #         glitched_item_name,
        #         options=[
        #             OptionFilter(RandomizeChapters, RandomizeChapters.option_in_order),
        #             OptionFilter(IncludeChapter1, IncludeChapter1.option_false),
        #         ],
        #         filtered_resolution=True,
        #     )
        #     & have_chapter2_equipment
        # )

        # have_white_ribbon = Has(CCItems.white_ribbon) | have_chapter2_equipment_in_order

        # if world.has_at_least_one_chapter_included([2, 3]) and (
        #     (world.is_starting_equipment_removed() and world.has_at_least_one_chapter_included([1, 3]))
        #     or (not world.is_starting_equipment_removed() and world.has_at_least_one_chapter_included([1, 2, 3]))
        # ):
        #     world.set_rule(
        #         world.get_location(CCLocations.castle_town_twin_ribbon_fusion),
        #         have_white_ribbon & Has(CCItems.pink_ribbon),
        #     )

        # have_chapter4_equipment = [
        #     OptionFilter(RemoveStartingEquipment, RemoveStartingEquipment.option_false),
        #     OptionFilter(IncludeChapter4, IncludeChapter4.option_true),
        # ]

        # have_chapter4_equipment_in_order = (
        #     Has(
        #         glitched_item_name,
        #         options=[
        #             OptionFilter(RandomizeChapters, RandomizeChapters.option_in_order),
        #             OptionFilter(IncludeChapter3, IncludeChapter3.option_false),
        #         ],
        #         filtered_resolution=True,
        #     )
        #     & have_chapter4_equipment
        # )

        # have_glowwrist = Has(Ch2Items.glowwrist) | have_chapter4_equipment

        # if world.include_chapter(1) and (
        #     world.include_chapter(2) or (not world.is_starting_equipment_removed() and world.include_chapter(4))
        # ):
        #     world.set_rule(
        #         world.get_location(CCLocations.castle_town_spike_band_fusion),
        #         have_glowwrist & Has(Ch1Items.ironshackle),
        #     )

        # TwinRibbon
        if world.is_starting_equipment_removed():
            if world.has_at_least_one_chapter_included([2, 3]) and world.has_at_least_one_chapter_included([1, 3]):
                # We have no ch2 starting equipment
                set_rule(
                    multiworld.get_location(CCLocations.castle_town_twin_ribbon_fusion, player),
                    lambda state: state.has(CCItems.pink_ribbon, player) and state.has(CCItems.white_ribbon, player),
                )
        else:
            if world.has_at_least_one_chapter_included([2, 3]) and world.has_at_least_one_chapter_included([1, 2, 3]):
                if world.include_chapter(1) and world.include_chapter(2) and world.is_chapters_in_order():
                    # We have ch2 starting equipment but we are playing in order so expected to load ch1 completion data (?)
                    set_rule(
                        multiworld.get_location(CCLocations.castle_town_twin_ribbon_fusion, player),
                        lambda state: state.has(CCItems.pink_ribbon, player)
                        and (state.has(CCItems.white_ribbon, player) or state.has(glitched_item_name, player)),
                    )
                else:
                    # We have ch2 starting equipment
                    set_rule(
                        multiworld.get_location(CCLocations.castle_town_twin_ribbon_fusion, player),
                        lambda state: state.has(CCItems.pink_ribbon, player),
                    )

        # SpikeBand
        if world.include_chapter(1):
            if (
                world.include_chapter(4) and not world.is_starting_equipment_removed()
            ):  # Chapter 4 have GlowWist have starter item so don't require it
                set_rule(
                    multiworld.get_location(CCLocations.castle_town_spike_band_fusion, player),
                    lambda state: state.has(Ch1Items.ironshackle, player),
                )
            elif world.include_chapter(2):  # Chapter 2 have to gain GlowWist so require it to acquire it
                set_rule(
                    multiworld.get_location(CCLocations.castle_town_spike_band_fusion, player),
                    lambda state: state.has(Ch1Items.ironshackle, player) and state.has(Ch2Items.glowwrist, player),
                )

        if world.include_chapter(2) and world.is_not_weird_route_only():
            world.set_rule(
                world.get_location(CCLocations.castle_town_tensionbow_fusion),
                Has(Ch2Items.bshotbowtie) & Has(Ch2Items.tensionbit),
            )

        # TwistedSwd
        if world.is_unused_items_included() and world.include_chapter(2) and world.is_weird_route():
            world.set_rule(
                world.get_location(CCLocations.castle_town_twistedsword_fusion),
                Has(Ch2Items.thornring) & Has(CCItems.purecrystal),
            )


def get_location(world: "DeltaruneWorld", chapter: int):
    if chapter == 1:
        return world.multiworld.get_location(Ch1Locations.fountain_sealed, world.player)
    if chapter == 2:
        return world.multiworld.get_location(Ch2Locations.fountain_sealed, world.player)
    if chapter == 3:
        return world.multiworld.get_location(Ch3Locations.fountain_sealed, world.player)
    if chapter == 4:
        return world.multiworld.get_location(Ch4Locations.third_sanctuary_fountain_sealed, world.player)


def get_unlock_item(world: "DeltaruneWorld", chapter: int):
    if chapter == 1:
        return Ch1Items.chapter_1_unlock
    if chapter == 2:
        return Ch2Items.chapter_2_unlock
    if chapter == 3:
        return Ch3Items.chapter_3_unlock
    if chapter == 4:
        return Ch4Items.chapter_4_unlock
    if chapter == 5:
        return Ch5Items.chapter_5_unlock


def handle_locked_items(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld

    if world.is_chapters_in_order():
        playable_chapters = world.get_playable_chapters()

        for current_chapter in playable_chapters:
            next_chapter = world.get_next_in_order_chapter(current_chapter)
            if next_chapter == -1:
                next_chapter = current_chapter + 1

            get_location(world, current_chapter).place_locked_item(
                world.create_item(get_unlock_item(world, next_chapter))
            )
