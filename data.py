from json import load
from pathlib import Path as pathtype


DATA_DIR = pathtype("data")

with open(DATA_DIR / "abilities.json") as file:
    ABILITIES = load(file)
with open(DATA_DIR / "blocks.json") as file:
    BLOCKS = load(file)
with open(DATA_DIR / "compact_chances.json") as file:
    COMPACT_CHANCES = load(file)
with open(DATA_DIR / "hotm_perks.json") as file:
    HOTM_PERKS = load(file)
with open(DATA_DIR / "hotm_powder_exponent.json") as file:
    HOTM_POWDER_EXPONENT = load(file)
with open(DATA_DIR / "hotm_powder_level_pad.json") as file:
    HOTM_POWDER_LEVEL_PAD = load(file)
with open(DATA_DIR / "hotm_tree.json") as file:
    HOTM_TREE = load(file)
with open(DATA_DIR / "powder_types.json") as file:
    POWDER_TYPES = load(file)
with open(DATA_DIR / "task_stats.json") as file:
    TASK_STATS = load(file)
with open(DATA_DIR / "tokens_hotm.json") as file:
    TOKENS_HOTM = load(file)
with open(DATA_DIR / "tokens_cotm.json") as file:
    TOKENS_COTM = load(file)

NODE_NAMES = []
NODE_POSITIONS = {}
for i, row in enumerate(HOTM_TREE):
    for j, name in enumerate(row):
        if name is not None:
            NODE_NAMES.append(name)
            NODE_POSITIONS[name] = (i, j)

HOTM_BOOL = [[item is not None for item in row] for row in HOTM_TREE]
HOTM_TAKEN = [(i, j) for i, row in enumerate(HOTM_BOOL)
              for j, item in enumerate(row) if item]

BLOCK_MAP = {}
for block in BLOCKS:
    BLOCK_MAP[block["name"]] = {key: value for key, value in block.items()
                                if key != "name"}


def to_name(node_pos: tuple[int, int]) -> str:
    """
    Get the HOTM node name from the position tuple.

    @node_pos: The integer tuple of row and column of the node, starting each at 0.
    """
    return HOTM_TREE[node_pos[0]][node_pos[1]]


def is_node(node_name: str) -> bool:
    """
    Check if a HOTM node name exists.

    @node_name: The name of the node.
    """
    return node_name in NODE_NAMES


def to_pos(node_name: str) -> tuple[int, int]:
    """
    Get the HOTM node position tuple from the name.

    @node_name: The name of the node.
    """
    return NODE_POSITIONS[node_name]


def get_cost(node_name: str, level: int) -> int:
    """
    Calculates the cost of the next purchase on a node.

    @node_name: The string name of the node.
    @level: The integer levels already purchased on the node.
    """
    if node_name not in HOTM_POWDER_EXPONENT or HOTM_POWDER_EXPONENT[node_name] is None:
        raise ValueError(f"node not found or not leveled: {node_name}")

    pad = HOTM_POWDER_LEVEL_PAD.get(node_name, 1)
    exp = HOTM_POWDER_EXPONENT[node_name]

    # The formula for cost at a specific level L is (L + pad)^exp
    cost = (level + pad + 1) ** exp
    return int(cost)


def get_cost_type(name: str) -> str:
    return POWDER_TYPES[to_pos(name)[0]]


MAX_LEVELS = {}
TOTAL_COSTS = {}
for name in NODE_NAMES:
    perk = HOTM_PERKS[name]
    if isinstance(perk, list) or perk["type"] != "stat" or "max_level" not in perk:
        continue
    MAX_LEVELS[name] = perk["max_level"]
    costs = [0]
    total_cost = 0
    for i in range(1, perk["max_level"]):
        total_cost += get_cost(name, i)
        costs.append(total_cost)
    TOTAL_COSTS[name] = costs


STAT_NAMES = []
NODE_STATS = {}
for name, perk in HOTM_PERKS.items():
    node_stats = []
    if isinstance(perk, dict):
        if perk["type"] == "stat":
            node_stats.append(perk["stat"])
        elif perk["type"] in ("ability", "misc"):
            node_stats.extend(perk.get("related_stats", []))
    elif isinstance(perk, list):
        for subperk in perk:
            node_stats.append(subperk["stat"])
    NODE_STATS[name] = node_stats.copy()
    STAT_NAMES.extend(node_stats)
STAT_NAMES = sorted({*STAT_NAMES})

# ability_cooldown_reduction
# block_fortune
# cold_resistance
# dwarven_metal_fortune
# dwarven_metal_speed
# gemstone_fortune
# gemstone_powder
# gemstone_speed
# glacite_powder
# glacite_powder_gain
# goblin_chance
# hardstone_spread
# heat_resistance
# hotm_xp_gain
# mineshaft_ability_cooldown_reduction
# mineshaft_fortune
# mineshaft_gemstone_spread
# mineshaft_speed
# mining_fortune
# mining_speed
# mining_spread
# mining_wisdom
# mithril_powder
# ore_fortune
# powder_gain
# pristine
# rare_ocurrences
# titanium_chance
# titanium_drop
# treasure_chest_chance
