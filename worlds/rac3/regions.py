"""This module provides handling for location regions"""

from typing import TYPE_CHECKING

from BaseClasses import CollectionRule, Location, Region
from worlds.rac3.constants.data.location import LOCATION_FROM_AP_CODE, RAC3_LOCATION_DATA_TABLE, RAC3LOCATIONDATA
from worlds.rac3.constants.event import RAC3EVENT
from worlds.rac3.constants.items import RAC3ITEM
from worlds.rac3.constants.locations.general import RAC3LOCATION
from worlds.rac3.constants.locations.nanotech import NANOTECH_OPTION_TO_MOD, RAC3NANOTECH
from worlds.rac3.constants.locations.sewers import RAC3SEWER
from worlds.rac3.constants.locations.skillpoints import RAC3SKILLPOINT
from worlds.rac3.constants.locations.tags import RAC3TAG
from worlds.rac3.constants.locations.tbolts import RAC3TBOLT
from worlds.rac3.constants.locations.trophies import RAC3TROPHY
from worlds.rac3.constants.options import RAC3OPTION
from worlds.rac3.constants.player_type import RAC3PLAYERTYPE
from worlds.rac3.constants.region import RAC3REGION, REGIONS_WITH_LOCATIONS
from worlds.rac3.constants.shortcuts import RAC3SHORTCUTS
from worlds.rac3.items import GameItem
from worlds.rac3.rac3options import RaC3Options
from worlds.rac3.rules import all_locations

if TYPE_CHECKING:
    from worlds.rac3.world import RaC3World


class GameLocation(Location):
    """Rac3 game location"""
    game = RAC3OPTION.GAME_TITLE_FULL


all_nanotech: list[str] = [getattr(RAC3NANOTECH, f"LEVEL_{level}") for level in range(11, 201)]


def should_skip_nanotech_location(location: str, options: type[RaC3Options]) -> bool:
    """
    Determine if a nanotech location should be skipped based on options.

    :param location: Nanotech location name, must end with the value
    :param options: RaC3Options of current generation
    :return: True if the location should not be created
    """
    nanotech_level = int(location.split()[-1])
    if options.nanotech_milestones.value == 0:
        return True
    if nanotech_level > 100 and not options.ngplus_start.value:
        return True
    if nanotech_level > options.nanotech_limitation.value:
        return True

    nanotech_step = NANOTECH_OPTION_TO_MOD.get(options.nanotech_milestones.value, 0)
    if not nanotech_step:
        return True

    return nanotech_level % nanotech_step != 0


def get_nanotech_locations(options: type[RaC3Options]) -> list[str]:
    """
    Get a list of nanotech locations based on the provided options.

    :param options: RaC3Options of current generation
    :return: List of nanotech location names
    """
    return [location for location in all_nanotech if not should_skip_nanotech_location(location, options)]


def should_skip_skill_master(options: type[RaC3Options]) -> bool:
    """
    Determine if the skill master trophy location should be skipped based on options.

    :param options: RaC3Options of current generation
    :return: True if the location should not be created
    """
    if options.skill_points.value < 2:
        return True
    if options.sewer_limitation.value < 100:
        return True
    if options.vidcomics.value == 0:
        return True
    if options.vr_challenges.value == 0:
        return True
    if options.armor_vendor.value == 0:
        return True
    if options.arena.value < 3:
        return True
    if options.rangers.value == 0 or options.rangers.value == 2:
        return True
    return False


every_sewer_crystals: list[str] = [
    RAC3SEWER.TRADE_1,
    RAC3SEWER.TRADE_2,
    RAC3SEWER.TRADE_3,
    RAC3SEWER.TRADE_4,
    RAC3SEWER.TRADE_5,
    RAC3SEWER.TRADE_6,
    RAC3SEWER.TRADE_7,
    RAC3SEWER.TRADE_8,
    RAC3SEWER.TRADE_9,
    RAC3SEWER.TRADE_10,
    RAC3SEWER.TRADE_11,
    RAC3SEWER.TRADE_12,
    RAC3SEWER.TRADE_13,
    RAC3SEWER.TRADE_14,
    RAC3SEWER.TRADE_15,
    RAC3SEWER.TRADE_16,
    RAC3SEWER.TRADE_17,
    RAC3SEWER.TRADE_18,
    RAC3SEWER.TRADE_19,
    RAC3SEWER.TRADE_20,
    RAC3SEWER.TRADE_21,
    RAC3SEWER.TRADE_22,
    RAC3SEWER.TRADE_23,
    RAC3SEWER.TRADE_24,
    RAC3SEWER.TRADE_25,
    RAC3SEWER.TRADE_26,
    RAC3SEWER.TRADE_27,
    RAC3SEWER.TRADE_28,
    RAC3SEWER.TRADE_29,
    RAC3SEWER.TRADE_30,
    RAC3SEWER.TRADE_31,
    RAC3SEWER.TRADE_32,
    RAC3SEWER.TRADE_33,
    RAC3SEWER.TRADE_34,
    RAC3SEWER.TRADE_35,
    RAC3SEWER.TRADE_36,
    RAC3SEWER.TRADE_37,
    RAC3SEWER.TRADE_38,
    RAC3SEWER.TRADE_39,
    RAC3SEWER.TRADE_40,
    RAC3SEWER.TRADE_41,
    RAC3SEWER.TRADE_42,
    RAC3SEWER.TRADE_43,
    RAC3SEWER.TRADE_44,
    RAC3SEWER.TRADE_45,
    RAC3SEWER.TRADE_46,
    RAC3SEWER.TRADE_47,
    RAC3SEWER.TRADE_48,
    RAC3SEWER.TRADE_49,
    RAC3SEWER.TRADE_50,
    RAC3SEWER.TRADE_51,
    RAC3SEWER.TRADE_52,
    RAC3SEWER.TRADE_53,
    RAC3SEWER.TRADE_54,
    RAC3SEWER.TRADE_55,
    RAC3SEWER.TRADE_56,
    RAC3SEWER.TRADE_57,
    RAC3SEWER.TRADE_58,
    RAC3SEWER.TRADE_59,
    RAC3SEWER.TRADE_60,
    RAC3SEWER.TRADE_61,
    RAC3SEWER.TRADE_62,
    RAC3SEWER.TRADE_63,
    RAC3SEWER.TRADE_64,
    RAC3SEWER.TRADE_65,
    RAC3SEWER.TRADE_66,
    RAC3SEWER.TRADE_67,
    RAC3SEWER.TRADE_68,
    RAC3SEWER.TRADE_69,
    RAC3SEWER.TRADE_70,
    RAC3SEWER.TRADE_71,
    RAC3SEWER.TRADE_72,
    RAC3SEWER.TRADE_73,
    RAC3SEWER.TRADE_74,
    RAC3SEWER.TRADE_75,
    RAC3SEWER.TRADE_76,
    RAC3SEWER.TRADE_77,
    RAC3SEWER.TRADE_78,
    RAC3SEWER.TRADE_79,
    RAC3SEWER.TRADE_80,
    RAC3SEWER.TRADE_81,
    RAC3SEWER.TRADE_82,
    RAC3SEWER.TRADE_83,
    RAC3SEWER.TRADE_84,
    RAC3SEWER.TRADE_85,
    RAC3SEWER.TRADE_86,
    RAC3SEWER.TRADE_87,
    RAC3SEWER.TRADE_88,
    RAC3SEWER.TRADE_89,
    RAC3SEWER.TRADE_90,
    RAC3SEWER.TRADE_91,
    RAC3SEWER.TRADE_92,
    RAC3SEWER.TRADE_93,
    RAC3SEWER.TRADE_94,
    RAC3SEWER.TRADE_95,
    RAC3SEWER.TRADE_96,
    RAC3SEWER.TRADE_97,
    RAC3SEWER.TRADE_98,
    RAC3SEWER.TRADE_99,
    RAC3SEWER.TRADE_100,
    RAC3SEWER.TRADE_101,
    RAC3SKILLPOINT.SEWER_MOTHERLOAD,
]
every_5_sewer_crystals: list[str] = [
    RAC3SEWER.TRADE_5,
    RAC3SEWER.TRADE_10,
    RAC3SEWER.TRADE_15,
    RAC3SEWER.TRADE_20,
    RAC3SEWER.TRADE_25,
    RAC3SEWER.TRADE_30,
    RAC3SEWER.TRADE_35,
    RAC3SEWER.TRADE_40,
    RAC3SEWER.TRADE_45,
    RAC3SEWER.TRADE_50,
    RAC3SEWER.TRADE_55,
    RAC3SEWER.TRADE_60,
    RAC3SEWER.TRADE_65,
    RAC3SEWER.TRADE_70,
    RAC3SEWER.TRADE_75,
    RAC3SEWER.TRADE_80,
    RAC3SEWER.TRADE_85,
    RAC3SEWER.TRADE_90,
    RAC3SEWER.TRADE_95,
    RAC3SEWER.TRADE_100,
    RAC3SKILLPOINT.SEWER_MOTHERLOAD,
]
every_10_sewer_crystals: list[str] = [
    RAC3SEWER.TRADE_10,
    RAC3SEWER.TRADE_20,
    RAC3SEWER.TRADE_30,
    RAC3SEWER.TRADE_40,
    RAC3SEWER.TRADE_50,
    RAC3SEWER.TRADE_60,
    RAC3SEWER.TRADE_70,
    RAC3SEWER.TRADE_80,
    RAC3SEWER.TRADE_90,
    RAC3SEWER.TRADE_100,
    RAC3SKILLPOINT.SEWER_MOTHERLOAD,
]
every_20_sewer_crystals: list[str] = [
    RAC3SEWER.TRADE_20,
    RAC3SEWER.TRADE_40,
    RAC3SEWER.TRADE_60,
    RAC3SEWER.TRADE_80,
    RAC3SEWER.TRADE_100,
    RAC3SKILLPOINT.SEWER_MOTHERLOAD,
]

annihilation_nation_1: list[str] = [
    RAC3TBOLT.NATION_CLIFF,
    RAC3SKILLPOINT.NATION_CAMERA,
    RAC3SKILLPOINT.NATION_FLEE,
    RAC3LOCATION.NATION_TYHRRA_GUISE,
    RAC3LOCATION.NATION_GRAND_PRIZE_BOUT,
    RAC3LOCATION.NATION_THE_TERRIBLE_TWO,
    RAC3LOCATION.NATION_ROBOT_RAMPAGE,
    RAC3LOCATION.NATION_TWO_MINUTE_WARNING,
    RAC3LOCATION.NATION_90_SECONDS,
    RAC3LOCATION.NATION_ONSLAUGHT,
    RAC3LOCATION.NATION_WHIP_IT_GOOD,
    RAC3LOCATION.NATION_HYDRA_N_SEEK,
    RAC3LOCATION.NATION_CHAMPIONSHIP_BOUT,
    RAC3LOCATION.NATION_HEAT_STREET,
    RAC3LOCATION.NATION_CRISPY_CRITTER,
    RAC3LOCATION.NATION_PYRO_PLAYGROUND,
    RAC3LOCATION.NATION_SUICIDE_RUN,
]
annihilation_nation_2: list[str] = [
    RAC3TBOLT.NATION_CLIFF,
    RAC3SKILLPOINT.NATION_CAMERA,
    RAC3SKILLPOINT.NATION_FLEE,
    # These 3 are doable on the second part of the challenges as well
    RAC3SKILLPOINT.NATION_BASH,
    RAC3LOCATION.NATION_MEET_COURTNEY,
    RAC3LOCATION.NATION_INFOBOT_HOLOSTAR,
    RAC3LOCATION.NATION_NINJA_CHALLENGE,
    RAC3LOCATION.NATION_COUNTING_DUCKS,
    RAC3LOCATION.NATION_CYCLING_WEAPONS,
    RAC3LOCATION.NATION_ONE_HIT_WONDER,
    RAC3LOCATION.NATION_TIME_TO_SUCK,
    RAC3LOCATION.NATION_NAPTIME,
    RAC3LOCATION.NATION_MORE_CYCLING_WEAPONS,
    RAC3LOCATION.NATION_DODGE_THE_TWINS,
    RAC3LOCATION.NATION_CHOP_CHOP,
    RAC3LOCATION.NATION_SLEEP_INDUCER,
    RAC3LOCATION.NATION_THE_OTHER_WHITE_MEAT,
    RAC3LOCATION.NATION_CHAMPIONSHIP_BOUT_II,
    RAC3LOCATION.NATION_QWARKTASTIC_BATTLE,
    RAC3LOCATION.NATION_BBQ_BOULEVARD,
    RAC3LOCATION.NATION_MAZE_OF_BLAZE,
    RAC3TBOLT.NATION_PLATFORM,
    RAC3LOCATION.NATION_CREMATION_STATION,
    RAC3LOCATION.NATION_THE_ANNIHILATOR,
]

extra_ranger: list[str] = [
    RAC3LOCATION.TYHRRANOSIS_RANGERS_1,
    RAC3LOCATION.TYHRRANOSIS_RANGERS_2,
    RAC3LOCATION.TYHRRANOSIS_RANGERS_3,
    RAC3LOCATION.TYHRRANOSIS_RANGERS_4,
    RAC3TBOLT.METROPOLIS_RANGERS,
    RAC3LOCATION.METROPOLIS_RANGERS_1,
    RAC3LOCATION.METROPOLIS_RANGERS_2,
    RAC3LOCATION.METROPOLIS_RANGERS_3,
    RAC3LOCATION.METROPOLIS_RANGERS_4,
    RAC3LOCATION.METROPOLIS_RANGERS_5,
    RAC3LOCATION.METROPOLIS_MAP_O_MATIC,
]

veldin_weapons: list[str] = [
    RAC3LOCATION.VELDIN_FIRST_RANGER,
    RAC3LOCATION.VELDIN_SECOND_RANGER,
]

simple_skillpoints: list[str] = [
    RAC3SKILLPOINT.ARIDIA_HANG_TIME,
    RAC3SKILLPOINT.PHOENIX_VR_TRAINING,
    RAC3SKILLPOINT.PHOENIX_ARMOR,
    RAC3SKILLPOINT.PHOENIX_MONKEY,
    RAC3SKILLPOINT.MARCADIA_REFLECT,
    RAC3SKILLPOINT.DAXX_BUGS,
    RAC3SKILLPOINT.NATION_CAMERA,
    RAC3SKILLPOINT.AQUATOS_SUNKEN,
    RAC3SKILLPOINT.TYHRRANOSIS_SHARPSHOOTER,
    RAC3SKILLPOINT.GEMINI_BELT,
    RAC3SKILLPOINT.BLACKWATER_BASH,
    RAC3SKILLPOINT.KOROS_BREAK,
    RAC3SKILLPOINT.METROPOLIS_GOOD_YEAR,
    RAC3SKILLPOINT.CRASH_SITE_AIM_HIGH,
    RAC3SKILLPOINT.ARIDIA_ZAP,
    RAC3SKILLPOINT.HIDEOUT_DAN,
    RAC3SKILLPOINT.COMMAND_CENTER_GERMS,
]


def create_regions(world: "RaC3World"):
    """
    Creates each region and connects them together

    :param world: RaC3World of current generation
    """
    # ----- Introduction Sequence -----#
    menu = create_region(world, RAC3REGION.MENU)
    veldin = create_region_and_connect(world, RAC3REGION.VELDIN, f"{RAC3REGION.MENU} -> {RAC3REGION.VELDIN}", menu)
    if world.options.shortcuts.value.get(RAC3SHORTCUTS.VELDIN_SKIP, False):
        phoenix = create_region_and_connect(world, RAC3REGION.STARSHIP_PHOENIX,
                                            f"{RAC3REGION.MENU} -> {RAC3REGION.STARSHIP_PHOENIX}", menu)
        florana = create_region_and_connect(world, RAC3REGION.FLORANA,
                                            f"{RAC3REGION.STARSHIP_PHOENIX} -> {RAC3REGION.FLORANA}", phoenix)
    else:
        florana = create_region_and_connect(world, RAC3REGION.FLORANA,
                                            f"{RAC3REGION.VELDIN} -> {RAC3REGION.FLORANA}", veldin)
        phoenix = create_region_and_connect(world, RAC3REGION.STARSHIP_PHOENIX,
                                            f"{RAC3REGION.FLORANA} -> {RAC3REGION.STARSHIP_PHOENIX}", florana)

    # ----- Regions within the game -----#
    marcadia = create_region_and_connect(world, RAC3REGION.MARCADIA,
                                         f"{RAC3REGION.STARSHIP_PHOENIX} -> {RAC3REGION.MARCADIA}", phoenix)
    nation = create_region_and_connect(world, RAC3REGION.ANNIHILATION_NATION,
                                       f"{RAC3REGION.STARSHIP_PHOENIX} -> {RAC3REGION.ANNIHILATION_NATION}", phoenix)
    aquatos = create_region_and_connect(world, RAC3REGION.AQUATOS,
                                        f"{RAC3REGION.STARSHIP_PHOENIX} -> {RAC3REGION.AQUATOS}", phoenix)
    tyhrranosis = create_region_and_connect(world, RAC3REGION.TYHRRANOSIS,
                                            f"{RAC3REGION.STARSHIP_PHOENIX} -> {RAC3REGION.TYHRRANOSIS}", phoenix)
    daxx = create_region_and_connect(world, RAC3REGION.DAXX,
                                     f"{RAC3REGION.STARSHIP_PHOENIX} -> {RAC3REGION.DAXX}", phoenix)
    obani = create_region_and_connect(world, RAC3REGION.OBANI_GEMINI,
                                      f"{RAC3REGION.STARSHIP_PHOENIX} -> {RAC3REGION.OBANI_GEMINI}", phoenix)
    blackwater = create_region_and_connect(
        world, RAC3REGION.BLACKWATER_CITY,
        f"{RAC3REGION.STARSHIP_PHOENIX} -> {RAC3REGION.BLACKWATER_CITY}", phoenix)
    holostar = create_region_and_connect(
        world, RAC3REGION.HOLOSTAR_STUDIOS,
        f"{RAC3REGION.STARSHIP_PHOENIX} -> {RAC3REGION.HOLOSTAR_STUDIOS}", phoenix)
    skidd_cutscene = create_region(world, RAC3REGION.SKIDD_CUTSCENE)
    blackwater.connect(skidd_cutscene, f"{RAC3REGION.BLACKWATER_CITY} -> {RAC3REGION.SKIDD_CUTSCENE}")
    holostar.connect(skidd_cutscene, f"{RAC3REGION.HOLOSTAR_STUDIOS} -> {RAC3REGION.SKIDD_CUTSCENE}")
    draco = create_region_and_connect(world, RAC3REGION.OBANI_DRACO,
                                      f"{RAC3REGION.STARSHIP_PHOENIX} -> {RAC3REGION.OBANI_DRACO}", phoenix)
    starport = create_region_and_connect(world, RAC3REGION.ZELDRIN_STARPORT,
                                         f"{RAC3REGION.STARSHIP_PHOENIX} -> {RAC3REGION.ZELDRIN_STARPORT}", phoenix)
    metropolis = create_region_and_connect(world, RAC3REGION.METROPOLIS,
                                           f"{RAC3REGION.STARSHIP_PHOENIX} -> {RAC3REGION.METROPOLIS}", phoenix)
    crash_site = create_region_and_connect(world, RAC3REGION.CRASH_SITE,
                                           f"{RAC3REGION.STARSHIP_PHOENIX} -> {RAC3REGION.CRASH_SITE}", phoenix)
    aridia = create_region_and_connect(world, RAC3REGION.ARIDIA,
                                       f"{RAC3REGION.STARSHIP_PHOENIX} -> {RAC3REGION.ARIDIA}", phoenix)
    hideout = create_region_and_connect(world, RAC3REGION.QWARKS_HIDEOUT,
                                        f"{RAC3REGION.STARSHIP_PHOENIX} -> {RAC3REGION.QWARKS_HIDEOUT}", phoenix)
    koros = create_region_and_connect(world, RAC3REGION.KOROS,
                                      f"{RAC3REGION.STARSHIP_PHOENIX} -> {RAC3REGION.KOROS}", phoenix)
    create_region_and_connect(world, RAC3REGION.COMMAND_CENTER,
                              f"{RAC3REGION.STARSHIP_PHOENIX} -> {RAC3REGION.COMMAND_CENTER}", phoenix)

    # Victory Location

    # ----- Connecting everything to Starship Phoenix -----#

    # ----- Dummy regions for weapon upgrade organization -----#

    create_region_and_connect(world, RAC3REGION.NANOTECH, f"{RAC3REGION.MENU} -> {RAC3REGION.NANOTECH}", menu)

    create_region_and_connect(world, RAC3REGION.UPGRADES, f"{RAC3REGION.MENU} -> {RAC3REGION.UPGRADES}", menu)

    # New Game Plus

    create_region_and_connect(world, RAC3REGION.NGPLUS, f"{RAC3REGION.STARSHIP_PHOENIX} -> {RAC3REGION.NGPLUS}",
                              phoenix)

    event_create(florana, RAC3EVENT.FLORANA_QWARK, lambda state: state.has_any(
        [RAC3ITEM.HELI_PACK, RAC3ITEM.CLANK, RAC3ITEM.PROGRESSIVE_PACK, RAC3ITEM.CHARGE_BOOTS], world.player))
    event_create(florana, RAC3EVENT.FLORANA_COMPLETE, lambda state: state.has_any(
        [RAC3ITEM.HELI_PACK, RAC3ITEM.CLANK, RAC3ITEM.PROGRESSIVE_PACK, RAC3ITEM.CHARGE_BOOTS], world.player))

    if world.options.goal_museum.value > 0:
        event_create(phoenix, RAC3EVENT.PHOENIX_MUSEUM, lambda state: all_locations(state, world, RAC3TAG.TROPHY, ""))

    event_create(marcadia, RAC3EVENT.MARCADIA_COMPLETE, lambda state: state.has(RAC3ITEM.REFRACTOR, world.player))

    event_create(nation, RAC3EVENT.AN_PRIZE)
    event_create(nation, RAC3EVENT.AN_TWO)
    event_create(nation, RAC3EVENT.AN_SCORPIO, lambda state: state.has(RAC3EVENT.DAXX_WARSHIP[1], world.player))
    event_create(nation, RAC3EVENT.AN_QWARK, (
        lambda state: state.has(RAC3EVENT.DAXX_WARSHIP[1], world.player)
                      and state.has_any([RAC3ITEM.HELI_PACK, RAC3ITEM.THRUSTER_PACK, RAC3ITEM.CLANK,
                                         RAC3ITEM.PROGRESSIVE_PACK, RAC3ITEM.CHARGE_BOOTS], world.player)))
    event_create(nation, RAC3EVENT.AN_COMPLETE,
                 lambda state: state.has(RAC3EVENT.DAXX_WARSHIP[1], world.player) and state.has_any(
                     [RAC3ITEM.HELI_PACK, RAC3ITEM.THRUSTER_PACK, RAC3ITEM.CLANK,
                      RAC3ITEM.PROGRESSIVE_PACK, RAC3ITEM.CHARGE_BOOTS],
                     world.player))

    event_create(aquatos, RAC3EVENT.AQUATOS_COMPLETE)

    event_create(tyhrranosis, RAC3EVENT.NOID_BOSS)
    event_create(tyhrranosis, RAC3EVENT.TYHRRANOSIS_COMPLETE)

    event_create(daxx, RAC3EVENT.DAXX_WARSHIP, lambda state: state.has(RAC3ITEM.HYPERSHOT, world.player))
    event_create(daxx, RAC3EVENT.DAXX_COMPLETE,
                 lambda state: state.has_all([RAC3ITEM.HYPERSHOT, RAC3ITEM.HACKER], world.player))

    event_create(obani, RAC3EVENT.OBANI_GEMINI_COMPLETE, lambda state: state.has(RAC3ITEM.REFRACTOR, world.player))

    event_create(blackwater, RAC3EVENT.BLACKWATER_CITY_COMPLETE)

    event_create(holostar, RAC3EVENT.HOLOSTAR_TALOS)
    event_create(holostar, RAC3EVENT.HOLOSTAR_COMPLETE,
                 lambda state: state.has_all([RAC3ITEM.HYPERSHOT, RAC3ITEM.HACKER], world.player))

    event_create(draco, RAC3EVENT.DRACO_GEARS, lambda state: state.has(RAC3ITEM.GRAV_BOOTS, world.player))
    event_create(draco, RAC3EVENT.OBANI_DRACO_COMPLETE, lambda state: state.has(RAC3ITEM.GRAV_BOOTS, world.player))

    event_create(starport, RAC3EVENT.ZELDRIN_STARPORT_COMPLETE, lambda state: state.has_any(
        [RAC3ITEM.HELI_PACK, RAC3ITEM.THRUSTER_PACK, RAC3ITEM.CLANK, RAC3ITEM.PROGRESSIVE_PACK, RAC3ITEM.CHARGE_BOOTS],
        world.player))

    event_create(metropolis, RAC3EVENT.METROPOLIS_KLUNK,
                 lambda state: state.has_all([RAC3ITEM.GRAV_BOOTS, RAC3ITEM.REFRACTOR], world.player))
    event_create(metropolis, RAC3EVENT.METROPOLIS_COMPLETE,
                 lambda state: state.has_all([RAC3ITEM.GRAV_BOOTS, RAC3ITEM.REFRACTOR], world.player))

    event_create(crash_site, RAC3EVENT.CRASH_SITE_COMPLETE)
    progressive_requirement = 1
    if world.options.ngplus_start.value:
        progressive_requirement += 5 if world.options.ngplus_items.value else 4

    event_create(aridia, RAC3EVENT.ARIDIA_COMPLETE,
                 lambda state: (state.has_any([RAC3ITEM.GRAV_BOOTS, RAC3ITEM.RIFT_INDUCER,
                                               RAC3ITEM.FLUX_RIFLE, RAC3ITEM.ANNIHILATOR,
                                               RAC3ITEM.RY3N0, RAC3ITEM.SUCK_CANNON,
                                               RAC3ITEM.DISC_BLADE, RAC3ITEM.PLASMA_COIL], world.player)
                                or state.has(RAC3ITEM.PROGRESSIVE_RIFT_INDUCER, world.player, 2
                     if progressive_requirement == 1 else progressive_requirement)
                                or state.has(RAC3ITEM.PROGRESSIVE_FLUX_RIFLE, world.player, progressive_requirement)
                                or state.has(RAC3ITEM.PROGRESSIVE_ANNIHILATOR, world.player, progressive_requirement)
                                or state.has(RAC3ITEM.PROGRESSIVE_RY3N0, world.player, progressive_requirement)
                                or state.has(RAC3ITEM.PROGRESSIVE_SUCK_CANNON, world.player, progressive_requirement)
                                or state.has(RAC3ITEM.PROGRESSIVE_DISC_BLADE, world.player, progressive_requirement)
                                or state.has(RAC3ITEM.PROGRESSIVE_PLASMA_COIL, world.player, progressive_requirement)))

    event_create(hideout, RAC3EVENT.HIDEOUT_QWARK,
                 lambda state: state.has_all([RAC3ITEM.WARP_PAD, RAC3ITEM.HYPERSHOT], world.player)
                               and state.has_any([RAC3ITEM.HELI_PACK, RAC3ITEM.CLANK, RAC3ITEM.PROGRESSIVE_PACK,
                                                  RAC3ITEM.CHARGE_BOOTS], world.player))
    event_create(hideout, RAC3EVENT.HIDEOUT_COMPLETE,
                 lambda state: state.has_all([RAC3ITEM.WARP_PAD, RAC3ITEM.HYPERSHOT], world.player)
                               and state.has_any([RAC3ITEM.HELI_PACK, RAC3ITEM.CLANK, RAC3ITEM.PROGRESSIVE_PACK,
                                                  RAC3ITEM.CHARGE_BOOTS], world.player))

    event_create(koros, RAC3EVENT.KOROS_COMPLETE)

    missing_regions = []
    regions_missing = []
    region_dict = world.multiworld.regions.region_cache[world.player]
    for name in REGIONS_WITH_LOCATIONS:
        if name not in region_dict.keys():
            missing_regions.append(name)
    for name, region in region_dict.items():
        if name not in REGIONS_WITH_LOCATIONS and len(region.locations):
            regions_missing.append(name)
    if missing_regions and regions_missing:
        assert False, (f"Regions: {missing_regions} were declared but not created\nRegions: {regions_missing} were "
                       f"created but not declared.")
    assert missing_regions == [], f"Regions: {missing_regions} were declared but not created."
    assert regions_missing == [], f"Regions: {regions_missing} were created but not declared."

    # shock_blaster_upgrades = create_region(world, f"{RAC3ITEM.SHOCK_BLASTER} Upgrades")
    # menu.connect(shock_blaster_upgrades, rule=lambda state: state.has(RAC3ITEM.SHOCK_BLASTER, world.player)),
    #
    # nitro_launcher_upgrades = create_region(world, f"{RAC3ITEM.NITRO_LAUNCHER} Upgrades")
    # menu.connect(nitro_launcher_upgrades, rule=lambda state: state.has(RAC3ITEM.NITRO_LAUNCHER, world.player)),
    #
    # n60_storm_upgrades = create_region(world, f"{RAC3ITEM.N60_STORM} Upgrades")
    # menu.connect(n60_storm_upgrades, rule=lambda state: state.has(RAC3ITEM.N60_STORM, world.player)),
    #
    # plasma_whip_upgrades = create_region(world, f"{RAC3ITEM.PLASMA_WHIP} Upgrades")
    # menu.connect(plasma_whip_upgrades, rule=lambda state: state.has(RAC3ITEM.PLASMA_WHIP, world.player)),
    #
    # infector_upgrades = create_region(world, f"{RAC3ITEM.INFECTOR} Upgrades")
    # menu.connect(infector_upgrades, rule=lambda state: state.has(RAC3ITEM.INFECTOR, world.player)),
    #
    # suck_cannon_upgrades = create_region(world, f"{RAC3ITEM.SUCK_CANNON} Upgrades")
    # menu.connect(suck_cannon_upgrades, rule=lambda state: state.has(RAC3ITEM.SUCK_CANNON, world.player)),
    #
    # spitting_hydra_upgrades = create_region(world, f"{RAC3ITEM.SPITTING_HYDRA} Upgrades")
    # menu.connect(spitting_hydra_upgrades, rule=lambda state: state.has(RAC3ITEM.SPITTING_HYDRA, world.player)),
    #
    # agents_of_doom_upgrades = create_region(world, f"{RAC3ITEM.AGENTS_OF_DOOM} Upgrades")
    # menu.connect(agents_of_doom_upgrades, rule=lambda state: state.has(RAC3ITEM.AGENTS_OF_DOOM, world.player)),
    #
    # flux_rifle_upgrades = create_region(world, f"{RAC3ITEM.FLUX_RIFLE} Upgrades")
    # menu.connect(flux_rifle_upgrades, rule=lambda state: state.has(RAC3ITEM.FLUX_RIFLE, world.player)),
    #
    # annihilator_upgrades = create_region(world, f"{RAC3ITEM.ANNIHILATOR} Upgrades")
    # menu.connect(annihilator_upgrades, rule=lambda state: state.has(RAC3ITEM.ANNIHILATOR, world.player)),
    #
    # holo_shield_glove_upgrades = create_region(world, f"{RAC3ITEM.HOLO_SHIELD} Upgrades")
    # menu.connect(holo_shield_glove_upgrades, rule=lambda state: state.has(RAC3ITEM.HOLO_SHIELD, world.player)),
    #
    # disc_blade_gun_upgrades = create_region(world, f"{RAC3ITEM.DISC_BLADE} Upgrades")
    # menu.connect(disc_blade_gun_upgrades, rule=lambda state: state.has(RAC3ITEM.DISC_BLADE, world.player)),
    #
    # rift_inducer_upgrades = create_region(world, f"{RAC3ITEM.RIFT_INDUCER} Upgrades")
    # menu.connect(rift_inducer_upgrades, rule=lambda state: state.has(RAC3ITEM.RIFT_INDUCER, world.player)),
    #
    # qwack_o_ray_upgrades = create_region(world, f"{RAC3ITEM.QWACK_O_RAY} Upgrades")
    # menu.connect(qwack_o_ray_upgrades, rule=lambda state: state.has(RAC3ITEM.QWACK_O_RAY, world.player)),
    #
    # ry3no_upgrades = create_region(world, f"{RAC3ITEM.RY3N0} Upgrades")
    # menu.connect(ry3no_upgrades, rule=lambda state: state.has(RAC3ITEM.RY3N0, world.player)),
    #
    # mega_turret_glove_upgrades = create_region(world, f"{RAC3ITEM.MINI_TURRET} Upgrades")
    # menu.connect(mega_turret_glove_upgrades, rule=lambda state: state.has(RAC3ITEM.MINI_TURRET, world.player)),
    #
    # lava_gun_upgrades = create_region(world, f"{RAC3ITEM.LAVA_GUN} Upgrades")
    # menu.connect(lava_gun_upgrades, rule=lambda state: state.has(RAC3ITEM.LAVA_GUN, world.player)),
    #
    # tesla_barrier_upgrades = create_region(world, f"{RAC3ITEM.SHIELD_CHARGER} Upgrades")
    # menu.connect(tesla_barrier_upgrades, rule=lambda state: state.has(RAC3ITEM.SHIELD_CHARGER, world.player)),
    #
    # bouncer_upgrades = create_region(world, f"{RAC3ITEM.BOUNCER} Upgrades")
    # menu.connect(bouncer_upgrades, rule=lambda state: state.has(RAC3ITEM.BOUNCER, world.player)),
    #
    # plasma_coil_upgrades = create_region(world, f"{RAC3ITEM.PLASMA_COIL} Upgrades")
    # menu.connect(plasma_coil_upgrades, rule=lambda state: state.has(RAC3ITEM.PLASMA_COIL, world.player))


def create_region(world: "RaC3World", name: str) -> Region:
    """
    Create a new Region object already populated with its locations

    :param world: RaC3World of current generation
    :param name: Name of the region to be created
    :return: Region object of newly created region
    """
    reg = Region(name, world.player, world.multiworld)
    options = world.options
    for key, data in RAC3_LOCATION_DATA_TABLE.items():
        if data.REGION == name and not should_skip_location(data, options):
            location = GameLocation(world.player, key, data.AP_CODE, reg)
            reg.locations.append(location)

    world.multiworld.regions.append(reg)
    return reg


def create_region_and_connect(world: "RaC3World", name: str, entrance_name: str, connected_region: Region) -> Region:
    """
    Create a new Region, connected to a given region, already populated with its item locations

    :param world: RaC3World of current generation
    :param name: Name of the region to be created
    :param entrance_name: Name of the connection linking the two regions
    :param connected_region: Region object to connect the new region to
    :return: Region object of newly created region
    """
    reg: Region = create_region(world, name)
    connected_region.connect(reg, entrance_name)
    return reg


def should_skip_location(data: RAC3LOCATIONDATA, options: type[RaC3Options]) -> bool:
    """
    Return False if the location should be skipped based on options.

    :param data: RAC3LOCATIONDATA of the location to be checked
    :param options: RaC3Options of current generation
    :return: True if the location should not be created
    """
    loc = LOCATION_FROM_AP_CODE[data.AP_CODE]
    for tag in data.TAGS:
        match tag:
            case RAC3TAG.NOT_IMPLEMENTED:  # Skip all locations not yet implemented
                return True
            case RAC3TAG.TROPHY:
                if not options.trophies.value:  # Skip trophy locations if trophies are disabled
                    return True
            case RAC3TAG.LONG_TROPHY:
                if options.trophies.value < 2:  # Skip long term trophies if not set to every trophy
                    return True
                if should_skip_skill_master(options) and loc == RAC3TROPHY.PHOENIX_SKILL_MASTER:
                    return True
                if options.ngplus_start.value < 1:
                    if loc == RAC3TROPHY.PHOENIX_NANO_FINDER or loc == RAC3TROPHY.PHOENIX_OMEGA_ARSENAL:
                        return True  # Skip Phoenix Nano Master and Omega Arsenal trophies if NG+ start is not enabled
                if options.ngplus_start.value > 0:
                    if loc == RAC3TROPHY.PHOENIX_NANO_FINDER and options.nanotech_limitation.value < 200:
                        return True  # Skip Phoenix Nano Master trophy if nanotech limitation is not set to include
                        # level 200
                    if loc == RAC3TROPHY.PHOENIX_OMEGA_ARSENAL and options.ngplus_items.value == 0:
                        return True  # Skip Phoenix Omega Arsenal trophy if NG+ items are disabled
            case RAC3TAG.SKILLPOINT:
                if options.skill_points.value == 0:
                    return True  # Skips skill points when disabled
                if options.skill_points.value == 1 and loc not in simple_skillpoints:
                    return True  # Skips harder skill points
            case RAC3TAG.T_BOLT:
                if options.titanium_bolts.value == 0:
                    return True  # Skip titanium bolt locations if titanium bolt option is disabled
            case RAC3TAG.NANOTECH:
                if should_skip_nanotech_location(loc, options):
                    return True  # Skip nanotech milestones outside the selected interval or NG+ range
            case RAC3TAG.RANGERS:
                if options.rangers.value == 0:
                    return True  # Skips ranger missions locations if rangers option is none
                if options.rangers.value == 1 and loc in extra_ranger:
                    return True  # Skips optional ranger missions locations if set to story_missions
                if options.rangers.value == 2 and loc not in extra_ranger:
                    return True  # Skips story ranger missions locations if set to optional_missions
            case RAC3TAG.ARENA:
                if options.arena.value == 0:
                    return True  # Skips arena challenges locations if arena option is none
                if options.arena.value == 1 and loc not in annihilation_nation_1:
                    return True  # Skips AN2 challenge locations if arena option is set to first_only
                if options.arena.value == 2 and loc not in annihilation_nation_2:
                    return True  # Skips AN1 challenge locations if arena option is set to second_only
            case RAC3TAG.VIDCOMIC:
                if options.vidcomics.value == 0:
                    return True  # Skips vidcomic locations if vidcomics option is disabled
            case RAC3TAG.VIDCOMIC_HEALTH_UPGRADE:
                if options.vidcomic_health_upgrades.value == 0:
                    return True  # Skips vidcomic health upgrade locations if vidcomic_health_upgrade option is disabled
            case RAC3TAG.VR:
                if options.vr_challenges.value == 0:
                    return True  # Skips vr challenges locations if vr_challenges option is disabled
            case RAC3TAG.SEWER:
                if (loc in every_sewer_crystals[options.sewer_limitation.value::]
                    and not (loc == RAC3SKILLPOINT.SEWER_MOTHERLOAD and options.sewer_limitation.value >= 100)):
                    return True  # Place sewer crystal amount specified in sewer_limitations
                if options.sewer_crystals.value == 0:
                    return True  # Skip sewer crystal locations if sewer crystals option is disabled
                if options.sewer_crystals.value == 1 and loc not in every_20_sewer_crystals:
                    return True  # Skip sewer crystal locations that are not in every 20
                if options.sewer_crystals.value == 2 and loc not in every_10_sewer_crystals:
                    return True  # Skip sewer crystal locations that are not in every 10
                if options.sewer_crystals.value == 3 and loc not in every_5_sewer_crystals:
                    return True  # Skip sewer crystal locations that are not in every 5
            case RAC3TAG.WEAPONS:
                if options.weapon_vendors.value == 0 and loc not in veldin_weapons:
                    return True  # Skips every weapon vendor checks except the Veldin ones
            case RAC3TAG.NGPLUS:
                if options.ngplus_vendors.value == 0:
                    return True  # Skips any NG+ items
            case RAC3TAG.ONE_HP_UNSTABLE:
                if options.one_hp_challenge.value.get(RAC3PLAYERTYPE.RATCHET, False):
                    return True  # Skip all unstable locations in One HP Challenge
            case RAC3TAG.SHIP:
                if options.ship_vendor.value == 0:
                    return True  # Skip all ship upgrade locations if ship upgrades are disabled
            case RAC3TAG.ARMOR:
                if options.armor_vendor.value == 0:
                    return True  # Skip all armor upgrade locations if armor upgrades are disabled
            case RAC3TAG.WEAPON_LEVEL:
                if options.weapon_level_locations.value == 0:
                    return True  # Skip all weapon level locations if weapon levels are disabled
                if options.weapon_level_locations.value == 1 and "V5" not in loc:
                    return True  # Skip all weapon level locations that are not V5 if weapon levels are set to V5 only
                if options.ngplus_items.value == 0 and ("RY3N0" in loc or "V6" in loc or "V7" in loc or "V8" in loc):
                    return True  # Skip all weapon level locations that are V6 or higher if NG+ items are disabled
                if options.one_hp_challenge.value.get(RAC3PLAYERTYPE.RATCHET, False) and "Shield Charger" in loc:
                    return True  # Skip Shield Charger level locations in One HP Challenge
            case RAC3TAG.GOAL:
                if options.lock_command_center.value == 0 and (options.goal_bio.value or options.goal_nef.value):
                    return True  # Skip if command center infobot isn't locked, and the location won't be the goal
            # Add more conditions here if needed in the future
    return False


def event_create(planet: Region, event: tuple[str, str], rule: CollectionRule = lambda _: True) -> None:
    """
    Creates a new Event specific to RAC3, given a name and rule, and adds it to a given region

    :param planet: Region the event should belong to
    :param event: RAC3EVENT to be created
    :param rule: Logic rule to be applied
    """
    planet.add_event(event[0], event[1], rule, GameLocation, GameItem)


def get_regions() -> set[str]:
    """:return: a set containing the planet names"""
    return {name for name in REGIONS_WITH_LOCATIONS}
