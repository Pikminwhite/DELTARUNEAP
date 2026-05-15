from rule_builder.field_resolvers import FromOption
from rule_builder.options import OptionFilter
from rule_builder.rules import Has
from worlds.deltarune.Options import MacGuffinChapter4, RandomizeChapters
from worlds.generic.Rules import set_rule
from BaseClasses import CollectionState
from typing import TYPE_CHECKING
from .LocationsAndRegions import Ch4Entrances, Ch4Regions, Ch4Locations
from .Items import Ch4Items
from ..cross_chapter.LocationsAndRegions import CCEntrances
from ..cross_chapter.Items import CCItems
from ..Items import glitched_item_name
from ..Rules import have_kris_susie_or_ralsei, have_kris_or_susie, have_susie

if TYPE_CHECKING:
    from .. import DeltaruneWorld


def set_rules(world: "DeltaruneWorld"):
    world.set_rule(
        world.get_entrance(CCEntrances.chapter_4_entrance),
        Has(Ch4Items.chapter_4_unlock) | [OptionFilter(RandomizeChapters, RandomizeChapters.option_all_unlocked)],
    )

    # Character requirement
    world.set_rule(world.get_entrance(Ch4Entrances.dark_sanctuary_entrance), have_kris_susie_or_ralsei)
    world.set_rule(
        world.get_entrance(Ch4Entrances.third_sanctuary_entrance), have_kris_or_susie | Has(glitched_item_name)
    )
    world.set_rule(
        world.get_location(Ch4Locations.dark_sanctuary_hammer_of_justice_defeat_item_1),
        have_susie | Has(glitched_item_name),
    )
    world.set_rule(
        world.get_location(Ch4Locations.dark_sanctuary_hammer_of_justice_defeat_item_2),
        have_susie | Has(glitched_item_name),
    )

    # Region blockers
    world.set_rule(world.get_entrance(Ch4Entrances.dark_sanctuary_claimbclaws_entrance), Has(Ch4Items.claimbclaws))
    world.set_rule(
        world.get_entrance(Ch4Entrances.second_sanctuary_entrance), have_kris_or_susie & Has(Ch4Items.sheetmusic)
    )
    world.set_rule(
        world.get_entrance(Ch4Entrances.titan_fight_entrance),
        Has(Ch4Items.combination_lock_digit, FromOption(MacGuffinChapter4)),
    )


def handle_locked_items(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld

    if not world.is_secret_bosses_randomized():
        multiworld.get_location(Ch4Locations.dark_sanctuary_hammer_of_justice_defeat_item_1, player).place_locked_item(
            world.create_item(Ch4Items.justiceaxe)
        )
        multiworld.get_location(Ch4Locations.dark_sanctuary_hammer_of_justice_defeat_item_2, player).place_locked_item(
            world.create_item(CCItems.shadowcrystal)
        )

    # Hidden Items
    if not world.is_hidden_items_randomized():
        multiworld.get_location(Ch4Locations.second_sanctuary_man, player).place_locked_item(
            world.create_item(Ch4Items.egg)
        )
        multiworld.get_location(Ch4Locations.second_sanctuary_moss, player).place_locked_item(
            world.create_item(Ch4Items.holy_moss)
        )
