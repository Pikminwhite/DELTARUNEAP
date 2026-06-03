from rule_builder.options import OptionFilter
from rule_builder.rules import Has
from worlds.deltarune.Options import UnlockCharacters, UnlockFunGangActions
from worlds.deltarune.Items import items, ItemIDs

have_kris = Has(items[ItemIDs.kris]) | OptionFilter(UnlockCharacters, UnlockCharacters.option_true, operator="ne")
have_ralsei = Has(items[ItemIDs.ralsei]) | OptionFilter(UnlockCharacters, UnlockCharacters.option_false, operator="eq")
have_susie = Has(items[ItemIDs.susie]) | OptionFilter(UnlockCharacters, UnlockCharacters.option_false, operator="eq")
have_noelle = Has(items[ItemIDs.noelle]) | OptionFilter(UnlockCharacters, UnlockCharacters.option_false, operator="eq")

have_kris_or_susie = have_kris | have_susie
have_kris_or_ralsei = have_kris | have_ralsei
have_kris_susie_or_ralsei = have_kris | have_susie | have_ralsei
have_kris_susie_and_ralsei = have_kris & have_susie & have_ralsei

have_actions = Has(items[ItemIDs.s_r_n_actions]) | OptionFilter(UnlockFunGangActions, 0)
have_thornring = Has(items[ItemIDs.thornring]) | Has(items[ItemIDs.progressive_noelle_weapons], 2)

can_snowgrave = have_noelle & have_thornring
