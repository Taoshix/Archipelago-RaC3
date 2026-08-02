"""This module contains options for titanium bolt locations"""

from Options import Choice
from worlds.rac3.constants.options import RAC3OPTION


class ObjectSanity(Choice):
    """
    Determines whether Objects are locations in the world.
    -----------------------------------------------------------------------------------------------
    Disabled: No objects are locations.
    Enabled:  Objects are added as locations. 
    -----------------------------------------------------------------------------------------------
    Currently only Obani Draco has objects as locations.
    """
    display_name = RAC3OPTION.OBJECT_SANITY
    option_disabled = 0
    option_enabled = 1
    default = 0
