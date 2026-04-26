from enum import StrEnum

from Options import Choice, Toggle, Range, PerGameCommonOptions, NamedRange, OptionGroup
from dataclasses import dataclass


class Notice(Choice):
    """
    THIS IS NOT AN OPTION:

    SHOULD A CHAPTER BE EXCLUDED
    FROM BOTH OF ITS NEIGHBORS,

    GENERATION WILL FAIL.

    (For example: Including only chapter 2 and 3 or just doing a single chapter WILL work fine.)
    (Including chapter 1, not including chapter 2, but including chapter 3 will not work.)"""

    display_name = "NOTICE: READ OPTION INFO"
    option_understood = 0
    default = 0


class ChosenRoute(Choice):
    """
    CHOOSE THE ROUTE
    THAT YOU PREFER.

    (All Recruits - Progress through the story normally. Recruit Everyone!!!)
    (Weird Route - Proceed through the "Weird Route" storyline while losing all possible recruits.)
    (Losing/Gaining recruits have been turned into checks.)"""

    display_name = "Chosen Route"
    option_all_recruits = 0
    option_weird_route = 1
    option_all_routes = 2
    default = option_all_recruits


class ChosenRouteOptions(StrEnum):
    all_recruits = "all_recruits"
    weird_route = "weird_route"
    all_routes = "all_routes"


class RandomizeChapters(Choice):
    """
    HOW WILL YOU PROGRESS
    THROUGH THE CHAPTERS?

    (In Order - The next chapter will be unlocked once you complete the one you're in. This is the recommended option.)
    (Randomized Chapters - Chapters are unlocked through getting checks. In Multiplayer, be prepared to wait a while!)
    (All Unlocked - All chapters are unlocked from the start. You will be expected to play through another chapter once stuck.)

    AS A REMINDER,

    YOUR GOAL IS
    TO SEE THE END
    OF ALL CHAPTERS."""

    display_name = "Randomize Chapters"
    option_in_order = 0
    option_randomized = 1
    option_all_unlocked = 2
    default = option_in_order


class RandomizeChapterOptions(StrEnum):
    in_order = "in_order"
    randomized = "randomized"
    all_unlocked = "all_unlocked"


class RandomizeSecretBosses(Choice):
    """
    ITEMS GIVEN BY THOSE
    POSSESSING SHADOW CRYSTALS
    WILL BE RANDOMIZED.

    OTHERWISE, THEY WILL REMAIN
    IN THEIR DEFAULT LOCATIONS.

    SHOULD THE OPTION
    BE SET TO "MANDATORY",

    DEFEATING THESE CHALLENGES
    WILL BE REQUIRED TO PROGRESS.

    (If you don't choose "Mantleless" for the next option,)
    (The Shadow Mantle will also be included as a mandatory boss.)"""

    display_name = "Randomize Secret Bosses"
    option_false = 0
    option_true = 1
    option_mandatory = 2
    default = option_false


class RandomizeSecretBossesOptions(StrEnum):
    false = "false"
    true = "true"
    mandatory = "mandatory"


class RandomizeMANTLE(Choice):
    """
    CHECKS RECIEVED
    IN THE ORIGINAL GAME
    OF THE THIRD CHAPTER
    WILL BE RANDOMIZED.

    OTHERWISE, THEY WILL REMAIN
    IN THEIR DEFAULT LOCATIONS.

    SHOULD THE OPTION
    BE SET TO "MANTLELESS",

    THE CHECKS OF THE ORIGINAL GAME
    WILL STILL BE RANDOMIZED,

    HOWEVER

    CHECK LOCATIONS SPECIFICALLY
    LOCKED BEHIND DEFEATING THE MANTLE
    WILL BE REMOVED.

    (So basically, if you choose "Mantleless", the game's still randomized, you just won't have to fight the Mantle.)
    (You can still get the items normally locked behind the boss fight from other checks, though.)
    (And of course, this only applies if you play Chapter 3.)"""

    display_name = "Randomize MANTLE"
    option_false = 0
    option_true = 1
    option_mantleless = 2
    default = option_false


class RandomizeMANTLEOptions(StrEnum):
    false = "false"
    true = "true"
    mantleless = "mantleless"


class IncludeShadowMantle(Toggle):
    """
    THE SHADOW MANTLE WILL BE
    IN THE ITEM POOL
    OF THE THIRD CHAPTER.

    SHOULD THE OPTION
    BE SET TO "FALSE",

    THE SHADOW MANTLE WILL
    BE REMOVED ENTIRELY

    AND THE SHADOW MANTLE WILL NOT
    BE IN LOGIC FOR THE DUEL
    WITH THE KNIGHT.

    (Of course, this only applies if you play Chapter 3.)"""

    display_name = "Include Shadow Mantle"
    default = 1


class IncludeTraps(Choice):
    """
    SOME CHECKS RECIEVED
    WILL ACTUALLY BE TRAPS.


    SHOULD THE OPTION
    BE SET TO "ALL TRAPS",

    THE JUNK POOL WILL
    BE ENTIRELY REPLACED
    BY TRAPS."""

    display_name = "Include Traps"
    option_false = 0
    option_true = 1
    option_all_traps = 2
    default = option_false


class IncludeTRank(Choice):
    """
    GETTING THE HIGHEST RANK
    OF THE THIRD CHAPTER
    WILL BE EXPECTED.

    (Of course, this only applies if you play Chapter 3.)"""

    display_name = "Include T Rank"
    option_false = 0
    option_true = 1
    option_excluded_from_logic = 2
    default = option_false


class IncludeTRankOptions(StrEnum):
    false = "false"
    true = "true"
    excluded_from_logic = "excluded_from_logic"


class ItemBalancing(Toggle):
    """
    IF AN ITEM IS
    OBTAINED EARLY,

    ITS POWER WILL
    BE SCALED DOWN.

    (For example, Chapter 4's AbsorbAx in chapter 1 will only give +3 attack instead of +8.)"""

    display_name = "ItemBalancing"
    default = 0

class IncludeHiddenItems(Toggle):
    """
    RANDOMIZES ITEMS
    THAT ARE CONSIDERABLY MORE
    DIFFICULT TO FIND
    OR TEDIOUS TO OBTAIN.

    OTHERWISE, THEY WILL REMAIN
    IN THEIR DEFAULT LOCATIONS.

    (Examples:)
    - (The Golden Prizes in Chapter 3)
    - (The Eggs)
    - (Items Needed for Secret Bosses)
    - (Dog Dollars)
    - (Moss)"""

    display_name = "Randomize Grindy/Hidden Items"
    default = 0


class IncludeChapter1(Toggle):
    """DO YOU WISH
    TO PLAY CHAPTER 1?"""

    display_name = "Include Chapter 1"
    default = 1


class IncludeChapter2(Toggle):
    """
    DO YOU WISH
    TO PLAY CHAPTER 2?"""

    display_name = "Include Chapter 2"
    default = 1


class IncludeChapter3(Toggle):
    """
    DO YOU WISH
    TO PLAY CHAPTER 3?"""

    display_name = "Include Chapter 3"
    default = 1


class IncludeChapter4(Toggle):
    """
    DO YOU WISH
    TO PLAY CHAPTER 4?"""

    display_name = "Include Chapter 4"
    default = 1


class MacGuffinChapter1(Range):
    """
    A NEW ROADBLACK WILL
    APPEAR BEFORE THE
    FINAL BOSS OF CHAPTER 1

    THIS OPTION DETERMINES
    HOW MANY OF THESE ITEMS
    WILL BE REQUIRED
    TO PROGRESS.

    (King-Shaped Key Pieces)
    """

    display_name = "Macguffin Chapter 1 Amount"
    default = 3
    range_start = 0
    range_end = 10


class MacGuffinChapter2(Range):
    """
    A NEW ROADBLACK WILL
    APPEAR BEFORE THE
    FINAL BOSS OF CHAPTER 2

    THIS OPTION DETERMINES
    HOW MANY OF THESE ITEMS
    WILL BE REQUIRED
    TO PROGRESS.

    (KeyGen 2 Segments)
    """

    display_name = "Macguffin Chapter 2 Amount"
    default = 3
    range_start = 0
    range_end = 10


class MacGuffinChapter3(Range):
    """
    A NEW ROADBLACK WILL
    APPEAR BEFORE THE
    FINAL BOSS OF CHAPTER 3

    THIS OPTION DETERMINES
    HOW MANY OF THESE ITEMS
    WILL BE REQUIRED
    TO PROGRESS.

    (Remote Batteries)
    """

    display_name = "Macguffin Chapter 3 Amount"
    default = 3
    range_start = 0
    range_end = 10


class MacGuffinChapter4(Range):
    """
    A NEW ROADBLACK WILL
    APPEAR BEFORE THE
    FINAL BOSS OF CHAPTER 4

    THIS OPTION DETERMINES
    HOW MANY OF THESE ITEMS
    WILL BE REQUIRED
    TO PROGRESS.

    (Combination Lock Digits)
    """

    display_name = "Macguffin Chapter 4 Amount"
    default = 3
    range_start = 0
    range_end = 10


class MacGuffinExtra(Range):
    """
    Amount of extra macfuffins added in the item pool that are not required to progress.
    """

    display_name = "Extra MacGuffin Amount"
    default = 1
    range_start = 0
    range_end = 5


class DeathLink(Toggle):
    """
    YOUR FAILURE
    CAUSES THE FAILURE
    OF EVERYONE
    WHO HAS ENABLED
    THIS OPTION.

    TO COMPLIMENT,
    THE REVERSE
    IS TRUE AS WELL."""

    display_name = "Death Link"
    default = 0


class ProgressionBalancing(NamedRange):
    """
    ATTEMPTS TO BALANCE
    THE PROGRESSION
    OF YOUR ITEMS.

    SETTING THE VALUE LOWER
    WILL RESULT IN MORE WAITING
    TO RECIEVE ITEMS.

    SETTING THE VALUE HIGHER
    WILL RESULT IN LESS WAITING
    TO RECIEVE ITEMS.
    """

    default = 50
    range_start = 0
    range_end = 99
    display_name = "Progression Balancing"
    rich_text_doc = True
    special_range_names = {
        "disabled": 0,
        "normal": 50,
        "extreme": 99,
    }


class Accessibility(Choice):
    """
    SETS THE RULES
    FOR THE ABILITY
    TO REACH ALL ITEMS.

    **Full:** GUARANTEES THAT ALL ITEMS CAN BE OBTAINED.

    **Minimal:** GUARANTEES ONLY WHAT IS NECESSARY, BUT NO MORE.
    """

    display_name = "Accessibility"
    rich_text_doc = True
    option_full = 0
    option_minimal = 2
    alias_none = 2
    alias_locations = 0
    alias_items = 0
    default = 0


filler_weight_range_names = {"common": 50, "uncommon": 25, "rare": 10, "very rare": 5, "extremely rare": 1}


class FillerHealingWeight(NamedRange):
    """
    DETERMINES HOW OFTEN
    COMMON HEALING ITEMS WILL APPEAR
    COMPARED TO OTHERS ITEMS.

    REGARDLESS OF THIS SETTING,
    EACH WILL BE GUARANTEED
    TO APPEAR AT LEAST ONCE.
    """

    display_name = "Healing Items Weights"
    range_start = 0
    range_end = 99
    default = filler_weight_range_names["common"]
    rich_text_doc = True
    special_range_names = filler_weight_range_names


class FillerCurrencyWeight(NamedRange):
    """
    DETERMINES HOW OFTEN
    ALL CURRENCIES WILL APPEAR
    COMPARED TO OTHERS ITEMS.

    REGARDLESS OF THIS SETTING,
    EACH AMOUNT WILL BE GUARANTEED
    TO APPEAR AT LEAST ONCE.
    """

    display_name = "Currency Weights"
    range_start = 0
    range_end = 99
    default = filler_weight_range_names["uncommon"]
    rich_text_doc = True
    special_range_names = filler_weight_range_names


class TrapWeight(NamedRange):
    """
    DETERMINES HOW OFTEN
    TRAPS WILL APPEAR
    COMPARED TO OTHERS ITEMS.

    REGARDLESS OF THIS SETTING,
    EACH TRAP WILL BE GUARANTEED
    TO APPEAR AT LEAST ONCE.
    """

    display_name = "(Coming Soon) Trap Weights"
    range_start = 0
    range_end = 99
    default = filler_weight_range_names["uncommon"]
    rich_text_doc = True
    special_range_names = filler_weight_range_names


class FillerArmorWeight(NamedRange):
    """
    DETERMINES HOW OFTEN
    ARMOR ITEMS WILL APPEAR
    COMPARED TO OTHERS ITEMS.

    REGARDLESS OF THIS SETTING,
    EACH WILL BE GUARANTEED
    TO APPEAR AT LEAST ONCE.
    """

    display_name = "Armors Weights"
    range_start = 0
    range_end = 99
    default = filler_weight_range_names["rare"]
    rich_text_doc = True
    special_range_names = filler_weight_range_names


class FillerTensionWeight(NamedRange):
    """
    DETERMINES HOW OFTEN
    TENSION ITEMS WILL APPEAR
    COMPARED TO OTHERS ITEMS.

    REGARDLESS OF THIS SETTING,
    EACH WILL BE GUARANTEED
    TO APPEAR AT LEAST ONCE.
    """

    display_name = "Tension Items Weights"
    range_start = 0
    range_end = 99
    default = filler_weight_range_names["very rare"]
    rich_text_doc = True
    special_range_names = filler_weight_range_names


class FillerSMILEWeight(NamedRange):
    """
    DETERMINES HOW OFTEN
    IT WILL SMILE.

    REGARDLESS OF THIS SETTING,
    IT WILL BE GUARANTEED
    TO SMILE AT LEAST ONCE.

    (SMILE only sends you a silly message.)
    
    (...Right?)
    """

    display_name = "SMILE Weight"
    range_start = 0
    range_end = 99
    default = filler_weight_range_names["extremely rare"]
    rich_text_doc = True
    special_range_names = filler_weight_range_names


class ProgressiveKrisWeapons(Toggle):
    """
    THE WEAPONS RECEIVED
    FOR THE CAGE
    WILL BE IN SEQUENTIAL ORDER
    OF RISING POWER.
    """

    display_name = "(COMING SOON) Progressive Kris Weapons"
    default = 0


class ProgressiveSusieWeapons(Toggle):
    """
    THE WEAPONS RECEIVED
    FOR THE GIRL
    WILL BE IN SEQUENTIAL ORDER
    OF RISING POWER.
    """

    display_name = "(COMING SOON) Progressive Susie Weapons"
    default = 0


class ProgressiveRalseiWeapons(Toggle):
    """
    THE WEAPONS RECEIVED
    FOR THE PRINCE
    WILL BE IN SEQUENTIAL ORDER
    OF RISING POWER.
    """

    display_name = "(COMING SOON) Progressive Ralsei Weapons"
    default = 0


class ProgressiveNoelleWeapons(Toggle):
    """
    THE FORBIDDEN RINGS
    WILL BE IN SEQUENTIAL ORDER
    OF RISING POWER.
    """

    display_name = "(COMING SOON) Progressive Noelle Weapons"


class IncludeUnusedItems(Choice):
    """
    CERTAIN ITEMS ARE
    NOT NORMALLY PRESENT.

    WILL THEY NOW
    BE WITH THE REST?
    
    (EverybodyWeapon is pretty over-powered, and it's probably for testing purposes.)
    (Set this option to "True Without EverybodyWeapon" if you'd rather not have it.)
    """

    display_name = "Include Unused Items"
    option_false = 0
    option_true = 1
    option_true_without_everybodyweapon = 2
    default = option_false


class IncludeUnusedItemsOptions(StrEnum):
    false = "false"
    true = "true"
    true_without_everybodyweapon = "true without everybodyweapon"


class IncludeMike(Choice):
    """
    WILL THE DEFEAT
    OF THE MICROPHONE
    AS WELL AS THEIR GAMES
    COUNT AS CHECK LOCATIONS?
    """

    display_name = "(COMING SOON) Include Mike"
    option_false = 0
    option_battle_only = 1
    option_battle_and_games = 2
    default = option_false


class IncludeMikeOptions(StrEnum):
    false = "false"
    battle_only = "battle_only"
    battle_and_games = "battle_and_games"


deltarune_option_groups = [
    OptionGroup("Chapters", [RandomizeChapters, IncludeChapter1, IncludeChapter2, IncludeChapter3, IncludeChapter4]),
    OptionGroup(
        "Fillers",
        [
            FillerHealingWeight,
            FillerCurrencyWeight,
            TrapWeight,
            FillerArmorWeight,
            FillerTensionWeight,
            FillerSMILEWeight,
        ],
    ),
    OptionGroup(
        "Goal",
        [
            ChosenRoute,
            MacGuffinChapter1,
            MacGuffinChapter2,
            MacGuffinChapter3,
            MacGuffinChapter4,
            MacGuffinExtra,
            RandomizeSecretBosses,
            RandomizeMANTLE,
        ],
    ),
    OptionGroup(
        "Items",
        [
            IncludeShadowMantle,
            IncludeHiddenItems,
            IncludeUnusedItems,
            ProgressiveKrisWeapons,
            ProgressiveSusieWeapons,
            ProgressiveRalseiWeapons,
            ProgressiveNoelleWeapons,
        ],
    ),
    OptionGroup("Locations", [IncludeTRank, IncludeMike]),
]


@dataclass
class DeltaruneOptions(PerGameCommonOptions):
    progression_balancing: ProgressionBalancing
    accessibility: Accessibility
    include_chapter_1: IncludeChapter1
    include_chapter_2: IncludeChapter2
    include_chapter_3: IncludeChapter3
    include_chapter_4: IncludeChapter4
    randomize_chapters: RandomizeChapters
    chosen_route: ChosenRoute
    item_balancing: ItemBalancing
    macguffin_chapter_1: MacGuffinChapter1
    macguffin_chapter_2: MacGuffinChapter2
    macguffin_chapter_3: MacGuffinChapter3
    macguffin_chapter_4: MacGuffinChapter4
    macguffin_extra: MacGuffinExtra
    randomize_secret_bosses: RandomizeSecretBosses
    randomize_mantle: RandomizeMANTLE
    include_shadow_mantle: IncludeShadowMantle
    include_t_rank: IncludeTRank
    include_hidden_items: IncludeHiddenItems
    include_unused_items: IncludeUnusedItems
    death_link: DeathLink
    filler_healing_weight: FillerHealingWeight
    filler_currency_weight: FillerCurrencyWeight
    trap_weight: TrapWeight
    filler_armor_weight: FillerArmorWeight
    filler_tension_weight: FillerTensionWeight
    filler_smile_weight: FillerSMILEWeight
    progressive_kris_weapons: ProgressiveKrisWeapons
    progressive_susie_weapons: ProgressiveSusieWeapons
    progressive_ralsei_weapons: ProgressiveRalseiWeapons
    progressive_noelle_weapons: ProgressiveNoelleWeapons
    include_mike: IncludeMike

#    include_traps: IncludeTraps
