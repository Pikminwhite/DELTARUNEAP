from worlds.generic.Rules import set_rule
from BaseClasses import CollectionState
from typing import TYPE_CHECKING
from .LocationsAndRegions import Ch5Entrances, Ch5Regions, Ch5Locations
from .Items import Ch5Items
from ..cross_chapter.LocationsAndRegions import CCEntrances
from ..cross_chapter.Items import CCItems

if TYPE_CHECKING:
    from .. import DeltaruneWorld


def set_rules(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld

    # Chapter unlock
    if not world.is_all_chapters_unlocked():
        set_rule(
            multiworld.get_entrance(CCEntrances.chapter_5_entrance, player),
            lambda state: state.has(Ch5Items.chapter_5_unlock, player),
        )

    # Region lockers

    # Macguffin


def handle_locked_items(world: "DeltaruneWorld"):
    player = world.player
    multiworld = world.multiworld

    if not world.is_secret_bosses_randomized():
        return

    # Hidden Items
    if not world.is_hidden_items_randomized():
        return
