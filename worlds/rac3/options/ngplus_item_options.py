"""This module contains options for New Game Plus items in the item pool"""

from Options import Toggle
from worlds.rac3.constants.options import RAC3OPTION


class NGPlusItems(Toggle):
    """
    Adds the RY3N0 to the item pool.
    With regular weapons, each weapon gets a Mega Upgrade item that takes it from V5 to V6.
    With progressive weapons, the 6th progressive weapon takes the weapon from V5 to V6.
    """
    display_name = RAC3OPTION.NGPLUS_ITEMS
