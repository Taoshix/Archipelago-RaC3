"""Option for removing XP revisit diminishing returns."""

from Options import Toggle
from worlds.rac3.constants.options import RAC3OPTION


class RemoveXPDiminishingReturns(Toggle):
    """Keep XP gains at 100% when revisiting planets."""
    display_name = RAC3OPTION.REMOVE_XP_DIMINISHING_RETURNS
