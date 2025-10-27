from typing import Any, TYPE_CHECKING

from .Rac3Addresses import LOCATIONS, RAC3_REGION_DATA_TABLE, RAC3OPTION

if TYPE_CHECKING:
    from . import RaC3World


def setup_options_from_slot_data(world: "RaC3World") -> None:
    if hasattr(world.multiworld, "re_gen_passthrough"):
        if world.game in world.multiworld.re_gen_passthrough:
            world.using_ut = True
            world.passthrough = world.multiworld.re_gen_passthrough[world.game]
            world.options.start_inventory_from_pool.value = world.passthrough[RAC3OPTION.START_INVENTORY_FROM_POOL]
            world.options.starting_weapons.value = world.passthrough[RAC3OPTION.STARTING_WEAPONS]
            world.options.bolt_and_xp_multiplier.value = world.passthrough[RAC3OPTION.BOLT_AND_XP_MULTIPLIER]
            world.options.enable_progressive_weapons.value = world.passthrough[RAC3OPTION.ENABLE_PROGRESSIVE_WEAPONS]
            world.options.extra_armor_upgrade.value = world.passthrough[RAC3OPTION.EXTRA_ARMOR_UPGRADE]
            world.options.skill_points.value = world.passthrough[RAC3OPTION.SKILL_POINTS]
            world.options.trophies.value = world.passthrough[RAC3OPTION.TROPHIES]
            world.options.titanium_bolts.value = world.passthrough[RAC3OPTION.TITANIUM_BOLTS]
            world.options.nanotech_milestones.value = world.passthrough[RAC3OPTION.NANOTECH_MILESTONES]
            world.options.exclude_locations.value = world.passthrough[RAC3OPTION.EXCLUDE]
        else:
            world.using_ut = False
    else:
        world.using_ut = False


def map_page_index(data: Any) -> int:
    return RAC3_REGION_DATA_TABLE[data].ID


def tracker_data() -> dict[str, int]:
    return {loc["Name"]: loc["Id"] for loc in LOCATIONS}


tracker_world = {
    "map_page_maps": "maps/maps.json",
    "map_page_locations": "locations/locations.json",
    "map_page_setting_key": r'rac3_current_planet_{player}_{team}',
    "map_page_index": map_page_index,
    "poptracker_name_mapping": tracker_data()
}
