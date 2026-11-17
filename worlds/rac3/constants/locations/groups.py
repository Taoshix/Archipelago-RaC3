"""Display labels and abbreviations for Galactic Map location counts."""

from worlds.rac3.constants.locations.tags import RAC3TAG
from worlds.rac3.constants.options import RAC3OPTION


class RAC3LOCATIONGROUP:
    """String constants for location groups and their compact display names."""

    STORY = "Story"
    GENERAL = "General"
    VENDOR = "Vendor"
    COLLECTIBLES = "Collectibles"
    SKILL_POINTS = "Skill Points"
    VR = "VR"
    VID_COMICS = "Vid-Comics"
    SEWERS = "Sewers"
    RANGERS = "Rangers"
    LDF = "LDF"
    GAUNTLET = "Gauntlet"
    ARENA = "Arena"

    SHORT_NAMES = {
        GENERAL: "Gen",
        COLLECTIBLES: "Coll",
        SKILL_POINTS: "SP",
        VID_COMICS: "Comics",
    }
    SHORTER_NAMES = {
        **SHORT_NAMES,
        VID_COMICS: "VC",
        GAUNTLET: "Gaunt",
        VENDOR: "Vend",
    }
