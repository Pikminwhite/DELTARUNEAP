from ..Items import ItemIDs, ItemData, ConditionalItemData, generic_create_items, generic_get_filler_items, DeltaruneItem, ItemGroups
from ..cross_chapter.Items import CCItems
from typing import TYPE_CHECKING
from BaseClasses import ItemClassification
from enum import StrEnum

if TYPE_CHECKING: from .. import DeltaruneWorld

class Ch5Items(StrEnum):
  chapter_5_unlock = "This is where I would put my Chapter 5 Unlock... IF I HAD ONE!"
  
  egg = "CH5 Egg"
  
  # Healing
    
  # Armors
  
  # Weapons
  
  # Macguffin
  
chapter5_macguffin_item = ""
  
chapter5_items = {
}

chapter5_conditional_items = {
  Ch5Items.chapter_5_unlock.value:  ConditionalItemData(ItemIDs.chapter_5_unlock.value, ItemClassification.progression, lambda world: world.is_chapters_randomized(), [ItemGroups.region_blockers]),
  # Ch5Items.egg.value:           ConditionalItemData(ItemIDs.chapter_5_egg.value,  ItemClassification.useful, lambda world: world.is_hidden_items_randomized(), [ItemGroups.eggs]),
}

def create_items(world: "DeltaruneWorld") -> list[DeltaruneItem]:
  return generic_create_items(world, chapter5_items, chapter5_conditional_items)
  
def get_filler_items(world: "DeltaruneWorld"):
  return generic_get_filler_items(world, chapter5_items, chapter5_conditional_items)