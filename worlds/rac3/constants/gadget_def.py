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
