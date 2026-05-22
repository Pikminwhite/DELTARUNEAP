from BaseClasses import Location
from typing import TYPE_CHECKING

from worlds.deltarune.Locations import LocationData, LocationGroups, LocationIDs
from worlds.deltarune.Regions import Regions

if TYPE_CHECKING:
    from .. import DeltaruneWorld

chapter4_locations = {
    Regions.ch4_castle_town: [
        LocationData(
            LocationIDs.ch4_castle_town_lanino_elnina_challenge,
            Regions.ch4_castle_town,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_castle_town_top_chef_gift,
            Regions.ch4_castle_town,
            group=LocationGroups.chapter4,
        ),
    ],
    Regions.ch4_mike_room: [
        LocationData(
            LocationIDs.ch4_castle_town_mike_defeat,
            Regions.ch4_mike_room,
            should_be_included=lambda world: world.is_mike_battle_included(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_mike_battat_bronze,
            Regions.ch4_mike_room,
            should_be_included=lambda world: world.is_mike_games_included(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_mike_battat_silver,
            Regions.ch4_mike_room,
            should_be_included=lambda world: world.is_mike_games_included(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_mike_battat_gold,
            Regions.ch4_mike_room,
            should_be_included=lambda world: world.is_mike_games_included(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_mike_battat_platinum,
            Regions.ch4_mike_room,
            should_be_included=lambda world: world.is_mike_games_included(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_mike_jongler_bronze,
            Regions.ch4_mike_room,
            should_be_included=lambda world: world.is_mike_games_included(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_mike_jongler_silver,
            Regions.ch4_mike_room,
            should_be_included=lambda world: world.is_mike_games_included(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_mike_jongler_gold,
            Regions.ch4_mike_room,
            should_be_included=lambda world: world.is_mike_games_included(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_mike_jongler_platinum,
            Regions.ch4_mike_room,
            should_be_included=lambda world: world.is_mike_games_included(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_mike_pluey_bronze,
            Regions.ch4_mike_room,
            should_be_included=lambda world: world.is_mike_games_included(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_mike_pluey_silver,
            Regions.ch4_mike_room,
            should_be_included=lambda world: world.is_mike_games_included(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_mike_pluey_gold,
            Regions.ch4_mike_room,
            should_be_included=lambda world: world.is_mike_games_included(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_mike_pluey_platinum,
            Regions.ch4_mike_room,
            should_be_included=lambda world: world.is_mike_games_included(),
            group=LocationGroups.chapter4,
        ),
    ],
    Regions.ch4_dark_sanctuary: [
        LocationData(
            LocationIDs.ch4_dark_sanctuary_jockington_prophecy_chest,
            Regions.ch4_dark_sanctuary,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_dark_sanctuary_chest_in_first_dark_area,
            Regions.ch4_dark_sanctuary,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_dark_sanctuary_library_chest_1,
            Regions.ch4_dark_sanctuary,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_dark_sanctuary_worship_room_chest,
            Regions.ch4_dark_sanctuary,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_dark_sanctuary_lantern_puzzle_chest,
            Regions.ch4_dark_sanctuary,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_dark_sanctuary_library_chest_2,
            Regions.ch4_dark_sanctuary,
            group=LocationGroups.chapter4,
        ),
        LocationData(LocationIDs.ch4_old_man_shop_1, Regions.ch4_dark_sanctuary, group=LocationGroups.chapter4),
        LocationData(LocationIDs.ch4_old_man_shop_2, Regions.ch4_dark_sanctuary, group=LocationGroups.chapter4),
        LocationData(LocationIDs.ch4_old_man_shop_3, Regions.ch4_dark_sanctuary, group=LocationGroups.chapter4),
        LocationData(LocationIDs.ch4_old_man_shop_4, Regions.ch4_dark_sanctuary, group=LocationGroups.chapter4),
        LocationData(
            LocationIDs.ch4_recruit_guei,
            Regions.ch4_dark_sanctuary,
            should_be_included=lambda world: world.is_all_recruits(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_recruit_balthizard,
            Regions.ch4_dark_sanctuary,
            should_be_included=lambda world: world.is_all_recruits(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_recruit_bibliox,
            Regions.ch4_dark_sanctuary,
            should_be_included=lambda world: world.is_all_recruits(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_recruit_mizzle,
            Regions.ch4_dark_sanctuary,
            should_be_included=lambda world: world.is_all_recruits(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_lost_guei,
            Regions.ch4_dark_sanctuary,
            should_be_included=lambda world: world.is_weird_route(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_lost_balthizard,
            Regions.ch4_dark_sanctuary,
            should_be_included=lambda world: world.is_weird_route(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_lost_bibliox,
            Regions.ch4_dark_sanctuary,
            should_be_included=lambda world: world.is_weird_route(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_lost_mizzle,
            Regions.ch4_dark_sanctuary,
            should_be_included=lambda world: world.is_weird_route(),
            group=LocationGroups.chapter4,
        ),
    ],
    Regions.ch4_dark_sanctuary_claimbclaws: [
        LocationData(
            LocationIDs.ch4_dark_sanctuary_jackenstein_gift,
            Regions.ch4_dark_sanctuary_claimbclaws,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_dark_sanctuary_climbing_tutorial_chest,
            Regions.ch4_dark_sanctuary_claimbclaws,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_dark_sanctuary_cuptain_pillar_chest,
            Regions.ch4_dark_sanctuary_claimbclaws,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_dark_sanctuary_sleeping_mizzle_chest,
            Regions.ch4_dark_sanctuary_claimbclaws,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_dark_sanctuary_hidden_climbing_chest,
            Regions.ch4_dark_sanctuary_claimbclaws,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_dark_sanctuary_sheetmusic,
            Regions.ch4_dark_sanctuary_claimbclaws,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_dark_sanctuary_hammer_of_justice_defeat_item_1,
            Regions.ch4_dark_sanctuary_claimbclaws,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_dark_sanctuary_hammer_of_justice_defeat_item_2,
            Regions.ch4_dark_sanctuary_claimbclaws,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_recruit_miss_mizzle,
            Regions.ch4_dark_sanctuary_claimbclaws,
            should_be_included=lambda world: world.is_all_recruits(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_lost_miss_mizzle,
            Regions.ch4_dark_sanctuary_claimbclaws,
            should_be_included=lambda world: world.is_weird_route(),
            group=LocationGroups.chapter4,
        ),
    ],
    Regions.ch4_second_sanctuary: [
        LocationData(
            LocationIDs.ch4_dark_sanctuary_fountain_sealed,
            Regions.ch4_second_sanctuary,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_second_sanctuary_wall_climbing_chest,
            Regions.ch4_second_sanctuary,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_second_sanctuary_waterfall_chest,
            Regions.ch4_second_sanctuary,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_second_sanctuary_man,
            Regions.ch4_second_sanctuary,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_second_sanctuary_moss,
            Regions.ch4_second_sanctuary,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_second_sanctuary_gallery_prophecy_chest,
            Regions.ch4_second_sanctuary,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_second_sanctuary_fountain_sealed,
            Regions.ch4_second_sanctuary,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_second_sanctuary_destroyed_piano_block_chest,
            Regions.ch4_second_sanctuary,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_recruit_wicabel,
            Regions.ch4_second_sanctuary,
            should_be_included=lambda world: world.is_all_recruits(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_recruit_winglade,
            Regions.ch4_second_sanctuary,
            should_be_included=lambda world: world.is_all_recruits(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_recruit_organikk,
            Regions.ch4_second_sanctuary,
            should_be_included=lambda world: world.is_all_recruits(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_lost_wicabel,
            Regions.ch4_second_sanctuary,
            should_be_included=lambda world: world.is_weird_route(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_lost_winglade,
            Regions.ch4_second_sanctuary,
            should_be_included=lambda world: world.is_weird_route(),
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_lost_organikk,
            Regions.ch4_second_sanctuary,
            should_be_included=lambda world: world.is_weird_route(),
            group=LocationGroups.chapter4,
        ),
    ],
    Regions.ch4_third_sanctuary: [
        LocationData(
            LocationIDs.ch4_dark_sanctuary_annoying_dog,
            Regions.ch4_third_sanctuary,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_third_sanctuary_speed_climbing_chest,
            Regions.ch4_third_sanctuary,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_third_sanctuary_dark_area_chest,
            Regions.ch4_third_sanctuary,
            group=LocationGroups.chapter4,
        ),
    ],
    Regions.ch4_titan_fight: [
        LocationData(
            LocationIDs.ch4_third_sanctuary_titan_defeat,
            Regions.ch4_titan_fight,
            group=LocationGroups.chapter4,
        ),
        LocationData(
            LocationIDs.ch4_third_sanctuary_fountain_sealed,
            Regions.ch4_titan_fight,
            group=LocationGroups.chapter4,
        ),
    ],
}
