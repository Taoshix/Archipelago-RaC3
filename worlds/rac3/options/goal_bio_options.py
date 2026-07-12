"""This module contains options for if defeating the biobliterator is required to goal"""

from Options import Toggle
from worlds.rac3.constants.options import RAC3OPTION


class GoalBio(Toggle):
    """
    Determines if defeating the Biobliterator is required to goal
    --------------------------------------------------------------------------------------
    Off:    Biobliterator is not required, Goal is triggered the instant all other conditions are met
    On:     Biobliterator is required, it is the final goal that is unlocked after all other conditions have been met
    ---------------------------------------------------------------------------------------
    """
    display_name = RAC3OPTION.GOAL_BIO
