from rule_builder.field_resolvers import FromOption
from rule_builder.options import OptionFilter
from rule_builder.rules import CanReachLocation, CanReachRegion, Has
from worlds.deltarune.Options import (
    ChosenRoute,
    MacGuffinChapter2,
    RandomizeChapters,
    RandomizeSecretBosses,
    UnlockFunGangActions,
)
from worlds.generic.Rules import set_rule
from typing import TYPE_CHECKING
from .LocationsAndRegions import Ch2Entrances, Ch2Regions, Ch2Locations
from .Items import Ch2Items
from ..cross_chapter.LocationsAndRegions import CCEntrances
from ..cross_chapter.Items import CCItems
from ..Items import glitched_item_name
from ..Rules import have_kris_or_susie, have_kris_susie_or_ralsei, have_noelle, have_actions

if TYPE_CHECKING:
    from .. import DeltaruneWorld


def set_rules(world: "DeltaruneWorld"):
    world.set_rule(
        world.get_entrance(CCEntrances.chapter_2_entrance),
        Has(Ch2Items.chapter_2_unlock) | [OptionFilter(RandomizeChapters, RandomizeChapters.option_all_unlocked)],
    )

    # Region Blockers
    world.set_rule(
        world.get_entrance(Ch2Entrances.cyber_city_entrance), Has(Ch2Items.safety_vest) | Has(glitched_item_name)
    )
    world.set_rule(
        Ch2Entrances.mansion_lobby_entrance,
        can_proceed_weird_route
        | (
            CanReachRegion(Ch2Regions.cyber_city)
            & [OptionFilter(ChosenRoute, ChosenRoute.option_weird_route, operator="ne")]
        )
        | Has(glitched_item_name),
    )
    world.set_rule(
        world.get_entrance(Ch2Entrances.mansion_entrance), can_proceed_weird_route | Has(Ch2Items.mansion_reservation)
    )

    secret_boss_mandatory = CanReachLocation(Ch2Locations.mansion_spamton_neo_defeat_item_1) | [
        OptionFilter(RandomizeSecretBosses, RandomizeSecretBosses.option_mandatory, operator="ne")
    ]

    world.set_rule(
        world.get_entrance(Ch2Entrances.post_chapter_castle_town_entrance),
        secret_boss_mandatory & Has(Ch2Items.keygen_2_segment, FromOption(MacGuffinChapter2)),
    )

    # Character requirement
    world.set_rule(world.get_entrance(Ch2Entrances.cyber_field_entrance), have_kris_or_susie)
    world.set_rule(world.get_location(Ch2Locations.castle_town_jigsaw_joe_challenge), have_kris_susie_or_ralsei)
    world.set_rule(world.get_location(Ch2Locations.castle_town_clover_rematch_challenge), have_kris_susie_or_ralsei)

    # Actions requirement
    world.set_rule(
        world.get_entrance(Ch2Entrances.cyber_field_post_dj_entrance),
        have_actions | Has(glitched_item_name),
    )

    if world.is_fun_gang_actions_unlockable():
        world.set_rule(world.get_location(Ch2Locations.cyber_field_fun_gang_actions_unlock), Has(CCItems.s_r_n_actions))

    # Spamton quest
    world.set_rule(
        world.get_entrance(Ch2Entrances.mansion_basement_entrance),
        Has(Ch2Items.keygen),
    )

    spamton_neo_weird_route = can_proceed_weird_route
    spamton_neo = Has(Ch2Items.mansion_reservation) & Has(Ch2Items.keygen) & Has(Ch2Items.emptydisk)

    world.set_rule(world.get_entrance(Ch2Entrances.spamton_neo_entrance), spamton_neo | spamton_neo_weird_route)

    # Weird Route
    if world.is_weird_route():
        # Lost recruits
        world.set_rule(
            world.get_location(Ch2Locations.lost_ambyulance), can_proceed_weird_route | Has(glitched_item_name)
        )
        world.set_rule(world.get_location(Ch2Locations.lost_poppup), can_proceed_weird_route | Has(glitched_item_name))
        world.set_rule(world.get_location(Ch2Locations.lost_maus), can_proceed_weird_route | Has(glitched_item_name))
        world.set_rule(
            world.get_location(Ch2Locations.lost_mauswheel), can_proceed_weird_route | Has(glitched_item_name)
        )
        world.set_rule(
            world.get_location(Ch2Locations.lost_tasque_manager), can_proceed_weird_route | Has(glitched_item_name)
        )
        world.set_rule(
            world.get_location(Ch2Locations.lost_werewerewire), can_proceed_weird_route | Has(glitched_item_name)
        )
        if world.options.include_lose_swatchling.value == 1:
            world.set_rule(
                world.get_location(Ch2Locations.lost_swatchlings), can_proceed_weird_route | Has(glitched_item_name)
            )

    if world.is_all_recruits():
        # Recruit recruits
        world.set_rule(
            world.get_location(Ch2Locations.recruit_mauswheel),
            Has(Ch2Items.mansion_reservation) | Has(glitched_item_name),
        )
        world.set_rule(
            world.get_location(Ch2Locations.recruit_tasque_manager),
            Has(Ch2Items.mansion_reservation) | Has(glitched_item_name),
        )
        world.set_rule(
            world.get_location(Ch2Locations.recruit_werewerewire),
            Has(Ch2Items.mansion_reservation) | Has(glitched_item_name),
        )
        world.set_rule(
            world.get_location(Ch2Locations.recruit_swatchling),
            Has(Ch2Items.mansion_reservation) | Has(glitched_item_name),
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

can_proceed_weird_route = (Has(Ch2Items.thornring) | Has(CCItems.progressive_noelle_weapons, 2)) & have_noelle
