from rule_builder.options import OptionFilter
from rule_builder.rules import Has

from worlds.generic.Rules import set_rule

from typing import TYPE_CHECKING

from worlds.deltarune.Locations import locations, LocationIDs
from worlds.deltarune.Items import glitched_item_name, items, ItemIDs
from worlds.deltarune.Rules import have_thornring

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
                    world.get_location(locations[LocationIDs.cc_castle_town_twin_ribbon_fusion]),
                    lambda state: state.has(items[ItemIDs.pink_ribbon], player)
                    and state.has(items[ItemIDs.white_ribbon], player),
                )
        else:
            if world.has_at_least_one_chapter_included([2, 3]) and world.has_at_least_one_chapter_included([1, 2, 3]):
                if world.include_chapter(1) and world.include_chapter(2) and world.is_chapters_in_order():
                    # We have ch2 starting equipment but we are playing in order so expected to load ch1 completion data (?)
                    set_rule(
                        world.get_location(locations[LocationIDs.cc_castle_town_twin_ribbon_fusion]),
                        lambda state: state.has(items[ItemIDs.pink_ribbon], player)
                        and (state.has(items[ItemIDs.white_ribbon], player) or state.has(glitched_item_name, player)),
                    )
                else:
                    # We have ch2 starting equipment
                    set_rule(
                        world.get_location(locations[LocationIDs.cc_castle_town_twin_ribbon_fusion]),
                        lambda state: state.has(items[ItemIDs.pink_ribbon], player),
                    )

        # SpikeBand
        if world.include_chapter(1):
            if (
                world.include_chapter(4) and not world.is_starting_equipment_removed()
            ):  # Chapter 4 have GlowWist have starter item so don't require it
                set_rule(
                    world.get_location(locations[LocationIDs.cc_castle_town_spike_band_fusion]),
                    lambda state: state.has(items[ItemIDs.ironshackle], player),
                )
            elif world.include_chapter(2):  # Chapter 2 have to gain GlowWist so require it to acquire it
                set_rule(
                    world.get_location(locations[LocationIDs.cc_castle_town_spike_band_fusion]),
                    lambda state: state.has(items[ItemIDs.ironshackle], player)
                    and state.has(items[ItemIDs.glowwrist], player),
                )

        if world.include_chapter(2) and world.is_not_weird_route_only():
            world.set_rule(
                world.get_location(locations[LocationIDs.cc_castle_town_tensionbow_fusion]),
                Has(items[ItemIDs.bshotbowtie], player) & Has(items[ItemIDs.tensionbit], player),
            )

        # TwistedSwd
        if world.is_unused_items_included() and world.include_chapter(2) and world.is_weird_route():
            world.set_rule(
                world.get_location(locations[LocationIDs.cc_castle_town_twistedsword_fusion]),
                have_thornring & Has(items[ItemIDs.purecrystal], player),
            )


def get_location(world: "DeltaruneWorld", chapter: int):
    if chapter == 1:
        return world.multiworld.get_location(locations[LocationIDs.ch1_fountain_sealed], world.player)
    if chapter == 2:
        return world.multiworld.get_location(locations[LocationIDs.ch2_fountain_sealed], world.player)
    if chapter == 3:
        return world.multiworld.get_location(locations[LocationIDs.ch3_fountain_sealed], world.player)
    if chapter == 4:
        return world.multiworld.get_location(locations[LocationIDs.ch4_third_sanctuary_fountain_sealed], world.player)


def get_unlock_item(world: "DeltaruneWorld", chapter: int):
    if chapter == 1:
        return items[ItemIDs.chapter_1_unlock]
    if chapter == 2:
        return items[ItemIDs.chapter_2_unlock]
    if chapter == 3:
        return items[ItemIDs.chapter_3_unlock]
    if chapter == 4:
        return items[ItemIDs.chapter_4_unlock]
    if chapter == 5:
        return items[ItemIDs.chapter_5_unlock]


def handle_locked_items(world: "DeltaruneWorld"):
    if world.is_chapters_in_order():
        playable_chapters = world.get_playable_chapters()

        for current_chapter in playable_chapters:
            next_chapter = world.get_next_in_order_chapter(current_chapter)
            if next_chapter == -1:
                continue

            get_location(world, current_chapter).place_locked_item(
                world.create_item(get_unlock_item(world, next_chapter))
            )
