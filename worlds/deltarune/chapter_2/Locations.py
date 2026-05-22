from worlds.deltarune.Locations import LocationData, LocationGroups, LocationIDs
from worlds.deltarune.Regions import Regions
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .. import DeltaruneWorld

chapter2_locations = {
    Regions.ch2_castle_town: [
        LocationData(
            LocationIDs.ch2_castle_town_jigsaw_joe_challenge,
            Regions.ch2_castle_town,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_castle_town_graze_challenge_1,
            Regions.ch2_castle_town,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_castle_town_clover_rematch_challenge,
            Regions.ch2_castle_town,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_castle_town_top_chef_gift,
            Regions.ch2_castle_town,
            group=LocationGroups.chapter2,
        ),
    ],
    Regions.ch2_cyber_field: [
        LocationData(
            LocationIDs.ch2_cyber_field_first_chest,
            Regions.ch2_cyber_field,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_field_nubert_chest,
            Regions.ch2_cyber_field,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_field_tasque_maze_checkmark,
            Regions.ch2_cyber_field,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_field_teacup_ride_checkmark,
            Regions.ch2_cyber_field,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_field_giasfelfebrehber_checkmark,
            Regions.ch2_cyber_field,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_field_warp_door,
            Regions.ch2_cyber_field,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_recruit_werewire,
            Regions.ch2_cyber_field,
            should_be_included=lambda world: world.is_all_recruits(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_recruit_tasque,
            Regions.ch2_cyber_field,
            should_be_included=lambda world: world.is_all_recruits(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_recruit_virovirokun,
            Regions.ch2_cyber_field,
            should_be_included=lambda world: world.is_all_recruits(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_lost_werewire,
            Regions.ch2_cyber_field,
            should_be_included=lambda world: world.is_weird_route(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_lost_tasque,
            Regions.ch2_cyber_field,
            should_be_included=lambda world: world.is_weird_route(),
            group=LocationGroups.chapter2,
        ),
    ],
    Regions.ch2_cyber_field_post_dj: [
        LocationData(
            LocationIDs.ch2_cyber_field_fun_gang_actions_unlock,
            Regions.ch2_cyber_field,
            should_be_included=lambda world: world.is_fun_gang_actions_unlockable(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_field_chest_near_music_shop,
            Regions.ch2_cyber_field_post_dj,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_field_virovirokun_puzzle_chest,
            Regions.ch2_cyber_field_post_dj,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_field_teacup_puzzle_chest,
            Regions.ch2_cyber_field_post_dj,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_music_shop_1,
            Regions.ch2_cyber_field_post_dj,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_music_shop_2,
            Regions.ch2_cyber_field_post_dj,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_music_shop_3,
            Regions.ch2_cyber_field_post_dj,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_music_shop_4,
            Regions.ch2_cyber_field_post_dj,
            group=LocationGroups.chapter2,
        ),
    ],
    Regions.ch2_cyber_city: [
        LocationData(
            LocationIDs.ch2_trash_zone_trash_can,
            Regions.ch2_cyber_city,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_city_trash_can_1,
            Regions.ch2_cyber_city,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_city_trash_can_2,
            Regions.ch2_cyber_city,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_city_queen_poster_chest,
            Regions.ch2_cyber_city,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_city_chest_guarded_by_virovirokun,
            Regions.ch2_cyber_city,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_city_cheese_maze_chest,
            Regions.ch2_cyber_city,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_city_trash_can_3,
            Regions.ch2_cyber_city,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_city_trash_can_4,
            Regions.ch2_cyber_city,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_city_trash_can_5,
            Regions.ch2_cyber_city,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_trash_zone_warp_door,
            Regions.ch2_cyber_city,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_recruit_poppup,
            Regions.ch2_cyber_city,
            should_be_included=lambda world: world.is_all_recruits(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_recruit_ambyu_lance,
            Regions.ch2_cyber_city,
            should_be_included=lambda world: world.is_all_recruits(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_city_purchase_mannequin,
            Regions.ch2_cyber_city,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_city_annoying_dog,
            Regions.ch2_cyber_city,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_city_man,
            Regions.ch2_cyber_city,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_city_moss,
            Regions.ch2_cyber_city,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_city_purchase_kris_tea,
            Regions.ch2_cyber_city,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_city_purchase_noelle_tea,
            Regions.ch2_cyber_city,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_city_purchase_susie_tea,
            Regions.ch2_cyber_city,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_city_purchase_ralsei_tea,
            Regions.ch2_cyber_city,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_recruit_maus,
            Regions.ch2_cyber_city,
            should_be_included=lambda world: world.is_all_recruits(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_spamton_shop_1,
            Regions.ch2_cyber_city,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_spamton_shop_2,
            Regions.ch2_cyber_city,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_spamton_shop_3,
            Regions.ch2_cyber_city,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_spamton_shop_4,
            Regions.ch2_cyber_city,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_lost_virovirokun,
            Regions.ch2_cyber_field,
            should_be_included=lambda world: world.is_weird_route(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_lost_poppup,
            Regions.ch2_cyber_city,
            should_be_included=lambda world: world.is_weird_route(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_lost_ambyu_lance,
            Regions.ch2_cyber_city,
            should_be_included=lambda world: world.is_weird_route(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_city_purchase_freezering,
            Regions.ch2_cyber_city,
            should_be_included=lambda world: world.is_weird_route(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_lost_maus,
            Regions.ch2_cyber_city,
            should_be_included=lambda world: world.is_weird_route(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_cyber_city_purchase_thornring,
            Regions.ch2_cyber_city,
            should_be_included=lambda world: world.is_weird_route(),
            group=LocationGroups.chapter2,
        ),
    ],
    Regions.ch2_mansion_lobby: [
        LocationData(
            LocationIDs.ch2_mansion_warp_door,
            Regions.ch2_mansion_lobby,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_swatchs_cafe_1,
            Regions.ch2_mansion_lobby,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_swatchs_cafe_2,
            Regions.ch2_mansion_lobby,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_swatchs_cafe_3,
            Regions.ch2_mansion_lobby,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_swatchs_cafe_4,
            Regions.ch2_mansion_lobby,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
    ],
    Regions.ch2_mansion: [
        LocationData(
            LocationIDs.ch2_mansion_painting_chest,
            Regions.ch2_mansion,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_mansion_sculpture_room_chest,
            Regions.ch2_mansion,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_mansion_platter_chest,
            Regions.ch2_mansion,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_mansion_tunnel_of_love_chest,
            Regions.ch2_mansion,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_recruit_swatchling,
            Regions.ch2_mansion,
            should_be_included=lambda world: world.is_all_recruits(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_recruit_tasque_manager,
            Regions.ch2_mansion,
            should_be_included=lambda world: world.is_all_recruits(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_recruit_mauswheel,
            Regions.ch2_mansion,
            should_be_included=lambda world: world.is_all_recruits(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_recruit_werewerewire,
            Regions.ch2_mansion,
            should_be_included=lambda world: world.is_all_recruits(),
            group=LocationGroups.chapter2,
        ),
    ],
    Regions.ch2_mansion_weird_route: [
        LocationData(
            LocationIDs.ch2_lost_swatchlings,
            Regions.ch2_mansion_weird_route,
            should_be_included=lambda world: world.is_weird_route()
            and world.options.include_lose_swatchling.value == 1,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_lost_tasque_manager,
            Regions.ch2_mansion_weird_route,
            should_be_included=lambda world: world.is_weird_route(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_lost_mauswheel,
            Regions.ch2_mansion_weird_route,
            should_be_included=lambda world: world.is_weird_route(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_lost_werewerewire,
            Regions.ch2_mansion_weird_route,
            should_be_included=lambda world: world.is_weird_route(),
            group=LocationGroups.chapter2,
        ),
    ],
    Regions.ch2_mansion_basement: [
        LocationData(
            LocationIDs.ch2_mansion_basement_chest,
            Regions.ch2_mansion_basement,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_mansion_basement_mechanism,
            Regions.ch2_mansion_basement,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
    ],
    Regions.ch2_spamton_neo: [
        LocationData(
            LocationIDs.ch2_mansion_spamton_neo_defeat_item_1,
            Regions.ch2_spamton_neo,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_mansion_spamton_neo_defeat_item_2,
            Regions.ch2_spamton_neo,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_mansion_spamton_neo_defeat_item_3,
            Regions.ch2_spamton_neo,
            should_be_included=lambda world: world.is_not_weird_route_only(),
            group=LocationGroups.chapter2,
        ),
    ],
    Regions.ch2_post_chapter_castle_town: [
        LocationData(
            LocationIDs.ch2_fountain_sealed,
            Regions.ch2_post_chapter_castle_town,
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_castle_town_tasque_manager_says_challenge,
            Regions.ch2_post_chapter_castle_town,
            should_be_included=lambda world: world.is_all_recruits(),
            group=LocationGroups.chapter2,
        ),
        LocationData(
            LocationIDs.ch2_castle_town_all_stars_challenge,
            Regions.ch2_post_chapter_castle_town,
            should_be_included=lambda world: world.is_all_recruits(),
            group=LocationGroups.chapter2,
        ),
    ],
}
