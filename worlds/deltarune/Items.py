from BaseClasses import Item, ItemClassification
from enum import Enum, StrEnum
from typing import TYPE_CHECKING, NamedTuple, Optional, Callable

if TYPE_CHECKING:
    from . import DeltaruneWorld, DeltaruneOptions

glitched_item_name = "Deltarune is an episodic role-playing video game by American indie developer Toby Fox."
progressive_weapon_name = "Progressive Weapon"

class ItemGroups(StrEnum):
    healing_item = "Healing Items"
    fusion_ingredient = "Fusion Ingredients"
    armors = "Armors"
    weapons = "Weapons"
    kris_weapons = "Kris Weapons"
    susie_weapons = "Susie Weapons"
    ralsei_weapons = "Ralsei Weapons"
    noelle_weapons = "Noelle Weapons"
    eggs = "Eggs"
    currencies = "Currencies"
    region_blockers = "Story Blockers"
    moss = "Moss"
    jevil_keys = "Jevil Keys"
    spamton_access = "Spamton Access"
    tension_items = "Tension Items"
    mantle_items = "Mantle Items"
    unused_items = "Unused Items"
    traps = "Traps"
    characters = "Characters"

class ItemData(NamedTuple):
    code: Optional[int]
    classification: ItemClassification
    groups: Optional[list[ItemGroups]] = []
    amount: Optional[int] = 1
    blacklist_filler: Optional[bool] = False


class ConditionalItemData(NamedTuple):
    code: Optional[int]
    classification: ItemClassification
    should_be_included: Callable[["DeltaruneWorld"], bool]
    groups: Optional[list[ItemGroups]] = []
    amount: Optional[int] = 1
    blacklist_filler: Optional[bool] = False


class DeltaruneItem(Item):
    game: str = "Deltarune"


class ItemIDs(Enum):
    # UT Integration
    glitched_item = -1

    dark_candy = 1
    revivemint = 2
    glowshard = 3
    manual = 4
    brokencake_consumable = 5
    # nothing = 6
    spincake = 7
    darkburger = 8
    lancer_cookie = 9
    gigasalad = 10
    clubsandwich = 11
    heartsdonut = 12
    chocdiamond = 13
    favsandwich = 14
    rouxlsroux = 15

    cd_bagel = 16
    mannequin_consumable = 17
    kris_tea = 18
    noelle_tea = 19
    ralsei_tea = 20
    susie_tea = 21
    dd_burger = 22
    lightcandy = 23
    butjuice = 24
    spagetticode = 25
    javacookie = 26
    tensionbit = 27
    tensiongem = 28
    tensionmax = 29
    revivedust = 30
    revivebrite = 31
    spoison = 32
    dogdollar = 33
    tvdinner = 34
    # nothing = 35
    flatsoda = 36
    tvslop = 37
    execbuffet = 38
    deluxedinner = 39

    ancientsweet = 60
    rhapsotea = 61
    scarlixir = 62
    bittertear = 63

    chapter_1_egg = 10002
    brokencake = 10003
    broken_key_a = 10004
    door_key = 10005
    broken_key_b = 10006
    broken_key_c = 10007

    emptydisk = 10010
    # nothing
    keygen = 10012
    shadowcrystal = 10013
    purecrystal = 1015

    oddcontroller = 10016
    # nothing
    tripticket = 10018

    sheetmusic = 10030
    claimbclaws = 10031

    # great_door_key = 11000
    bake_sale_ticket = 11001
    # king_chess_piece = 11002
    castle_key = 11003
    top_cake = 11004
    castle_moss = 11005
    joe_life_savings = 11006
    city_moss = 11007
    # susie_pencil = 11008
    safety_vest = 11009
    mansion_reservation = 11010
    chapter_2_egg = 11011
    chapter_3_egg = 11012
    board_2_cartridge = 11013
    vip_pass = 11014
    # nothing = 11015
    smile = 11016
    board_moss = 11017
    ice_key = 11018
    shelter_key = 11019
    sacred_moss = 11020
    chapter_4_egg = 11021

    amber_card = 20001
    dice_brace = 20002
    pink_ribbon = 20003
    white_ribbon = 20004
    ironshackle = 20005
    mouse_token = 20006
    jevilstail = 20007
    silver_card = 20008
    twin_ribbon = 20009
    glowwrist = 20010
    chainmail = 20011
    bshotbowtie = 20012
    spikeband = 20013
    tensionbow = 20015
    mannequin = 20016
    darkgoldband = 20017
    skymantle = 20018
    spikeshackle = 20019

    frayedbowtie = 20020
    dealmaker = 20021
    royalpin = 20022
    shadowmantle = 20023
    lodestone = 20024
    gingerguard = 20025
    blue_ribbon = 20026
    tennatie = 20027

    waferguard = 20050
    mysticband = 20051
    powerband = 20052
    princessrbn = 20053
    goldwidow = 20054

    wood_blade = 30001
    mane_ax = 30002
    red_scarf = 30003
    everybodyweapon = 30004
    spookysword = 30005
    brave_ax = 30006
    devilsknife = 30007
    trefoil = 30008
    ragger = 30009
    daintyscarf = 30010
    twistedswd = 30011
    snowring = 30012
    thornring = 30013
    bounceblade = 30014
    cheerscarf = 30015
    mechasaber = 30016
    autoaxe = 30017
    fiberscarf = 30018
    ragger2 = 30019
    brokenswd = 30020
    puppetscarf = 30021
    freezering = 30022
    saber10 = 30023
    toxicaxe = 30024
    flexscarf = 30025
    blackshard = 30026

    jingleblade = 30050
    scarfmark = 30051
    justiceaxe = 30052
    wingblade = 30053
    absorbaxe = 30054

    dark_dollar_1 = 40001
    dark_dollars_20 = 40020
    dark_dollars_40 = 40040
    dark_dollars_80 = 40080
    dark_dollars_100 = 40100
    dark_dollars_250 = 40250
    dark_dollars_500 = 40500

    progressive_kris_weapons = 50000
    progressive_susie_weapons = 50001
    progressive_ralsei_weapons = 50002
    progressive_noelle_weapons = 50003

    kris = 60001
    susie = 60002
    ralsei = 60003
    noelle = 60004
    what_interesting_behavior = 66666

    king_shape_key_piece = 70000
    key_gen_2_segment = 70001
    remote_battery = 70002
    combinaison_lock_digit = 70003

    point_1 = 80001
    points_2 = 80002
    points_10 = 80010
    points_50 = 80050
    points_120 = 80120
    points_300 = 80300
    points_500 = 80500

    chapter_1_unlock = 90001
    chapter_2_unlock = 90002
    chapter_3_unlock = 90003
    chapter_4_unlock = 90004
    chapter_5_unlock = 90005


def generic_create_items(
    world: "DeltaruneWorld", items: dict[str, ItemData], conditional_items: dict[str, ConditionalItemData]
) -> list[str]:
    item_pool: list[str] = []

    for item_name, item_data in items.items():
        item_pool += [item_name] * item_data.amount

    for item_name, item_data in conditional_items.items():
        if item_data.should_be_included(world):
            item_pool += [item_name] * item_data.amount

    return item_pool


def generic_get_filler_and_trap_items(
    world: "DeltaruneWorld", items: dict[str, ItemData], conditional_items: dict[str, ConditionalItemData]
) -> dict[str, ItemData | ConditionalItemData]:
    filler_items: dict[str, ItemData | ConditionalItemData] = {}

    filler_items |= {
        item_name: item_data
        for item_name, item_data in items.items()
        if (item_data.classification == ItemClassification.filler and not item_data.blacklist_filler)
        or item_data.classification == ItemClassification.trap
    }
    filler_items |= {
        item_name: item_data
        for item_name, item_data in conditional_items.items()
        if (
            (item_data.classification == ItemClassification.filler and not item_data.blacklist_filler)
            or item_data.classification == ItemClassification.trap
        )
        and item_data.should_be_included(world)
    }

    return filler_items


def convert_filler_and_trap_to_weights(items: dict[str, ItemData | ConditionalItemData], options: "DeltaruneOptions"):
    fillers_with_weights = {}

    healing_fillers = [
        item_name for item_name, item_data in items.items() if ItemGroups.healing_item in item_data.groups
    ]
    armor_fillers = [item_name for item_name, item_data in items.items() if ItemGroups.armors in item_data.groups]
    tension_fillers = [
        item_name for item_name, item_data in items.items() if ItemGroups.tension_items in item_data.groups
    ]
    currency_fillers = [
        item_name for item_name, item_data in items.items() if ItemGroups.currencies in item_data.groups
    ]
    traps = [item_name for item_name, item_data in items.items() if item_data.classification == ItemClassification.trap]
    smile_fillers = [item_name for item_name, item_data in items.items() if item_data.code == ItemIDs.smile.value]

    healing_adjusted_weight = (
        options.filler_healing_weight.value / len(healing_fillers) if len(healing_fillers) > 0 else 0
    )
    armor_adjusted_weight = options.filler_armor_weight.value / len(armor_fillers) if len(armor_fillers) > 0 else 0
    tension_adjusted_weight = (
        options.filler_tension_weight.value / len(tension_fillers) if len(tension_fillers) > 0 else 0
    )
    currency_adjusted_weight = (
        options.filler_currency_weight.value / len(currency_fillers) if len(currency_fillers) > 0 else 0
    )
    trap_adjusted_weight = options.trap_weight.value / len(traps) if len(traps) > 0 else 0
    smile_adjusted_weight = options.filler_smile_weight.value / len(smile_fillers) if len(smile_fillers) > 0 else 0

    for item_name in healing_fillers:
        fillers_with_weights[item_name] = healing_adjusted_weight
    for item_name in armor_fillers:
        fillers_with_weights[item_name] = armor_adjusted_weight
    for item_name in tension_fillers:
        fillers_with_weights[item_name] = tension_adjusted_weight
    for item_name in currency_fillers:
        fillers_with_weights[item_name] = currency_adjusted_weight
    for item_name in traps:
        fillers_with_weights[item_name] = trap_adjusted_weight
    for item_name in smile_fillers:
        fillers_with_weights[item_name] = smile_adjusted_weight

    return fillers_with_weights


def get_item_groups(items: dict[str, ItemData | ConditionalItemData]):
    groups: dict[str : set[str]] = {}

    for item_name, item_data in items:
        for group_name in item_data.groups:
            groups.setdefault(group_name.value, set()).add(item_name)

    return groups
