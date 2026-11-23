"""Addresses and field offsets for the game's GadgetDef table."""

from worlds.rac3.constants.region import PLANET_GADGETDEF_OFFSET, RAC3REGION
from worlds.rac3.constants.status import RAC3STATUS


class RAC3GADGETDEF:
    """A 0xF0-byte definition indexed by the exact ItemID, including weapon variants."""

    SIZE: int = 0xF0
    COUNT: int = 0xCB  # IDs 0x00 through 0xCA, including the empty definition at ID 0.

    IS_LEVELABLE_OFFSET: int = 0x00  # u8
    LEVEL_OFFSET: int = 0x01  # u8, zero-based
    NAME_TEXT_ID_OFFSET: int = 0x04  # s32
    EQUIPMENT_SLOT_OFFSET: int = 0x08  # s32
    ATTACH_JOINT_OFFSET: int = 0x0C  # s32
    MOBY_CLASS_OFFSET: int = 0x10  # s32
    SECOND_MOBY_CLASS_OFFSET: int = 0x14  # s32
    HOLD_STYLE_OFFSET: int = 0x18  # s32
    STANDING_FIRE_ANIM_OFFSET: int = 0x24  # s32
    FIRE_OVERLAY_ANIM_OFFSET: int = 0x28  # s32
    CROUCH_FIRE_OVERLAY_ANIM_OFFSET: int = 0x2C  # s32
    SUSTAINED_FIRE_POSE_OFFSET: int = 0x30  # 32-bit value
    AMMO_PICKUP_PLURAL_TEXT_ID_OFFSET: int = 0x34  # s16
    AMMO_PICKUP_SINGULAR_TEXT_ID_OFFSET: int = 0x36  # s16
    ICON_ID_OFFSET: int = 0x38  # u16
    AMMO_PICKUP_MOBY_CLASS_OFFSET: int = 0x3A  # s16
    VENDOR_DESCRIPTION_TEXT_ID_OFFSET: int = 0x3E  # s16
    VENDOR_MESSAGE_TEXT_ID_OFFSET: int = 0x42  # s16
    BASE_NAME_TEXT_ID_OFFSET: int = 0x44  # s16
    NEXT_LEVEL_ITEM_ID_OFFSET: int = 0x46  # s16
    PREVIOUS_LEVEL_ITEM_ID_OFFSET: int = 0x48  # s16
    PROJECTILE_SPEED_OFFSET: int = 0x4C  # float
    SHOTS_PER_SECOND_OFFSET: int = 0x50  # float
    TURRET_AMMO_CAPACITY_OFFSET: int = 0x54  # u16
    CUMULATIVE_XP_THRESHOLD_OFFSET: int = 0x68  # s32, in units of stored weapon XP >> 5
    DAMAGE_OFFSET: int = 0x6C  # float
    AREA_DAMAGE_OFFSET: int = 0x70  # float
    PURCHASE_PRICE_OFFSET: int = 0x7C  # s32
    AMMO_UNIT_PRICE_OFFSET: int = 0x84  # u16
    PDA_AMMO_UNIT_PRICE_OFFSET: int = 0x86  # u16
    AMMO_PICKUP_OFFSET: int = 0x88  # u16
    MAX_AMMO_OFFSET: int = 0x8A  # u16
    INITIAL_AMMO_OFFSET: int = 0x8E  # u16
    AIM_MODEL_OFFSET: int = 0xA0  # Four floats
    AIM_MODEL_ROTATION_OFFSET: int = 0xB0  # Four floats
    LEVEL_UP_MESSAGE_ID_OFFSET: int = 0xD0  # s32
    VENDOR_ITEM_DISPLAY_INDEX_OFFSET: int = 0xD4  # s16
    VENDOR_AMMO_DISPLAY_INDEX_OFFSET: int = 0xD6  # s16

    @classmethod
    def get_property_address(cls, planet: str, item_id: int, property_offset: int = 0) -> int:
        """Return an NTSC-U address for use with the client's regular reads and writes."""
        if not 0 <= item_id < cls.COUNT:
            raise ValueError(f"Invalid GadgetDef ItemID: {item_id:#x}")
        if not 0 <= property_offset < cls.SIZE:
            raise ValueError(f"Invalid GadgetDef property offset: {property_offset:#x}")
        return RAC3STATUS.GADGETDEF_BASE + PLANET_GADGETDEF_OFFSET[planet] + item_id * cls.SIZE + property_offset

    @classmethod
    def contains_address(cls, planet: str, address: int) -> bool:
        """Check whether an NTSC-U address falls in the current planet's GadgetDef table."""
        planet_offset = PLANET_GADGETDEF_OFFSET.get(planet)
        if planet_offset is None:
            return False
        base = RAC3STATUS.GADGETDEF_BASE + planet_offset
        return base <= address < base + cls.COUNT * cls.SIZE

WEAPON_DAMAGES_DICT: dict[int, float] = {
    # Shock Blaster
    0x27: 2.0,
    0x28: 2.5,
    0x29: 3.0,
    0x2A: 4.0,
    0x2B: 5.0,
    0x2C: 55.0,
    0x2D: 70.0,
    0x2E: 105.0,
    # Nitro Launcher
    0x77: 10.0,
    0x78: 12.0,
    0x79: 15.0,
    0x7A: 20.0,
    0x7B: 40.0,
    0x7C: 210.0,
    0x7D: 250.0,
    0x7E: 300.0,
    # N60 Storm
    0x2F: 1.5,
    0x30: 1.75,
    0x31: 2.0,
    0x32: 2.5,
    0x33: 3.5,
    0x34: 35.0,
    0x35: 50.0,
    0x36: 60.0,
    # Plasma Whip
    0x7F: 2.0,
    0x80: 2.5,
    0x81: 3.5,
    0x82: 5.0,
    0x83: 7.0,
    0x84: 70.0,
    0x85: 90.0,
    0x86: 120.0,
    # Infector
    0x37: 9.0,
    0x38: 12.0,
    0x39: 16.0,
    0x3A: 20.0,
    0x3B: 30.0,
    0x3C: 200.0,
    0x3D: 250.0,
    0x3E: 300.0,
    # Suck Cannon
    0x87: 10.0,
    0x88: 13.0,
    0x89: 16.0,
    0x8A: 22.0,
    0x8B: 30.0,
    0x8C: 210.0,
    0x8D: 250.0,
    0x8E: 300.0,
    # Spitting Hydra
    0x47: 10.0,
    0x48: 12.0,
    0x49: 14.0,
    0x4A: 16.0,
    0x4B: 20.0,
    0x4C: 160.0,
    0x4D: 270.0,
    0x4E: 300.0,
    # Agents of Doom
    0x57: 12.0,
    0x58: 16.0,
    0x59: 22.0,
    0x5A: 25.0,
    0x5B: 30.0,
    0x5C: 40.0,
    0x5D: 50.0,
    0x5E: 60.0,
    # Flux Rifle
    0x6F: 15.0,
    0x70: 20.0,
    0x71: 25.0,
    0x72: 80.0,
    0x73: 140.0,
    0x74: 260.0,
    0x75: 350.0,
    0x76: 420.0,
    # Annihilator
    0x3F: 25.0,
    0x40: 30.0,
    0x41: 40.0,
    0x42: 55.0,
    0x43: 70.0,
    0x44: 150.0,
    0x45: 200.0,
    0x46: 250.0,
    # Holo Shield Glove
    0x67: 10.0,
    0x68: 15.0,
    0x69: 20.0,
    0x6A: 25.0,
    0x6B: 30.0,
    0x6C: 50.0,
    0x6D: 75.0,
    0x6E: 100.0,
    # Disc Blade Gun
    0x4F: 25.0,
    0x50: 30.0,
    0x51: 35.0,
    0x52: 40.0,
    0x53: 45.0,
    0x54: 55.0,
    0x55: 70.0,
    0x56: 105.0,
    # Rift Inducer
    0x5F: 50.0,
    0x60: 65.0,
    0x61: 75.0,
    0x62: 85.0,
    0x63: 100.0,
    0x64: 200.0,
    0x65: 250.0,
    0x66: 300.0,
    # Qwack-O-Ray
    0x8F: 50.0,
    0x90: 75.0,
    0x91: 100.0,
    0x92: 125.0,
    0x93: 150.0,
    0x94: 200.0,
    0x95: 250.0,
    0x96: 300.0,
    # RY3N0
    0x97: 300.0,
    0x98: 350.0,
    0x99: 400.0,
    0x9A: 450.0,
    0x9B: 500.0,
    # Miniturret Glove
    0x15: 1.5,
    0xA2: 2.0,
    0xA8: 2.5,
    0xA9: 3.0,
    0xAA: 8.0,
    0xAB: 40.0,
    0xAC: 50.0,
    0xAD: 60.0,
    # Lava Gun
    0x11: 8.0,
    0xA1: 12.0,
    0xAE: 18.0,
    0xAF: 25.0,
    0xB0: 35.0,
    0xB1: 130.0,
    0xB2: 150.0,
    0xB3: 180.0,
    # Shield Charger
    0x16: 3.0,
    0xA7: 5.0,
    0xC0: 7.0,
    0xC1: 9.0,
    0xC2: 12.0,
    0xC3: 15.0,
    0xC4: 20.0,
    0xC5: 25.0,
    # Bouncer
    0x13: 30.0,
    0xA6: 35.0,
    0xB4: 40.0,
    0xB5: 45.0,
    0xB6: 50.0,
    0xB7: 75.0,
    0xB8: 90.0,
    0xB9: 110.0,
    # Plasma Coil
    0x10: 120.0,
    0xA0: 150.0,
    0xBA: 180.0,
    0xBB: 210.0,
    0xBC: 150.0,
    0xBD: 170.0,
    0xBE: 190.0,
    0xBF: 210.0,
    # OmniWrench
    0x09: 1.0,
    0xA4: 2.0,
    0xA5: 5.0,
    0xC6: 10.0,
    0xC7: 20.0,
    0xC8: 30.0,
    0xC9: 45.0,
    0xCA: 60.0,
}
