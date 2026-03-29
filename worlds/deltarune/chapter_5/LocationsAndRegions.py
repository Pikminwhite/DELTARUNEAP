from BaseClasses import Location
from enum import StrEnum
from ..Locations import LocationIDs, LocationData, ConditionalLocationData, LocationGroups
from ..Regions import generic_create_regions, fusion_access_region
from typing import TYPE_CHECKING

if TYPE_CHECKING: from .. import DeltaruneWorld

class Ch5Locations(StrEnum):
  castle_town_top_chef_gift             = "CH5: Castle Town - Top Chef Gift"
  
  # Recruits
  
  # Lost

class Ch5Regions(StrEnum):
  chapter_5                   = "Chapter 5"

class Ch5Entrances(StrEnum):
  unknown_entrance                = "CH5: "

chapter5_end_region = Ch5Regions.chapter_5.value

chapter5_locations = {
}

chapter5_conditional_locations = {
  # Recruits
  
  # Losts
}

chapter5_regions = [
  (Ch5Regions.chapter_5.value,                  []),
]

chapter5_mandatory_connections = [
]

def create_regions(world: "DeltaruneWorld"):
  generic_create_regions(world, chapter5_regions, chapter5_locations, chapter5_conditional_locations)
