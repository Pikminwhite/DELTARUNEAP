from BaseClasses import CollectionState
from worlds.generic.Rules import set_rule
from typing import TYPE_CHECKING
from .LocationsAndRegions import Ch2Entrances, Ch2Regions, Ch2Locations
from .Items import Ch2Items
from ..cross_chapter.LocationsAndRegions import CCEntrances
from ..cross_chapter.Items import CCItems
from ..Items import glitched_item_name

if TYPE_CHECKING:
    from .. import DeltaruneWorld


def set_rules(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld

    if world.is_kris_unlockable():
        set_rule(
            multiworld.get_entrance(Ch2Entrances.cyber_field_entrance, player),
            lambda state: state.has(CCItems.kris, player) or state.has(CCItems.susie, player),
        )

    # Chapter unlock
    if not world.is_all_chapters_unlocked():
        set_rule(
            multiworld.get_entrance(CCEntrances.chapter_2_entrance, player),
            lambda state: state.has(Ch2Items.chapter_2_unlock, player),
        )

    if world.is_all_routes():
        set_all_routes_rules(world)
    elif world.is_weird_route():
        set_weird_route_rules(world)
    elif world.is_all_recruits() or world.is_neutral_route():
        set_all_recruits_rules(world)

    if world.is_all_recruits():
        set_rule(
            multiworld.get_entrance(Ch2Entrances.mansion_entrance, player),
            lambda state: state.has(Ch2Items.mansion_reservation, player),
        )
        set_rule(
            multiworld.get_location(Ch2Locations.mansion_basement_chest, player),
            lambda state: state.has(Ch2Items.keygen, player),
        )
        set_rule(
            multiworld.get_location(Ch2Locations.mansion_basement_mechanism, player),
            lambda state: state.has(Ch2Items.keygen, player),
        )

    # Region lockers
    set_rule(
        multiworld.get_entrance(Ch2Entrances.cyber_city_entrance, player),
        lambda state: state.has(Ch2Items.safety_vest, player) or state.has(glitched_item_name, player),
    )
    # Mansion have special logic, need either thornring or mansion reservation depending of the route


def set_weird_route_rules(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld

    if world.is_characters_unlockables():
        handle_cyber_city_weird_route_having_noelle(world)

    set_rule(
        multiworld.get_entrance(Ch2Entrances.mansion_entrance, player),
        lambda state: handle_thornring(world, state),
    )

    set_rule(
        multiworld.get_location(Ch2Locations.mansion_warp_door, player),
        lambda state: handle_thornring(world, state) or state.has(glitched_item_name, player),
    )

    set_rule(
        multiworld.get_entrance(Ch2Entrances.post_chapter_castle_town_entrance, player),
        lambda state: state.has(Ch2Items.keygen_2_segment, player, world.options.macguffin_chapter_2.value)
        and handle_thornring(world, state),
    )
    set_rule(
        multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_1, player),
        lambda state: state.has(Ch2Items.keygen_2_segment, player, world.options.macguffin_chapter_2.value)
        and handle_thornring(world, state),
    )
    set_rule(
        multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_2, player),
        lambda state: state.has(Ch2Items.keygen_2_segment, player, world.options.macguffin_chapter_2.value)
        and handle_thornring(world, state),
    )


def set_all_recruits_rules(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld

    set_rule(
        multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_1, player),
        lambda state: state.has(Ch2Items.emptydisk, player) and state.has(Ch2Items.keygen, player),
    )
    set_rule(
        multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_2, player),
        lambda state: state.has(Ch2Items.emptydisk, player) and state.has(Ch2Items.keygen, player),
    )
    set_rule(
        multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_3, player),
        lambda state: state.has(Ch2Items.emptydisk, player) and state.has(Ch2Items.keygen, player),
    )

    if world.is_secret_bosses_mandatory():
        set_rule(
            multiworld.get_entrance(Ch2Entrances.post_chapter_castle_town_entrance, player),
            lambda state: state.has(Ch2Items.keygen_2_segment, player, world.options.macguffin_chapter_2.value)
            and state.has(Ch2Items.emptydisk, player)
            and state.has(Ch2Items.keygen, player),
        )
    else:
        set_rule(
            multiworld.get_entrance(Ch2Entrances.post_chapter_castle_town_entrance, player),
            lambda state: state.has(Ch2Items.keygen_2_segment, player, world.options.macguffin_chapter_2.value),
        )


def set_all_routes_rules(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld

    if world.is_characters_unlockables():
        handle_cyber_city_weird_route_having_noelle(world)

    set_rule(
        multiworld.get_entrance(Ch2Entrances.mansion_entrance, player),
        lambda state: state.has(Ch2Items.mansion_reservation, player) or handle_thornring(world, state),
    )

    set_rule(
        multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_1, player),
        lambda state: state.has(Ch2Items.keygen_2_segment, player, world.options.macguffin_chapter_2.value)
        and (
            handle_thornring(world, state)
            or (state.has(Ch2Items.emptydisk, player) and state.has(Ch2Items.keygen, player))
        ),
    )
    set_rule(
        multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_2, player),
        lambda state: state.has(Ch2Items.keygen_2_segment, player, world.options.macguffin_chapter_2.value)
        and (
            handle_thornring(world, state)
            or (state.has(Ch2Items.emptydisk, player) and state.has(Ch2Items.keygen, player))
        ),
    )
    set_rule(
        multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_3, player),
        lambda state: lambda state: state.has(
            Ch2Items.keygen_2_segment, player, world.options.macguffin_chapter_2.value
        )
        and (
            handle_thornring(world, state)
            or (state.has(Ch2Items.emptydisk, player) and state.has(Ch2Items.keygen, player))
        ),
    )

    if world.is_secret_bosses_mandatory():
        set_rule(
            multiworld.get_entrance(Ch2Entrances.post_chapter_castle_town_entrance, player),
            lambda state: state.has(Ch2Items.keygen_2_segment, player, world.options.macguffin_chapter_2.value)
            and (
                handle_thornring(world, state)
                or (state.has(Ch2Items.emptydisk, player) and state.has(Ch2Items.keygen, player))
            ),
        )
    else:
        set_rule(
            multiworld.get_entrance(Ch2Entrances.post_chapter_castle_town_entrance, player),
            lambda state: state.has(Ch2Items.keygen_2_segment, player, world.options.macguffin_chapter_2.value),
        )


def handle_locked_items(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld

    if not world.is_secret_bosses_randomized():
        multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_1, player).place_locked_item(
            world.create_item(Ch2Items.puppetscarf)
        )
        multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_2, player).place_locked_item(
            world.create_item(CCItems.shadowcrystal)
        )
        if world.is_not_weird_route_only():
            multiworld.get_location(Ch2Locations.mansion_spamton_neo_defeat_item_3, player).place_locked_item(
                world.create_item(Ch2Items.dealmaker)
            )

    # if not world.is_warps_randomized():
    # if True:
    #       multiworld.get_location(Ch2Locations.cyber_field_warp_door, player).place_locked_item(world.create_item(Ch2Items.cyber_field_warp))
    #       multiworld.get_location(Ch2Locations.trash_zone_warp_door, player).place_locked_item(world.create_item(Ch2Items.trash_zone_warp))
    #       multiworld.get_location(Ch2Locations.mansion_warp_door, player).place_locked_item(world.create_item(Ch2Items.mansion_warp))

    # Hidden items
    if not world.is_hidden_items_randomized():
        if world.is_not_weird_route_only():
            multiworld.get_location(Ch2Locations.spamton_shop_1, player).place_locked_item(
                world.create_item(Ch2Items.keygen)
            )
            multiworld.get_location(Ch2Locations.mansion_basement_mechanism, player).place_locked_item(
                world.create_item(Ch2Items.emptydisk)
            )
            multiworld.get_location(Ch2Locations.cyber_city_man, player).place_locked_item(
                world.create_item(Ch2Items.egg)
            )
            multiworld.get_location(Ch2Locations.cyber_city_moss, player).place_locked_item(
                world.create_item(Ch2Items.city_moss)
            )
            multiworld.get_location(Ch2Locations.cyber_city_annoying_dog, player).place_locked_item(
                world.create_item(CCItems.dogdollard)
            )


def handle_thornring(world: "DeltaruneWorld", state: CollectionState):
    player = world.player

    if world.is_noelle_weapons_progressive():
        return state.has(CCItems.progressive_noelle_weapons, player, 2) and handle_having_noelle(world, state)
    else:
        return state.has(Ch2Items.thornring, player) and handle_having_noelle(world, state)


def handle_having_noelle(world: "DeltaruneWorld", state: CollectionState):
    player = world.player

    if world.is_characters_unlockables():
        return state.has(CCItems.noelle, player)
    else:
        return True


def handle_cyber_city_weird_route_having_noelle(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld

    set_rule(
        multiworld.get_location(Ch2Locations.lost_ambyulance, player),
        lambda state: state.has(CCItems.noelle, player) or state.has(glitched_item_name, player),
    )
    set_rule(
        multiworld.get_location(Ch2Locations.lost_poppup, player),
        lambda state: state.has(CCItems.noelle, player) or state.has(glitched_item_name, player),
    )
    set_rule(
        multiworld.get_location(Ch2Locations.lost_maus, player),
        lambda state: state.has(CCItems.noelle, player) or state.has(glitched_item_name, player),
    )


def handle_lose_mansion_recruit_all_routes(world: "DeltaruneWorld"):
    locations = [Ch2Locations.lost_werewerewire, Ch2Locations.lost_tasque_manager, Ch2Locations.lost_mauswheel]

    for location in locations:
        set_rule(
            world.multiworld.get_location(location, world.player),
            lambda state: handle_thornring(world, state) or state.has(glitched_item_name, world.player),
        )

    if world.options.include_lose_swatchling.value == 1:
        set_rule(
            world.multiworld.get_location(Ch2Locations.lost_swatchlings, world.player),
            lambda state: handle_thornring(world, state) or state.has(glitched_item_name, world.player),
        )
