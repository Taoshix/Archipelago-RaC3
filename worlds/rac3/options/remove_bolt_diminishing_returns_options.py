"""Option for removing bolt revisit diminishing returns."""

from Options import Toggle
from worlds.rac3.constants.options import RAC3OPTION


class RemoveBoltDiminishingReturns(Toggle):
    """Keep bolt gains at 100% when revisiting planets."""
    display_name = RAC3OPTION.REMOVE_BOLT_DIMINISHING_RETURNS
