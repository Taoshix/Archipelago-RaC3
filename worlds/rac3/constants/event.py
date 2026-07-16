"""This module contains constant strings for events in RaC3"""


class RAC3EVENT:
    """Event name strings"""
    FLORANA_QWARK = ("Florana: Qwark Fight", "Defeat Qwark")
    FLORANA_COMPLETE = ("Florana: Completed", "Florana Completed")
    PHOENIX_MUSEUM = ("Phoenix: Collect All Trophies", "Insomniac Museum Teleporter")
    MARCADIA_COMPLETE = ("Marcadia: Completed", "Marcadia Completed")
    AN_PRIZE = ("Annihilation Nation: Win Grand Prize Bout", "Win Grand Prize Bout")
    AN_TWO = ("Annihilation Nation: The Terrible Two Fight", "Defeat the Terrible Two")
    AN_SCORPIO = ("Annihilation Nation: Scorpio Fight", "Defeat Scorpio")
    AN_QWARK = ("Annihilation Nation: Qwarktastic Battle", "Win Qwarktastic Battle")
    AN_COMPLETE = ("Annihilation Nation: Completed", "Annihilation Nation Completed")
    AQUATOS_COMPLETE = ("Aquatos: Completed", "Aquatos Completed")
    NOID_BOSS = ("Tyhrranosis: Momma Tyhrranoid Fight", "Defeat Momma Tyhrranoid")
    TYHRRANOSIS_COMPLETE = ("Tyhrranosis: Completed", "Tyhrranosis Completed")
    DAXX_WARSHIP = ("Daxx: Warship Fight", "Defeat Warship")
    DAXX_COMPLETE = ("Daxx: Completed", "Daxx Completed")
    OBANI_GEMINI_COMPLETE = ("Obani Gemini: Completed", "Obani Gemini Completed")
    BLACKWATER_CITY_COMPLETE = ("Blackwater City: Completed", "Blackwater City Completed")
    HOLOSTAR_TALOS = ("Holostar: Terror of Talos Fight", "Defeat Terror of Talos")
    HOLOSTAR_COMPLETE = ("Holostar: Completed", "Holostar Completed")
    DRACO_GEARS = ("Obani Draco: Courtney Gears Fight", "Defeat Courtney Gears")
    OBANI_DRACO_COMPLETE = ("Obani Draco: Completed", "Obani Draco Completed")
    ZELDRIN_STARPORT_COMPLETE = ("Zeldrin Starport: Completed", "Zeldrin Starport Completed")
    METROPOLIS_KLUNK = ("Metropolis: Klunk Fight", "Defeat Klunk")
    METROPOLIS_COMPLETE = ("Metropolis: Completed", "Metropolis Completed")
    CRASH_SITE_COMPLETE = ("Crash Site: Completed", "Crash Site Completed")
    ARIDIA_COMPLETE = ("Aridia: Completed", "Aridia Completed")
    HIDEOUT_QWARK = ("Qwarks Hideout: Phoenix is under attack", "Phoenix Assault Access")
    HIDEOUT_COMPLETE = ("Qwarks Hideout: Completed", "Qwarks Hideout Completed")
    KOROS_COMPLETE = ("Koros: Completed", "Koros Completed")


ALL_PLANETS: list[str] = [
    RAC3EVENT.FLORANA_COMPLETE[1],
    RAC3EVENT.MARCADIA_COMPLETE[1],
    RAC3EVENT.AN_COMPLETE[1],
    RAC3EVENT.AQUATOS_COMPLETE[1],
    RAC3EVENT.TYHRRANOSIS_COMPLETE[1],
    RAC3EVENT.DAXX_COMPLETE[1],
    RAC3EVENT.OBANI_GEMINI_COMPLETE[1],
    RAC3EVENT.BLACKWATER_CITY_COMPLETE[1],
    RAC3EVENT.HOLOSTAR_COMPLETE[1],
    RAC3EVENT.OBANI_DRACO_COMPLETE[1],
    RAC3EVENT.ZELDRIN_STARPORT_COMPLETE[1],
    RAC3EVENT.METROPOLIS_COMPLETE[1],
    RAC3EVENT.CRASH_SITE_COMPLETE[1],
    RAC3EVENT.ARIDIA_COMPLETE[1],
    RAC3EVENT.HIDEOUT_COMPLETE[1],
    RAC3EVENT.KOROS_COMPLETE[1],
]

ALL_GOALS: list[str] = [
    RAC3EVENT.FLORANA_QWARK[0],
    RAC3EVENT.FLORANA_COMPLETE[0],
    RAC3EVENT.PHOENIX_MUSEUM[0],
    RAC3EVENT.MARCADIA_COMPLETE[0],
    RAC3EVENT.AN_PRIZE[0],
    RAC3EVENT.AN_TWO[0],
    RAC3EVENT.AN_SCORPIO[0],
    RAC3EVENT.AN_QWARK[0],
    RAC3EVENT.AN_COMPLETE[0],
    RAC3EVENT.AQUATOS_COMPLETE[0],
    RAC3EVENT.NOID_BOSS[0],
    RAC3EVENT.TYHRRANOSIS_COMPLETE[0],
    RAC3EVENT.DAXX_WARSHIP[0],
    RAC3EVENT.DAXX_COMPLETE[0],
    RAC3EVENT.OBANI_GEMINI_COMPLETE[0],
    RAC3EVENT.BLACKWATER_CITY_COMPLETE[0],
    RAC3EVENT.HOLOSTAR_TALOS[0],
    RAC3EVENT.HOLOSTAR_COMPLETE[0],
    RAC3EVENT.DRACO_GEARS[0],
    RAC3EVENT.OBANI_DRACO_COMPLETE[0],
    RAC3EVENT.ZELDRIN_STARPORT_COMPLETE[0],
    RAC3EVENT.METROPOLIS_KLUNK[0],
    RAC3EVENT.METROPOLIS_COMPLETE[0],
    RAC3EVENT.CRASH_SITE_COMPLETE[0],
    RAC3EVENT.ARIDIA_COMPLETE[0],
    RAC3EVENT.HIDEOUT_QWARK[0],
    RAC3EVENT.HIDEOUT_COMPLETE[0],
    RAC3EVENT.KOROS_COMPLETE[0],
]
