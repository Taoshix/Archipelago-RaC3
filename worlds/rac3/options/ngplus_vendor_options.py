"""This module contains options for New Game Plus purchase locations"""

from Options import Toggle
from worlds.rac3.constants.options import RAC3OPTION


class NGPlusVendor(Toggle):
    """
    Adds Mega weapon vendor locations once the corresponding weapon reaches V5.
    If weapon vendors are enabled, this option also adds the RY3N0 as a vendor location.
    """
    display_name = RAC3OPTION.NGPLUS_VENDOR
