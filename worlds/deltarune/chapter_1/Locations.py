from enum import StrEnum

from worlds.deltarune.Locations import LocationData, LocationData, LocationGroups, LocationIDs
from worlds.deltarune.Regions import Regions

chapter1_locations = {
    Regions.ch1_castle_town: [
        LocationData(
            LocationIDs.ch1_unknown_hidden_item,
            Regions.ch1_castle_town,
            group=LocationGroups.chapter1,
        ),
        LocationData(LocationIDs.ch1_castle_town_manual, Regions.ch1_castle_town, group=LocationGroups.chapter1),
        LocationData(LocationIDs.ch1_throw_away_manual, Regions.ch1_castle_town, group=LocationGroups.chapter1),
        LocationData(
            LocationIDs.ch1_throw_away_manual_again,
            Regions.ch1_castle_town,
            group=LocationGroups.chapter1,
        ),
    ],
    Regions.ch1_fields: [
        LocationData(LocationIDs.ch1_field_dark_candy_tree_1, Regions.ch1_fields, group=LocationGroups.chapter1),
        LocationData(LocationIDs.ch1_field_dark_candy_tree_2, Regions.ch1_fields, group=LocationGroups.chapter1),
        LocationData(LocationIDs.ch1_field_dark_candy_tree_3, Regions.ch1_fields, group=LocationGroups.chapter1),
        LocationData(LocationIDs.ch1_field_dark_candy_tree_4, Regions.ch1_fields, group=LocationGroups.chapter1),
        LocationData(LocationIDs.ch1_field_brokencake, Regions.ch1_fields, group=LocationGroups.chapter1),
        LocationData(LocationIDs.ch1_field_return_top_cake, Regions.ch1_fields, group=LocationGroups.chapter1),
        LocationData(
            LocationIDs.ch1_field_maze_of_death_chest,
            Regions.ch1_fields,
            group=LocationGroups.chapter1,
        ),
    ],
    Regions.ch1_fields_post_hathy: [
        LocationData(
            LocationIDs.ch1_field_chest_before_great_board,
            Regions.ch1_fields_post_hathy,
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_field_warp_door,
            Regions.ch1_fields_post_hathy,
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_seam_seap_talk_about_strange_prisoner,
            Regions.ch1_fields_post_hathy,
            group=LocationGroups.chapter1,
        ),
        LocationData(LocationIDs.ch1_seam_seap_1, Regions.ch1_fields_post_hathy, group=LocationGroups.chapter1),
        LocationData(LocationIDs.ch1_seam_seap_2, Regions.ch1_fields_post_hathy, group=LocationGroups.chapter1),
        LocationData(LocationIDs.ch1_seam_seap_3, Regions.ch1_fields_post_hathy, group=LocationGroups.chapter1),
        LocationData(LocationIDs.ch1_seam_seap_4, Regions.ch1_fields_post_hathy, group=LocationGroups.chapter1),
        LocationData(
            LocationIDs.ch1_recruit_rudinn,
            Regions.ch1_fields_post_hathy,
            should_be_included=lambda world: world.is_chapter_1_recruit_system_enabled() and world.is_all_recruits(),
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_recruit_hathy,
            Regions.ch1_fields_post_hathy,
            should_be_included=lambda world: world.is_chapter_1_recruit_system_enabled() and world.is_all_recruits(),
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_recruit_jigsawry,
            Regions.ch1_fields_post_hathy,
            should_be_included=lambda world: world.is_chapter_1_recruit_system_enabled() and world.is_all_recruits(),
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_recruit_ponman,
            Regions.ch1_fields_post_hathy,
            should_be_included=lambda world: world.is_chapter_1_recruit_system_enabled() and world.is_all_recruits(),
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_lost_rudinn,
            Regions.ch1_fields_post_hathy,
            should_be_included=lambda world: world.is_chapter_1_recruit_system_enabled() and world.is_weird_route(),
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_lost_hathy,
            Regions.ch1_fields_post_hathy,
            should_be_included=lambda world: world.is_chapter_1_recruit_system_enabled() and world.is_weird_route(),
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_lost_jigsawry,
            Regions.ch1_fields_post_hathy,
            should_be_included=lambda world: world.is_chapter_1_recruit_system_enabled() and world.is_weird_route(),
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_lost_ponman,
            Regions.ch1_fields_post_hathy,
            should_be_included=lambda world: world.is_chapter_1_recruit_system_enabled() and world.is_weird_route(),
            group=LocationGroups.chapter1,
        ),
    ],
    Regions.ch1_forest: [
        LocationData(LocationIDs.ch1_forest_warp_door, Regions.ch1_forest, group=LocationGroups.chapter1),
        LocationData(LocationIDs.ch1_forest_coat_rack_chest, Regions.ch1_forest, group=LocationGroups.chapter1),
        LocationData(
            LocationIDs.ch1_forest_letter_block_chest,
            Regions.ch1_forest,
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_recruit_rabbick,
            Regions.ch1_forest,
            should_be_included=lambda world: world.is_chapter_1_recruit_system_enabled() and world.is_all_recruits(),
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_recruit_bloxer,
            Regions.ch1_forest,
            should_be_included=lambda world: world.is_chapter_1_recruit_system_enabled() and world.is_all_recruits(),
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_lost_rabbick,
            Regions.ch1_forest,
            should_be_included=lambda world: world.is_chapter_1_recruit_system_enabled() and world.is_weird_route(),
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_lost_bloxer,
            Regions.ch1_forest,
            should_be_included=lambda world: world.is_chapter_1_recruit_system_enabled() and world.is_weird_route(),
            group=LocationGroups.chapter1,
        ),
    ],
    Regions.ch1_bake_sale: [
        LocationData(LocationIDs.ch1_bake_sale_warp_door, Regions.ch1_bake_sale, group=LocationGroups.chapter1),
        LocationData(
            LocationIDs.ch1_bake_sale_repair_door_key,
            Regions.ch1_bake_sale,
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_bake_sale_repair_top_cake,
            Regions.ch1_bake_sale,
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_bake_sale_diamond_stand,
            Regions.ch1_bake_sale,
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_bake_sale_heart_stand,
            Regions.ch1_bake_sale,
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_bake_sale_spade_stand,
            Regions.ch1_bake_sale,
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_forest_scissor_dancers_chest,
            Regions.ch1_bake_sale,
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_forest_hidden_chest_near_dancers,
            Regions.ch1_bake_sale,
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_forest_chest_near_worm,
            Regions.ch1_bake_sale,
            group=LocationGroups.chapter1,
        ),
        LocationData(LocationIDs.ch1_forest_man, Regions.ch1_bake_sale, group=LocationGroups.chapter1),
    ],
    Regions.ch1_card_castle: [
        LocationData(
            LocationIDs.ch1_card_castle_warp_door,
            Regions.ch1_card_castle,
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_card_castle_ironshackle,
            Regions.ch1_card_castle,
            group=LocationGroups.chapter1,
        ),
        LocationData(LocationIDs.ch1_card_castle_moss, Regions.ch1_card_castle, group=LocationGroups.chapter1),
        LocationData(
            LocationIDs.ch1_card_castle_rudinn_gift,
            Regions.ch1_card_castle,
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_card_castle_2f_chest,
            Regions.ch1_card_castle,
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_card_castle_4f_chest,
            Regions.ch1_card_castle,
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_card_castle_jevil_1,
            Regions.ch1_card_castle,
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_card_castle_jevil_2,
            Regions.ch1_card_castle,
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_card_castle_jevil_3,
            Regions.ch1_card_castle,
            group=LocationGroups.chapter1,
        ),
        LocationData(LocationIDs.ch1_rouxls_shop_1, Regions.ch1_card_castle, group=LocationGroups.chapter1),
        LocationData(LocationIDs.ch1_rouxls_shop_2, Regions.ch1_card_castle, group=LocationGroups.chapter1),
        LocationData(LocationIDs.ch1_rouxls_shop_3, Regions.ch1_card_castle, group=LocationGroups.chapter1),
        LocationData(LocationIDs.ch1_rouxls_shop_4, Regions.ch1_card_castle, group=LocationGroups.chapter1),
        LocationData(
            LocationIDs.ch1_recruit_rudinn_ranger,
            Regions.ch1_card_castle,
            should_be_included=lambda world: world.is_chapter_1_recruit_system_enabled() and world.is_all_recruits(),
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_recruit_head_hathy,
            Regions.ch1_card_castle,
            should_be_included=lambda world: world.is_chapter_1_recruit_system_enabled() and world.is_all_recruits(),
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_lost_rudinn_ranger,
            Regions.ch1_card_castle,
            should_be_included=lambda world: world.is_chapter_1_recruit_system_enabled() and world.is_weird_route(),
            group=LocationGroups.chapter1,
        ),
        LocationData(
            LocationIDs.ch1_lost_head_hathy,
            Regions.ch1_card_castle,
            should_be_included=lambda world: world.is_chapter_1_recruit_system_enabled() and world.is_weird_route(),
            group=LocationGroups.chapter1,
        ),
    ],
    Regions.ch1_light_world: [
        LocationData(LocationIDs.ch1_fountain_sealed, Regions.ch1_light_world, group=LocationGroups.chapter1)
    ],
}
