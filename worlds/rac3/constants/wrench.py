"""This module provides constant address offsets, for use when reading data regarding the OmniWrench"""

from worlds.rac3.constants.function import (RAC3FUNCTION, WRENCH_FUNCTION_OFFSET_PAL, WRENCH_FUNCTION_OFFSET_NTSC, EQUIP_WRENCH_OFFSET_NTSC,
                                            EQUIP_WRENCH_OFFSET_PAL, SWING_WRENCH_OFFSET_NTSC, SWING_WRENCH_OFFSET_PAL)
from worlds.rac3.constants.version import RAC3VERSION

class RAC3WRENCH:
    """Base struct for the Wrench function data, containing common address offsets"""
    NANOTECH_THRESHOLD_OFFSET: int = 0x2B0 # Contains the instruction that holds the Nanotech required to reach a certain upgrade.
    NANOTECH_DIFFERENCE_CHECK_OFFSET: int = 0x2B4 # Example: For V2, this address contains the decimal number 25. 25 + 15 = 40, OmniWrench V3.
    UPGRADE_ID_OFFSET: int = 0x2BC # Contains the ID that will be written to the BASE_ITEM_ID.
    BASE_ITEM_ID_OFFSET: int = 0x350 # Contains the item ID that the function will write to. If 00 or 01, the OmniWrench is decoupled from Nanotech
                                     # and the function will write there instead.
    PER_LEVEL_OFFSET: int = 0x18 # Starting at WRENCH_FUNCTION_BASE + NANOTECH_THRESHOLD_OFFSET, 
                                 # every +0x18 will contain an upgrade. +0x90 directly jumps from V2 to V8. 

   #SWING_WRENCH_BASE_NTSC = 0x004D38F0
    SWING_WRENCH_ADDRESS_OFFSET: int = 0xD8 # 24020009, if 24020000 or NOP'd, you cannot swing the wrench.

   #EQUIP_WRENCH_BASE_NTSC = 0x004BDB58
    EQUIP_WRENCH_ADDRESS_OFFSET: int = 0x174 # 908228CA, if 90820000 or NOP'd, you cannot equip the wrench.
    HELD_WRENCH_ADDRESS_OFFSET: int = 0x1B0 # 24040009, if 24040000 or NOP'd, the player will hold nothing when pressing square.

   #todo: Research and write the offsets in their determined file 

    @staticmethod
    def get_wrench_property_address(planet: str, game_id: str = '') -> int:
        """Provides the wrench property address for reading data"""                                
        match game_id:
            case RAC3VERSION.US_ID:
                addr = RAC3FUNCTION.WRENCH_FUNCTION_BASE_NTSC + WRENCH_FUNCTION_OFFSET_NTSC[planet]
                return addr
            case RAC3VERSION.EU_ID:
                addr = RAC3FUNCTION.WRENCH_FUNCTION_BASE_PAL + WRENCH_FUNCTION_OFFSET_PAL[planet]
                return addr
            case _:
                addr = RAC3FUNCTION.WRENCH_FUNCTION_BASE_NTSC + WRENCH_FUNCTION_OFFSET_NTSC[planet]
                return addr

    @staticmethod
    def get_swing_wrench_address(planet: str, game_id: str = '') -> int: 
        """Provides one of the many address that effectively allows or disallows the player to swing the wrench""" 
        match game_id:
            case RAC3VERSION.US_ID:
                addr = RAC3FUNCTION.SWING_WRENCH_BASE_NTSC + SWING_WRENCH_OFFSET_NTSC[planet]
                return addr
            case RAC3VERSION.EU_ID:
                addr = RAC3FUNCTION.SWING_WRENCH_BASE_PAL + SWING_WRENCH_OFFSET_PAL[planet]
                return addr
            case _:
                addr = RAC3FUNCTION.SWING_WRENCH_BASE_NTSC + SWING_WRENCH_OFFSET_NTSC[planet]
                return addr
        #RESEARCH AQUATOS AND AQUATOS BASE

    @staticmethod
    def get_equip_wrench_address(planet: str, game_id: str = '') -> int:
        """Provides one of the many address that effectively allows or disallows the player to equip the wrench"""
        match game_id:
            case RAC3VERSION.US_ID:
                addr = RAC3FUNCTION.EQUIP_WRENCH_BASE_NTSC + EQUIP_WRENCH_OFFSET_NTSC[planet]
                return addr
            case RAC3VERSION.EU_ID:
                addr = RAC3FUNCTION.EQUIP_WRENCH_BASE_PAL + EQUIP_WRENCH_OFFSET_PAL[planet]
                return addr
            case _:
                addr = RAC3FUNCTION.EQUIP_WRENCH_BASE_NTSC + EQUIP_WRENCH_OFFSET_NTSC[planet]
                return addr
