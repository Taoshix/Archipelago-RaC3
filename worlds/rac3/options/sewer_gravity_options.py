"""This module contains options for enabling enhanced gravity in the sewer"""

from Options import Toggle
from worlds.rac3 import RAC3OPTION


class SewerChargeGravity(Toggle):
    """
    Determines if it is possible to use charge boots and run up walls in the sewer.
    ------------------------------------------------------------------------------
    Yes: If the player has both the charge boots and gravity boots, they will be able to use both at once in the sewer.
    No:  Vanilla behavior, the player will not be able to use charge boots and run up walls in the sewer at once.
    ------------------------------------------------------------------------------
    Warning: The game was not designed to allow the player to use charge boots and run up walls in the sewer at once.
    This makes EVERYTHING a "gravity ramp" so expect to see some weird behavior.
    """
    display_name = RAC3OPTION.SEWER_CHARGE_GRAVITY
