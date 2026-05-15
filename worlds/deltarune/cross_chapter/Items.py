from enum import StrEnum
from ..Items import (
    ItemData,
    ConditionalItemData,
    ItemIDs,
    generic_create_items,
    generic_get_filler_and_trap_items,
    ItemGroups,
)
from typing import TYPE_CHECKING
from BaseClasses import ItemClassification

if TYPE_CHECKING:
    from .. import DeltaruneWorld


class CCItems(StrEnum):
    # Gaster
    what_interresting_behavior = "WHAT INTERESTING BEHAVIOR."

    s_r_n_actions = "S/R/N-Action"

    # Characters
    kris = "Kris"
    susie = "Susie"
    ralsei = "Ralsei"
    noelle = "Noelle"

    # Healing Items
    dark_candy = "Dark Candy"
    clubsSandwich = "ClubsSandwich"
    dark_burger = "Dark Burger"
    dd_burger = "DD-Burger"
    lancer_cookie = "Lancer Cookie"
    spincake = "Spincake"
    revivemint = "Revive Mint"
    execbuffet = "ExecBuffet"
    tensiongem = "TensionGem"

    # Currency
    glowshard = "Glowshard"
    dogdollard = "DogDollar"
    dark_dollar_1 = "1 Dark Dollar"
    dark_dollars_20 = "20 Dark Dollars"
    dark_dollars_40 = "40 Dark Dollars"
    dark_dollars_80 = "80 Dark Dollars"
    dark_dollars_100 = "100 Dark Dollars"
    dark_dollars_250 = "250 Dark Dollars"
    dark_dollars_500 = "500 Dark Dollars"

    # Weapons
    progressive_kris_weapons = "Progressive Kris Weapons"
    progressive_susie_weapons = "Progressive Susie Weapons"
    progressive_ralsei_weapons = "Progressive Ralsei Weapons"
    progressive_noelle_weapons = "Progressive Noelle Weapons"
    twistedswd = "TwistedSwd"
    everybodyweapon = "EverybodyWeapon"

    # Armors
    amber_card = "Amber Card"
    pink_ribbon = "Pink Ribbon"
    white_ribbon = "White Ribbon"
    silver_card = "Silver Card"
    spikeband = "SpikeBand"
    twin_ribbon = "Twin Ribbon"
    tensionbow = "TensionBow"

    shadowcrystal = "ShadowCrystal"
    purecrystal = "PureCrystal"


cross_chapter_items = {
    CCItems.dark_dollar_1.value: ItemData(
        ItemIDs.dark_dollar_1.value, ItemClassification.filler, [ItemGroups.currencies]
    ),
    CCItems.dark_dollars_20.value: ItemData(
        ItemIDs.dark_dollars_20.value, ItemClassification.filler, [ItemGroups.currencies]
    ),
    CCItems.dark_dollars_40.value: ItemData(
        ItemIDs.dark_dollars_40.value, ItemClassification.filler, [ItemGroups.currencies]
    ),
    CCItems.dark_dollars_80.value: ItemData(
        ItemIDs.dark_dollars_80.value, ItemClassification.filler, [ItemGroups.currencies]
    ),
    CCItems.dark_dollars_100.value: ItemData(
        ItemIDs.dark_dollars_100.value, ItemClassification.filler, [ItemGroups.currencies]
    ),
    CCItems.dark_dollars_250.value: ItemData(
        ItemIDs.dark_dollars_250.value, ItemClassification.filler, [ItemGroups.currencies]
    ),
    CCItems.dark_dollars_500.value: ItemData(
        ItemIDs.dark_dollars_500.value, ItemClassification.filler, [ItemGroups.currencies]
    ),
    CCItems.what_interresting_behavior.value: ItemData(
        ItemIDs.what_interesting_behavior.value, ItemClassification.progression | ItemClassification.useful, amount=0
    ),
}

cross_chapter_conditional_items = {
    CCItems.s_r_n_actions.value: ConditionalItemData(
        ItemIDs.s_r_n_actions.value,
        ItemClassification.progression,
        lambda world: world.is_fun_gang_actions_unlockable() and world.has_at_least_one_chapter_included([2, 3, 4]),
    ),
    # Characters
    CCItems.kris.value: ConditionalItemData(
        ItemIDs.kris.value,
        ItemClassification.progression | ItemClassification.useful,
        lambda world: world.is_kris_unlockable(),
        [ItemGroups.characters],
    ),
    CCItems.susie.value: ConditionalItemData(
        ItemIDs.susie.value,
        ItemClassification.progression | ItemClassification.useful,
        lambda world: world.is_characters_unlockables(),
        [ItemGroups.characters],
    ),
    CCItems.ralsei.value: ConditionalItemData(
        ItemIDs.ralsei.value,
        ItemClassification.progression | ItemClassification.useful,
        lambda world: world.is_characters_unlockables(),
        [ItemGroups.characters],
    ),
    CCItems.noelle.value: ConditionalItemData(
        ItemIDs.noelle.value,
        ItemClassification.progression | ItemClassification.useful,
        lambda world: world.include_chapter(2) and world.is_characters_unlockables(),
        [ItemGroups.characters],
    ),
    # Fusions
    CCItems.dd_burger.value: ConditionalItemData(
        ItemIDs.dd_burger.value,
        ItemClassification.filler,
        lambda world: world.can_access_fusion(),
        [ItemGroups.healing_item],
    ),
    CCItems.silver_card.value: ConditionalItemData(
        ItemIDs.silver_card.value,
        ItemClassification.filler,
        lambda world: world.can_access_fusion(),
        [ItemGroups.armors],
    ),
    # Require Pink Ribbon that can be found in chapter 2 and 3 and White Ribbon that can be found in chapter 1 and 3 and starting armor for chapter 2
    CCItems.twin_ribbon.value: ConditionalItemData(
        ItemIDs.twin_ribbon.value,
        ItemClassification.useful,
        lambda world: world.can_access_fusion()
        and world.has_at_least_one_chapter_included([2, 3])
        and world.has_at_least_one_chapter_included([1, 2, 3]),
        [ItemGroups.armors],
    ),
    # Require IronShackle that is exclusive to chapter 1 and Glow Wrist to chapter 2 (shop) and chapter 4 (starting armor like chapter 3 but chapter 3 can't fuse)
    CCItems.spikeband.value: ConditionalItemData(
        ItemIDs.spikeband.value,
        ItemClassification.useful,
        lambda world: world.can_access_fusion()
        and world.include_chapter(1)
        and world.has_at_least_one_chapter_included([2, 4]),
        [ItemGroups.armors],
    ),
    # Require B.ShotBowtie that is exclusive to chapter 2 and can't be obtained on weird route
    CCItems.tensionbow.value: ConditionalItemData(
        ItemIDs.tensionbow.value,
        ItemClassification.useful,
        lambda world: world.can_access_fusion() and world.include_chapter(2) and not world.is_weird_route(),
        [ItemGroups.tension_items, ItemGroups.armors],
    ),
    # Progressive weapons
    CCItems.progressive_kris_weapons.value: ConditionalItemData(
        ItemIDs.progressive_kris_weapons.value,
        ItemClassification.useful,
        lambda world: world.is_kris_weapons_progressive(),
        [ItemGroups.weapons],
        0,
    ),
    CCItems.progressive_susie_weapons.value: ConditionalItemData(
        ItemIDs.progressive_susie_weapons.value,
        ItemClassification.useful,
        lambda world: world.is_susie_weapons_progressive(),
        [ItemGroups.weapons],
        0,
    ),
    CCItems.progressive_ralsei_weapons.value: ConditionalItemData(
        ItemIDs.progressive_ralsei_weapons.value,
        ItemClassification.useful,
        lambda world: world.is_ralsei_weapons_progressive(),
        [ItemGroups.weapons],
        0,
    ),
    CCItems.progressive_noelle_weapons.value: ConditionalItemData(
        ItemIDs.progressive_noelle_weapons.value,
        ItemClassification.progression | ItemClassification.useful,
        lambda world: world.include_chapter(2) and world.is_noelle_weapons_progressive(),
        [ItemGroups.weapons],
        0,
    ),
    # Unused
    CCItems.twistedswd.value: ConditionalItemData(
        ItemIDs.twistedswd.value,
        ItemClassification.useful,
        lambda world: world.can_access_fusion()
        and world.include_chapter(2)
        and world.is_unused_items_included()
        and world.is_weird_route(),
        [ItemGroups.weapons, ItemGroups.kris_weapons, ItemGroups.unused_items],
    ),
    CCItems.purecrystal.value: ConditionalItemData(
        ItemIDs.purecrystal.value,
        ItemClassification.progression,
        lambda world: world.can_access_fusion()
        and world.include_chapter(2)
        and world.is_unused_items_included()
        and world.is_weird_route(),
        [ItemGroups.fusion_ingredient, ItemGroups.unused_items],
    ),
    CCItems.everybodyweapon.value: ConditionalItemData(
        ItemIDs.everybodyweapon.value,
        ItemClassification.useful,
        lambda world: world.is_everybodyweapon_included(),
        [
            ItemGroups.weapons,
            ItemGroups.kris_weapons,
            ItemGroups.susie_weapons,
            ItemGroups.ralsei_weapons,
            ItemGroups.noelle_weapons,
            ItemGroups.unused_items,
        ],
        amount=4,
    ),
}


def create_items(world: "DeltaruneWorld"):
    return generic_create_items(world, cross_chapter_items, cross_chapter_conditional_items)


def get_filler_and_trap_items(world: "DeltaruneWorld"):
    return generic_get_filler_and_trap_items(world, cross_chapter_items, cross_chapter_conditional_items)
