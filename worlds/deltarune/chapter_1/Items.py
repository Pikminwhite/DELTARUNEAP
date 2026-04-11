from ..Items import (
    ItemIDs,
    ItemData,
    ConditionalItemData,
    generic_create_items,
    generic_get_filler_items,
    DeltaruneItem,
    ItemGroups,
)
from ..cross_chapter.Items import CCItems
from typing import TYPE_CHECKING
from BaseClasses import ItemClassification
from enum import StrEnum

if TYPE_CHECKING:
    from .. import DeltaruneWorld


class Ch1Items(StrEnum):
    chapter_1_unlock = "Chapter 1 Unlock"

    # Healing Items
    heartsdonut = "HeartsDonut"
    chocdiamond = "ChocDiamond"
    rouxlsroux = "RouxlsRoux"
    brokencake_consumable = "BrokenCake (Consumable)"
    gigasalad = "GigaSalad"
    favsandwich = "FavSandwich"

    # Armors
    dice_brace = "Dice Bracelet"
    ironshackle = "IronShackle"
    jevilstail = "JevilsTail"
    mouse_token = "Mouse Token"

    # Weapons
    spookysword = "Spookysword"
    trefoil = "Trefoil"
    brave_ax = "Brave Ax"
    devilsknife = "Devilsknife"
    ragger = "Ragger"
    daintyscarf = "DaintyScarf"

    egg = "CH1 Egg"
    castle_moss = "Castle Moss"

    manual = "Manual"

    brokencake = "BrokenCake"
    top_cake = "Top Cake"

    broken_key_a = "Broken Key A"
    broken_key_b = "Broken Key B"
    broken_key_c = "Broken Key C"

    # Blockers
    # great_door_key = "Great Door Key"
    # king_chess_piece = "King Chess Piece"
    bake_sale_ticket = "Bake Sale Ticket"
    castle_key = "Castle Key"
    door_key = "Door Key"

    # Macguffins
    king_shape_key_piece = "King-Shaped Key Piece"


chapter1_macguffin_item = Ch1Items.king_shape_key_piece.value

chapter1_items = {
    CCItems.dark_candy.value: ItemData(ItemIDs.dark_candy.value, ItemClassification.filler, [ItemGroups.healing_item]),
    Ch1Items.rouxlsroux.value: ItemData(ItemIDs.rouxlsroux.value, ItemClassification.filler, [ItemGroups.healing_item]),
    CCItems.clubsSandwich.value: ItemData(
        ItemIDs.clubsandwich.value, ItemClassification.filler, [ItemGroups.healing_item]
    ),
    CCItems.dark_burger.value: ItemData(
        ItemIDs.darkburger.value, ItemClassification.filler, [ItemGroups.healing_item, ItemGroups.fusion_ingredient]
    ),
    Ch1Items.heartsdonut.value: ItemData(
        ItemIDs.heartsdonut.value, ItemClassification.filler, [ItemGroups.healing_item]
    ),
    Ch1Items.chocdiamond.value: ItemData(
        ItemIDs.chocdiamond.value, ItemClassification.filler, [ItemGroups.healing_item]
    ),
    CCItems.revivemint.value: ItemData(
        ItemIDs.revivemint.value, ItemClassification.filler, [ItemGroups.healing_item], amount=2
    ),
    CCItems.spincake.value: ItemData(ItemIDs.spincake.value, ItemClassification.filler, [ItemGroups.healing_item]),
    CCItems.amber_card.value: ItemData(
        ItemIDs.amber_card.value, ItemClassification.filler, [ItemGroups.armors, ItemGroups.fusion_ingredient]
    ),
    CCItems.glowshard.value: ItemData(ItemIDs.glowshard.value, ItemClassification.filler, [ItemGroups.currencies]),
    Ch1Items.dice_brace.value: ItemData(ItemIDs.dice_brace.value, ItemClassification.useful, [ItemGroups.armors]),
    Ch1Items.spookysword.value: ItemData(
        ItemIDs.spookysword.value, ItemClassification.useful, [ItemGroups.weapons, ItemGroups.kris_weapons]
    ),
    Ch1Items.brave_ax.value: ItemData(
        ItemIDs.brave_ax.value, ItemClassification.useful, [ItemGroups.weapons, ItemGroups.susie_weapons]
    ),
    Ch1Items.ragger.value: ItemData(
        ItemIDs.ragger.value, ItemClassification.useful, [ItemGroups.weapons, ItemGroups.ralsei_weapons]
    ),
    Ch1Items.daintyscarf.value: ItemData(
        ItemIDs.daintyscarf.value, ItemClassification.useful, [ItemGroups.weapons, ItemGroups.ralsei_weapons]
    ),
    Ch1Items.manual.value: ItemData(
        ItemIDs.manual.value, ItemClassification.progression | ItemClassification.useful, amount=2
    ),
    # Blockers
    Ch1Items.bake_sale_ticket.value: ItemData(
        ItemIDs.bake_sale_ticket.value, ItemClassification.progression, [ItemGroups.region_blockers]
    ),
    Ch1Items.castle_key.value: ItemData(
        ItemIDs.castle_key.value, ItemClassification.progression, [ItemGroups.region_blockers]
    ),
    Ch1Items.brokencake.value: ItemData(ItemIDs.brokencake.value, ItemClassification.progression),
    Ch1Items.top_cake.value: ItemData(ItemIDs.top_cake.value, ItemClassification.progression),
    Ch1Items.ironshackle.value: ItemData(
        ItemIDs.ironshackle.value,
        ItemClassification.progression | ItemClassification.useful,
        [ItemGroups.armors, ItemGroups.fusion_ingredient],
    ),
    CCItems.white_ribbon.value: ItemData(
        ItemIDs.white_ribbon.value, ItemClassification.progression, [ItemGroups.armors, ItemGroups.fusion_ingredient]
    ),
}

chapter1_conditional_items = {
    # Hidden Items
    Ch1Items.egg.value: ConditionalItemData(
        ItemIDs.chapter_1_egg.value,
        ItemClassification.useful,
        lambda world: world.is_hidden_items_randomized(),
        [ItemGroups.eggs],
    ),
    Ch1Items.castle_moss.value: ConditionalItemData(
        ItemIDs.castle_moss.value,
        ItemClassification.useful,
        lambda world: world.is_hidden_items_randomized(),
        [ItemGroups.moss],
    ),
    Ch1Items.broken_key_a.value: ConditionalItemData(
        ItemIDs.broken_key_a.value,
        ItemClassification.progression,
        lambda world: world.is_hidden_items_randomized(),
        [ItemGroups.jevil_keys],
    ),
    Ch1Items.broken_key_b.value: ConditionalItemData(
        ItemIDs.broken_key_b.value,
        ItemClassification.progression,
        lambda world: world.is_hidden_items_randomized(),
        [ItemGroups.jevil_keys],
    ),
    Ch1Items.broken_key_c.value: ConditionalItemData(
        ItemIDs.broken_key_c.value,
        ItemClassification.progression,
        lambda world: world.is_hidden_items_randomized(),
        [ItemGroups.jevil_keys],
    ),
    Ch1Items.door_key.value: ConditionalItemData(
        ItemIDs.door_key.value,
        ItemClassification.progression,
        lambda world: world.is_hidden_items_randomized(),
        [ItemGroups.jevil_keys],
    ),
    # Secret boss
    Ch1Items.jevilstail.value: ConditionalItemData(
        ItemIDs.jevilstail.value,
        ItemClassification.useful,
        lambda world: world.is_secret_bosses_randomized(),
        [ItemGroups.armors],
    ),
    Ch1Items.devilsknife.value: ConditionalItemData(
        ItemIDs.devilsknife.value,
        ItemClassification.useful,
        lambda world: world.is_secret_bosses_randomized(),
        [ItemGroups.weapons, ItemGroups.susie_weapons],
    ),
    CCItems.shadowcrystal.value: ConditionalItemData(
        ItemIDs.shadowcrystal.value, ItemClassification.useful, lambda world: world.is_secret_bosses_randomized()
    ),
    Ch1Items.chapter_1_unlock.value: ConditionalItemData(
        ItemIDs.chapter_1_unlock.value,
        ItemClassification.progression,
        lambda world: world.is_chapters_randomized(),
        [ItemGroups.region_blockers],
    ),
    # Amount is handle in __init__.py handle_macguffins_items()
    Ch1Items.king_shape_key_piece.value: ConditionalItemData(
        ItemIDs.king_shape_key_piece.value,
        ItemClassification.progression_skip_balancing,
        lambda world: world.is_final_chapter(1),
        [ItemGroups.region_blockers],
        amount=0,
    ),
    # Unused Items
    Ch1Items.brokencake_consumable.value: ConditionalItemData(
        ItemIDs.brokencake_consumable.value,
        ItemClassification.filler,
        lambda world: world.is_unused_items_included(),
        [ItemGroups.healing_item],
    ),
    Ch1Items.gigasalad.value: ConditionalItemData(
        ItemIDs.gigasalad.value,
        ItemClassification.filler,
        lambda world: world.is_unused_items_included(),
        [ItemGroups.healing_item],
    ),
    Ch1Items.favsandwich.value: ConditionalItemData(
        ItemIDs.favsandwich.value,
        ItemClassification.filler,
        lambda world: world.is_unused_items_included(),
        [ItemGroups.healing_item],
    ),
    Ch1Items.mouse_token.value: ConditionalItemData(
        ItemIDs.mouse_token.value,
        ItemClassification.useful,
        lambda world: world.is_unused_items_included(),
        [ItemGroups.armors],
    ),
    Ch1Items.trefoil.value: ConditionalItemData(
        ItemIDs.trefoil.value,
        ItemClassification.useful,
        lambda world: world.is_unused_items_included(),
        [ItemGroups.weapons],
    ),
}


def create_items(world: "DeltaruneWorld"):
    return generic_create_items(world, chapter1_items, chapter1_conditional_items)


def get_filler_items(world: "DeltaruneWorld"):
    return generic_get_filler_items(world, chapter1_items, chapter1_conditional_items)
