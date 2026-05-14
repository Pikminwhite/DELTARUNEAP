from ..Items import (
    ItemGroups,
    ItemIDs,
    ItemData,
    ConditionalItemData,
    generic_create_items,
    generic_get_filler_and_trap_items,
    DeltaruneItem,
)
from ..cross_chapter.Items import CCItems
from typing import TYPE_CHECKING
from BaseClasses import ItemClassification
from enum import StrEnum

if TYPE_CHECKING:
    from .. import DeltaruneWorld


class Ch2Items(StrEnum):
    chapter_2_unlock = "Chapter 2 Unlock"

    # Healing Items
    cd_bagel = "CD Bagel"
    kris_tea = "Kris Tea"
    noelle_tea = "Noelle Tea"
    ralsei_tea = "Ralsei Tea"
    susie_tea = "Susie Tea"
    lightcandy = "LightCandy"
    butjuice = "ButJuice"
    spagetticode = "SpagettiCode"
    revivedust = "ReviveDust"
    javacookie = "JavaCookie"
    revivebrite = "ReviveBrite"
    mannequin_consumable = "Mannequin (Consumable)"

    darkgoldband = "DarkGoldBand"

    spoison = "S.POISON"
    tensionbit = "TensionBit"

    # Armors
    glowwrist = "GlowWrist"
    dealmaker = "DealMaker"
    mannequin = "Mannequin"
    royalpin = "RoyalPin"
    chainmail = "ChainMail"
    frayedbowtie = "FrayedBowtie"
    bshotbowtie = "B.ShotBowtie"
    skymantle = "SkyMantle"
    spikeshackle = "SpikeShackle"

    # Weapons
    mechasaber = "MechaSaber"
    bounceblade = "BounceBlade"
    autoaxe = "AutoAxe"
    fiberscarf = "FiberScarf"
    ragger2 = "Ragger2"
    puppetscarf = "PuppetScarf"
    cheerscarf = "CheerScarf"
    brokenswd = "BrokenSwd"
    snowring = "SnowRing"
    freezering = "FreezeRing"
    thornring = "ThornRing"

    egg = "CH2 Egg"
    joe_life_savings = "Jigsaw Joe's Life Savings"
    city_moss = "City Moss"
    dogdollar = "DogDollar"

    emptydisk = "EmptyDisk"
    keygen = "KeyGen"

    # Blockers
    safety_vest = "Safety Vest"
    mansion_reservation = "Mansion Reservation"

    # Macguffins
    keygen_2_segment = "KeyGen 2 Segment"


chapter2_macguffin_item = Ch2Items.keygen_2_segment.value

chapter2_items = {
    Ch2Items.cd_bagel.value: ItemData(ItemIDs.cd_bagel.value, ItemClassification.filler, [ItemGroups.healing_item]),
    CCItems.clubsSandwich.value: ItemData(
        ItemIDs.clubsandwich.value, ItemClassification.filler, [ItemGroups.healing_item]
    ),
    Ch2Items.lightcandy.value: ItemData(ItemIDs.lightcandy.value, ItemClassification.filler, [ItemGroups.healing_item]),
    CCItems.revivemint.value: ItemData(
        ItemIDs.revivemint.value, ItemClassification.filler, [ItemGroups.healing_item], amount=2
    ),
    CCItems.spincake.value: ItemData(ItemIDs.spincake.value, ItemClassification.filler, [ItemGroups.healing_item]),
    CCItems.tensiongem.value: ItemData(ItemIDs.tensiongem.value, ItemClassification.filler, [ItemGroups.tension_items]),
    Ch2Items.joe_life_savings.value: ItemData(
        ItemIDs.joe_life_savings.value,
        ItemClassification.filler,
        [ItemGroups.currencies],
        blacklist_filler=True,
    ),
    Ch2Items.mechasaber.value: ItemData(
        ItemIDs.mechasaber.value, ItemClassification.useful, [ItemGroups.weapons, ItemGroups.kris_weapons]
    ),
    Ch2Items.autoaxe.value: ItemData(
        ItemIDs.autoaxe.value, ItemClassification.useful, [ItemGroups.weapons, ItemGroups.susie_weapons]
    ),
    Ch2Items.fiberscarf.value: ItemData(
        ItemIDs.fiberscarf.value, ItemClassification.useful, [ItemGroups.weapons, ItemGroups.ralsei_weapons]
    ),
    Ch2Items.ragger2.value: ItemData(
        ItemIDs.ragger2.value, ItemClassification.useful, [ItemGroups.weapons, ItemGroups.ralsei_weapons]
    ),
    Ch2Items.bounceblade.value: ItemData(
        ItemIDs.bounceblade.value, ItemClassification.useful, [ItemGroups.weapons, ItemGroups.kris_weapons]
    ),
    Ch2Items.mannequin.value: ItemData(
        ItemIDs.mannequin.value, ItemClassification.filler, [ItemGroups.armors], blacklist_filler=True
    ),
    # Noelle royal pin
    Ch2Items.royalpin.value: ItemData(ItemIDs.royalpin.value, ItemClassification.useful, [ItemGroups.armors]),
    Ch2Items.tensionbit.value: ItemData(
        ItemIDs.tensionbit.value, ItemClassification.progression | ItemClassification.useful, [ItemGroups.tension_items]
    ),
    Ch2Items.glowwrist.value: ItemData(
        ItemIDs.glowwrist.value,
        ItemClassification.progression | ItemClassification.useful,
        [ItemGroups.armors, ItemGroups.fusion_ingredient],
        amount=2,
    ),
    CCItems.pink_ribbon.value: ItemData(
        ItemIDs.pink_ribbon.value, ItemClassification.progression, [ItemGroups.armors, ItemGroups.fusion_ingredient]
    ),
    Ch2Items.safety_vest.value: ItemData(
        ItemIDs.safety_vest.value, ItemClassification.progression, [ItemGroups.region_blockers]
    ),
    # Amount is handle in __init__.py handle_macguffins_items()
    Ch2Items.keygen_2_segment.value: ItemData(
        ItemIDs.key_gen_2_segment.value,
        ItemClassification.progression_skip_balancing,
        [ItemGroups.region_blockers],
        amount=0,
    ),
}

chapter2_conditional_items = {
    Ch2Items.spagetticode.value: ConditionalItemData(
        ItemIDs.spagetticode.value,
        ItemClassification.filler,
        lambda world: world.is_not_weird_route_only(),
        [ItemGroups.healing_item],
    ),
    Ch2Items.butjuice.value: ConditionalItemData(
        ItemIDs.butjuice.value,
        ItemClassification.filler,
        lambda world: world.is_not_weird_route_only(),
        [ItemGroups.healing_item],
    ),
    Ch2Items.spoison.value: ConditionalItemData(
        ItemIDs.spoison.value,
        ItemClassification.trap,
        lambda world: world.is_not_weird_route_only(),
        [ItemGroups.traps],
    ),
    Ch2Items.kris_tea.value: ConditionalItemData(
        ItemIDs.kris_tea.value,
        ItemClassification.filler,
        lambda world: world.is_not_weird_route_only(),
        [ItemGroups.healing_item],
    ),
    Ch2Items.noelle_tea.value: ConditionalItemData(
        ItemIDs.noelle_tea.value,
        ItemClassification.filler,
        lambda world: world.is_not_weird_route_only(),
        [ItemGroups.healing_item],
    ),
    Ch2Items.ralsei_tea.value: ConditionalItemData(
        ItemIDs.ralsei_tea.value,
        ItemClassification.filler,
        lambda world: world.is_not_weird_route_only(),
        [ItemGroups.healing_item],
    ),
    Ch2Items.susie_tea.value: ConditionalItemData(
        ItemIDs.susie_tea.value,
        ItemClassification.filler,
        lambda world: world.is_not_weird_route_only(),
        [ItemGroups.healing_item],
    ),
    Ch2Items.revivedust.value: ConditionalItemData(
        ItemIDs.revivedust.value,
        ItemClassification.filler,
        lambda world: world.is_not_weird_route_only(),
        [ItemGroups.healing_item],
    ),
    Ch2Items.royalpin.value: ConditionalItemData(
        ItemIDs.royalpin.value,
        ItemClassification.filler,
        lambda world: world.is_not_weird_route_only(),
        [ItemGroups.armors],
    ),
    Ch2Items.frayedbowtie.value: ConditionalItemData(
        ItemIDs.frayedbowtie.value,
        ItemClassification.filler,
        lambda world: world.is_not_weird_route_only(),
        [ItemGroups.armors],
    ),
    CCItems.glowshard.value: ConditionalItemData(
        ItemIDs.glowshard.value,
        ItemClassification.filler,
        lambda world: world.is_not_weird_route_only(),
        [ItemGroups.currencies],
    ),
    CCItems.dogdollard.value: ConditionalItemData(
        ItemIDs.dogdollar.value,
        ItemClassification.filler,
        lambda world: world.is_not_weird_route_only(),
        [ItemGroups.currencies],
        0,
    ),
    Ch2Items.egg.value: ConditionalItemData(
        ItemIDs.chapter_2_egg.value,
        ItemClassification.filler,
        lambda world: world.is_not_weird_route_only() and world.is_hidden_items_randomized(),
        [ItemGroups.eggs],
        blacklist_filler=True,
    ),
    Ch2Items.city_moss.value: ConditionalItemData(
        ItemIDs.city_moss.value,
        ItemClassification.filler,
        lambda world: world.is_not_weird_route_only() and world.is_hidden_items_randomized(),
        [ItemGroups.moss],
        blacklist_filler=True,
    ),
    Ch2Items.chainmail.value: ConditionalItemData(
        ItemIDs.chainmail.value,
        ItemClassification.useful,
        lambda world: world.is_not_weird_route_only(),
        [ItemGroups.armors],
    ),
    Ch2Items.brokenswd.value: ConditionalItemData(
        ItemIDs.brokenswd.value,
        ItemClassification.filler,
        lambda world: world.is_not_weird_route_only(),
        [ItemGroups.weapons],
        blacklist_filler=True,
    ),
    Ch2Items.mansion_reservation.value: ConditionalItemData(
        ItemIDs.mansion_reservation.value,
        ItemClassification.progression,
        lambda world: world.is_not_weird_route_only(),
        [ItemGroups.region_blockers],
    ),
    Ch2Items.bshotbowtie.value: ConditionalItemData(
        ItemIDs.bshotbowtie.value,
        ItemClassification.progression | ItemClassification.useful,
        lambda world: world.is_not_weird_route_only(),
        [ItemGroups.armors],
    ),
    # Weird route
    Ch2Items.freezering.value: ConditionalItemData(
        ItemIDs.freezering.value,
        ItemClassification.useful,
        lambda world: world.is_weird_route(),
        [ItemGroups.weapons, ItemGroups.noelle_weapons],
    ),
    Ch2Items.thornring.value: ConditionalItemData(
        ItemIDs.thornring.value,
        ItemClassification.progression | ItemClassification.useful,
        lambda world: world.is_weird_route(),
        [ItemGroups.weapons, ItemGroups.noelle_weapons, ItemGroups.fusion_ingredient],
    ),
    Ch2Items.chapter_2_unlock.value: ConditionalItemData(
        ItemIDs.chapter_2_unlock.value,
        ItemClassification.progression,
        lambda world: world.is_chapters_randomized(),
        [ItemGroups.region_blockers],
    ),
    # Secret Boss
    Ch2Items.emptydisk.value: ConditionalItemData(
        ItemIDs.emptydisk.value,
        ItemClassification.progression,
        lambda world: world.is_not_weird_route_only() and world.is_hidden_items_randomized(),
        [ItemGroups.spamton_access],
    ),
    Ch2Items.keygen.value: ConditionalItemData(
        ItemIDs.keygen.value,
        ItemClassification.progression,
        lambda world: world.is_not_weird_route_only() and world.is_hidden_items_randomized(),
        [ItemGroups.spamton_access],
    ),
    Ch2Items.dealmaker.value: ConditionalItemData(
        ItemIDs.dealmaker.value,
        ItemClassification.useful,
        lambda world: world.is_not_weird_route_only() and world.is_secret_bosses_randomized(),
        [ItemGroups.armors],
    ),
    Ch2Items.puppetscarf.value: ConditionalItemData(
        ItemIDs.puppetscarf.value,
        ItemClassification.useful,
        lambda world: world.is_secret_bosses_randomized(),
        [ItemGroups.weapons, ItemGroups.ralsei_weapons],
    ),
    CCItems.shadowcrystal.value: ConditionalItemData(
        ItemIDs.shadowcrystal.value,
        ItemClassification.filler,
        lambda world: world.is_secret_bosses_randomized(),
        blacklist_filler=True,
    ),
    # Unused Items
    Ch2Items.javacookie.value: ConditionalItemData(
        ItemIDs.javacookie.value,
        ItemClassification.filler,
        lambda world: world.is_unused_items_included(),
        [ItemGroups.healing_item, ItemGroups.unused_items],
    ),
    Ch2Items.revivebrite.value: ConditionalItemData(
        ItemIDs.revivebrite.value,
        ItemClassification.filler,
        lambda world: world.is_unused_items_included(),
        [ItemGroups.healing_item, ItemGroups.unused_items],
    ),
    Ch2Items.mannequin_consumable.value: ConditionalItemData(
        ItemIDs.mannequin_consumable.value,
        ItemClassification.filler,
        lambda world: world.is_unused_items_included(),
        [ItemGroups.healing_item, ItemGroups.unused_items],
    ),
    Ch2Items.darkgoldband.value: ConditionalItemData(
        ItemIDs.darkgoldband.value,
        ItemClassification.filler,
        lambda world: world.is_unused_items_included(),
        [ItemGroups.currencies, ItemGroups.unused_items],
    ),
    Ch2Items.skymantle.value: ConditionalItemData(
        ItemIDs.skymantle.value,
        ItemClassification.useful,
        lambda world: world.is_unused_items_included(),
        [ItemGroups.armors, ItemGroups.unused_items],
    ),
    Ch2Items.spikeshackle.value: ConditionalItemData(
        ItemIDs.spikeshackle.value,
        ItemClassification.useful,
        lambda world: world.is_unused_items_included(),
        [ItemGroups.armors, ItemGroups.unused_items],
    ),
    Ch2Items.cheerscarf.value: ConditionalItemData(
        ItemIDs.cheerscarf.value,
        ItemClassification.useful,
        lambda world: world.is_unused_items_included(),
        [ItemGroups.weapons, ItemGroups.ralsei_weapons, ItemGroups.unused_items],
    ),
}


def create_items(world: "DeltaruneWorld") -> list[DeltaruneItem]:
    return generic_create_items(world, chapter2_items, chapter2_conditional_items)


def get_filler_and_trap_items(world: "DeltaruneWorld"):
    return generic_get_filler_and_trap_items(world, chapter2_items, chapter2_conditional_items)
