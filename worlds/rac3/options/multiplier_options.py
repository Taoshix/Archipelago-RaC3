"""Options for in-game bolt and XP rewards."""

from Options import Choice, Toggle
from worlds.rac3.constants.options import RAC3OPTION


class BoltAndXPMultiplier(Choice):
    """
    Determines what your base bolt and xp multiplier will be set to,
    recommended to use x8 if you're looking to do a sync.
    """
    display_name = RAC3OPTION.BOLT_AND_XP_MULTIPLIER
    option_x1 = 0
    option_x2 = 1
    option_x4 = 2
    option_x8 = 3
    option_x16 = 4
    default = 2


class RemoveBoltDiminishingReturns(Toggle):
    """Keep bolt rewards at 100% when revisiting planets."""
    display_name = RAC3OPTION.REMOVE_BOLT_DIMINISHING_RETURNS


class RemoveXPDiminishingReturns(Toggle):
    """Keep XP rewards at 100% when revisiting planets."""
    display_name = RAC3OPTION.REMOVE_XP_DIMINISHING_RETURNS
