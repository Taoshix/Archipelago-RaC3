"""Galactic Map destination rows and their inline objective text."""

from worlds.rac3.constants.data.region import INFOBOT_FROM_PLANET
from worlds.rac3.constants.locations.general import RAC3LOCATION
from worlds.rac3.constants.locations.skillpoints import RAC3SKILLPOINT
from worlds.rac3.constants.locations.tbolts import RAC3TBOLT
from worlds.rac3.constants.region import PLANET_VENDOR_OFFSET, RAC3REGION


PLANET_ROWS_OFFSET = {
    **PLANET_VENDOR_OFFSET,
    RAC3REGION.VELDIN: 0x2FC0,
    RAC3REGION.MUSEUM: 0xE80,
}


LDF_LOCATIONS = [
    RAC3LOCATION.MARCADIA_REFRACTOR,
    RAC3SKILLPOINT.MARCADIA_REFLECT,
    RAC3TBOLT.MARCADIA_LAST_REFRACTOR,
    RAC3TBOLT.MARCADIA_BEFORE_AL,
    RAC3LOCATION.MARCADIA_MEET_AL,
]


GAUNTLET_LOCATIONS = [
    RAC3LOCATION.NATION_HEAT_STREET,
    RAC3LOCATION.NATION_CRISPY_CRITTER,
    RAC3LOCATION.NATION_PYRO_PLAYGROUND,
    RAC3LOCATION.NATION_SUICIDE_RUN,
    RAC3LOCATION.NATION_BBQ_BOULEVARD,
    RAC3LOCATION.NATION_MAZE_OF_BLAZE,
    RAC3LOCATION.NATION_CREMATION_STATION,
    RAC3LOCATION.NATION_THE_ANNIHILATOR,
    RAC3TBOLT.NATION_CLIFF,
    RAC3TBOLT.NATION_PLATFORM,
    RAC3SKILLPOINT.NATION_CAMERA,
    RAC3SKILLPOINT.NATION_FLEE,
    RAC3SKILLPOINT.NATION_EIGHT,
]


class RAC3GALACTICMAP:
    """Layout and US-relative addresses of the Galactic Map destination rows."""

    ROW_SIZE = 0xB0
    MAX_ROWS = 0x3C
    OBJECTIVE_OFFSET = 0x55
    OBJECTIVE_SIZE = 0x50
    ROWS_BASE = 0x00230E98

    @staticmethod
    def get_rows_address(planet: str) -> int | None:
        """Return the US-relative row address for use with address_convert."""
        if planet not in INFOBOT_FROM_PLANET:
            return None
        return RAC3GALACTICMAP.ROWS_BASE + PLANET_ROWS_OFFSET[planet]
