import logging
from typing import List, TYPE_CHECKING

from BaseClasses import Item, ItemClassification
from Rac3Addresses import (FILLER_LIST, GADGET_LIST, PLANET_LIST, PROGRESSIVE_DICT, RAC3_ITEM_DATA_TABLE, RAC3ITEMDATA,
                           RAC3OPTION, WEAPON_LIST)
from worlds.rac3 import RAC3ITEM

from .Types import GameItem

if TYPE_CHECKING:
    from . import RaC3World

rac3_logger = logging.getLogger(RAC3OPTION.GAME_TITLE_FULL)
rac3_logger.setLevel(logging.DEBUG)


def create_itempool(world: "RaC3World") -> List[Item]:
    itempool: List[Item] = []
    options = world.options

    for name in item_table.keys():
        item_type: ItemClassification = RAC3_ITEM_DATA_TABLE[name].AP_CLASSIFICATION
        item_amount: int = item_counts.get(name)

        # Already placed items (Starting items and vanilla)
        if name in world.preplaced_items:
            if item_amount == 1:
                continue
            else:
                item_amount -= 1  # remove one from the pool as it has already been placed

        # Progressive Weapons option
        if not options.enable_progressive_weapons.value:
            if name in prog_dict.keys():
                continue
        else:  # options.EnableProgressiveWeapons.value:
            if name in weapon_dict.keys():
                continue

        # ExtraArmorUpgrade option
        if name == RAC3ITEM.PROGRESSIVE_ARMOR:
            item_amount += options.extra_armor_upgrade.value

        # Catch accidental duplicates
        if item_amount > 1 and name not in PROGRESSIVE_DICT.keys():
            rac3_logger.warning(f"multiple copies of {name} added to the item pool")

        itempool += create_multiple_items(world, name, item_amount, item_type)

    victory = create_item(world, RAC3ITEM.VICTORY)
    world.multiworld.get_location("Command Center: Biobliterator Defeated!", world.player).place_locked_item(victory)
    return itempool


def create_multiple_items(world: "RaC3World", name: str, count: int = 1,
                          item_type: ItemClassification = ItemClassification.progression) -> List[Item]:
    data = RAC3_ITEM_DATA_TABLE[name]
    itemlist: List[Item] = []

    for i in range(count):
        itemlist += [GameItem(name, item_type, data.AP_CODE, world.player)]

    return itemlist


def create_item(world: "RaC3World", name: str) -> Item:
    data = RAC3_ITEM_DATA_TABLE[name]
    return GameItem(name, data.AP_CLASSIFICATION, data.AP_CODE, world.player)


def get_filler_item_selection(world: "RaC3World"):
    frequencies: dict[str, int] = {
        RAC3ITEM.TITANIUM_BOLT: 0,
        RAC3ITEM.WEAPON_XP: 0,
        RAC3ITEM.PLAYER_XP: 5,
        RAC3ITEM.BOLTS: 10,
        RAC3ITEM.INFERNO_MODE: 1,
        RAC3ITEM.JACKPOT: 10,
    }
    if not world.options.enable_progressive_weapons.value:
        weapon_exp: dict[str, int] = {RAC3ITEM.WEAPON_XP: 5}
        frequencies.update(weapon_exp)
    # if world.options.traps_enabled:
    #     traps = trap_items.copy()
    #     frequencies.update(traps)
    return [name for name, count in frequencies.items() for _ in range(count)]


def get_dict(item_list) -> dict[str, RAC3ITEMDATA]:
    return dict(filter(lambda data_kv: data_kv[0] in item_list, RAC3_ITEM_DATA_TABLE.items()))


weapon_dict: dict[str, RAC3ITEMDATA] = get_dict(WEAPON_LIST)
prog_dict: dict[str, RAC3ITEMDATA] = get_dict(PROGRESSIVE_DICT.keys())
gadget_dict: dict[str, RAC3ITEMDATA] = get_dict(GADGET_LIST)
planet_dict: dict[str, RAC3ITEMDATA] = get_dict(PLANET_LIST)
filler_dict: dict[str, RAC3ITEMDATA] = get_dict(FILLER_LIST)

item_counts: dict[str, int] = {
    **dict.fromkeys(weapon_dict.keys(), 1),
    **dict.fromkeys(prog_dict.keys(), 5),
    **dict.fromkeys(gadget_dict.keys(), 1),
    **dict.fromkeys(planet_dict.keys(), 1),
    RAC3ITEM.VICTORY: 0
}



item_table: dict[str, RAC3ITEMDATA] = {
    **weapon_dict,
    **prog_dict,
    **gadget_dict,
    **planet_dict,
    # **filler_dict,
}

# Todo: Add Item Groups (see location_groups)
item_group = {

}

# class ItemData(NamedTuple):
#    ap_code: Optional[int]
#    classification: ItemClassification
#    count: Optional[int] = 1

default_starting_weapons = {name: 1 for name in weapon_dict.keys()}


def filter_items(classification):
    return filter(lambda l: l[1].AP_CLASSIFICATION == classification, RAC3_ITEM_DATA_TABLE.items())


def filter_item_names(classification):
    return map(lambda entry: entry[0], filter_items(classification))


def starting_weapons(world, dictionary: dict[str, int]) -> list[str]:
    weapon_list: list[str] = []
    for name in dictionary:
        count = dictionary[name]
        if count == 0:
            continue
        if world.options.enable_progressive_weapons.value:
            for i in range(count):
                weapon_list.append(f"Progressive {name}")
        else:
            weapon_list.append(name)
    world.random.shuffle(weapon_list)
    return [weapon_list[0], weapon_list[1]]
