from collections import defaultdict
from math import floor, inf
from typing import Iterable

from data import *
from pathfind import to_set_pos, find_trees
from strings import snake_to_title


def print_tree(names: list[str], max_hotm: int = 10):
    for i, row in enumerate(HOTM_TREE[max_hotm-1::-1]):
        hi = max_hotm - 1 - i
        print(''.join('C' if (hi, pi) == (
            4, 3) else '1' if perk in names else '0' if perk is not None else ' ' for pi, perk in enumerate(row)))


def print_tree_coords(pairs: list[tuple[int]], max_hotm: int = 10):
    for ri in range(max_hotm - 1, -1, -1):
        for ci in range(7):
            if HOTM_TREE[ri][ci] is None:
                print(' ', end='')
                continue
            if (ri, ci) == (4, 3):
                print('C', end='')
            elif (ri, ci) in pairs:
                print('1', end='')
            else:
                print('0', end='')
        print()


def round_tick(t, is_hardstone=False):
    if is_hardstone and t * 20 < 1:
        return 0
    ticks = round(t * 20)
    if 1 <= ticks < 4:
        ticks = 4
    return ticks / 20


class Profile:
    def __init__(self, config):
        self.heart_of_the_mountain = self.hotm = config["heart_of_the_mountain"]
        self.core_of_the_mountain = self.cotm = config["core_of_the_mountain"]
        self.tokens = TOKENS_HOTM[self.hotm - 1] + TOKENS_COTM[self.cotm - 1]

        self.mithril_powder = config["mithril_powder"]
        self.gemstone_powder = config["gemstone_powder"]
        self.glacite_powder = config["glacite_powder"]

        self.breaking_power = config["breaking_power"]

        self.reaction_speed = config["reaction_speed"]
        if not 0.1 <= self.reaction_speed <= 1:
            raise ValueError(
                "reaction speed must be between 0.1s and 1s, inclusive")

        self.mode = config["mode"]
        self.ore = config["ore"]
        self.powder_type = config["powder_type"]
        self.consider_fortune = config["consider_fortune"]
        self.use_titanium = config["use_titanium"]
        self.target_amount = config["target_amount"]
        self.is_amplified = config["is_amplified"]
        self.is_fiesta = config["is_fiesta"]
        self.force_ability = config["force_ability"]
        self.given_tree = config["given_tree"]

        self.mining_speed = config["mining_speed"]
        self.ore_speed = config["ore_speed"]
        self.mithril_speed = config["mithril_speed"]
        self.dwarven_mines_speed = config["dwarven_mines_speed"]
        self.gemstone_speed = config["gemstone_speed"]

        self.mining_spread = config["mining_spread"]
        self.hardstone_spread = config["hardstone_spread"]
        self.mines_of_divan_spread = config["mines_of_divan_spread"]
        self.block_spread = config["block_spread"]
        self.ore_and_block_spread = config["ore_and_block_spread"]

        self.pristine = config["pristine"]
        self.magma_fields_pristine = config["magma_fields_pristine"]
        self.corpse_pristine = config["corpse_pristine"]

        self.mining_fortune = config["mining_fortune"]
        self.mining_fortune_mult = config["mining_fortune_mult"]
        self.ore_fortune = config["ore_fortune"]
        self.block_fortune = config["block_fortune"]
        self.mithril_fortune = config["mithril_fortune"]
        self.titanium_fortune = config["titanium_fortune"]
        self.dwarven_metal_fortune = config["dwarven_metal_fortune"]
        self.gemstone_fortune = config["gemstone_fortune"]
        self.dwarven_mines_fortune = config["dwarven_mines_fortune"]
        self.crystal_hollows_fortune = config["crystal_hollows_fortune"]
        self.mineshafts_fortune = config["mineshafts_fortune"]
        self.scraped_fortune = config["scraped_fortune"]
        self.cold_fortune = config["cold_fortune"]
        self.fiesta_fortune = config["fiesta_fortune"]

        self.fiesta_titanium_chance = config["fiesta_titanium_chance"]

        self.mining_wisdom = config["mining_wisdom"]

        self.global_powder_boost = config["global_powder_boost"]
        self.fiesta_powder_boost = config["fiesta_powder_boost"]
        self.mithril_powder_boost = config["mithril_powder_boost"]
        self.titanium_powder_gain = config["titanium_powder_gain"]
        self.gemstone_powder_boost = config["gemstone_powder_boost"]
        self.glacite_powder_boost = config["glacite_powder_boost"]
        self.treasure_chest_chance = config["treasure_chest_chance"]

        self.using_blue_cheese = config["using_blue_cheese"]
        self.compact_level = config["compact_level"]
        self.flowstate_level = config["flowstate_level"]

        self.heat_resistance = config["heat_resistance"]
        self.cold_resistance = config["cold_resistance"]
        self.mineral_chance = config["mineral_chance"]

        if self.mode == "ores":
            if self.ore == None:
                raise ValueError("ore name not specified for ores mode.")
            elif self.ore not in ("ore", "mithril", "titanium", "glacite",
                                  "ruby", "amber", "topaz", "jasper", "aquamarine"):
                raise ValueError(f"unknown ore name: {self.ore!r}")
            if self.ore == "titanium":
                if not self.use_titanium:
                    raise ValueError(
                        "use_titanium must be true for titanium ore")
            elif self.use_titanium and self.ore not in ("gray_mithril", "green_mithril", "blue_mithril"):
                raise ValueError(
                    "use_titanium can only be used on mithril and titanium ore")
            self.consider_fortune = True
        elif self.mode == "powder":
            if self.powder_type == None:
                raise ValueError("powder type not specified for powder mode.")
            if self.use_titanium:
                if self.powder_type == "mithril":
                    self.ore = "titanium"
                elif self.powder_type in ("gemstone", "glacite"):
                    raise ValueError("use_titanium can only be used"
                                     f" for mithril powder mode")
                else:
                    raise ValueError(f"unknown powder type: {self.powder_type!r}, "
                                     f"valid powder types include mithril, gemstone and glacite")
            elif self.powder_type == "mithril":
                self.ore = "mithril"
            elif self.powder_type == "gemstone":
                self.ore = ""
            elif self.powder_type == "mithril":
                pass
            else:
                raise ValueError(f"unknown powder type: {self.powder_type!r}, "
                                 f"valid powder types include mithril, gemstone and glacite")
        elif self.mode == "exp":
            if self.ore == None:
                raise ValueError("ore name not specified for exp mode.")
            elif self.ore not in ("ore", "mithril", "titanium", "glacite",
                                  "ruby", "amber", "topaz", "jasper", "aquamarine"):
                raise ValueError(f"unknown ore name: {self.ore!r}")
            if self.ore == "titanium":
                if not self.use_titanium:
                    raise ValueError(
                        "use_titanium must be true for titanium ore")
            elif self.use_titanium and self.ore not in ("gray_mithril", "green_mithril", "blue_mithril"):
                raise ValueError(
                    "use_titanium can only be used on mithril and titanium ore")
        else:
            raise ValueError(f"unknown optimizer mode: {self.mode!r}, "
                             f"only supports ores, powder and exp currently.")
        if self.force_ability is not None and self.force_ability not in ABILITIES:
            raise ValueError(f"unknown ability name: {self.force_ability}")
        if self.target_amount is not None and not isinstance(self.target_amount, (int, float)):
            raise ValueError(f"target amount must be either None or a number,"
                             f" got {type(self.target_amount)}")

    def print_info(self):
        print(f"Optimizer Mode: {self.mode}")
        print(f"HOTM Level: {self.hotm}")
        print(f"COTM Level: {self.cotm}")
        print(f"Tokens: {self.tokens}")
        print(f"Mithril Powder:  {self.mithril_powder}")
        print(f"Gemstone Powder: {self.gemstone_powder}")
        print(f"Glacite Powder:  {self.glacite_powder}")

    def get_stats(self, levels: defaultdict[str, int]) -> defaultdict[str, float]:
        result = defaultdict(int)
        for name, level in levels.items():
            perks = HOTM_PERKS[name]
            for effect in perks if isinstance(perks, list) else [perks]:
                if effect["type"] == "stat":
                    if "max_level" in effect:
                        result[effect["stat"]] += effect["init"] + \
                            (level + self.using_blue_cheese) * effect["delta"]
                    else:
                        result[effect["stat"]] += effect["value"]
        return result

    def eval(self, levels: defaultdict[str, int], do_round=False):
        """
        Evaluate efficiency score in the set mode.

        @levels: Dictionary of HOTM levels in the tree. All selected nodes should have level at least 1.
        @do_round: Whether to round tick for more accurate result at the cost of slower optimization.
        """
        stats = self.get_stats(levels)
        if self.ore == "mithril":
            block = BLOCK_MAP["blue_mithril"]
        else:
            block = BLOCK_MAP[self.ore]
        is_gemstone = self.ore in (
            "ruby", "amber", "topaz", "jasper", "aquamarine")

        mining_speed = self.mining_speed + stats["mining_speed"]
        mining_speed += self.flowstate_level * 200
        mining_fortune = self.mining_fortune + stats["mining_fortune"]
        mining_fortune += self.fiesta_fortune * self.is_fiesta
        mining_spread = self.mining_spread + stats["mining_spread"]
        mining_wisdom = self.mining_wisdom + stats["mining_wisdom"]
        powder_rate = 1 + self.global_powder_boost
        powder_rate += self.fiesta_powder_boost * self.is_fiesta
        powder_rate += stats["powder_gain"] / 100
        pristine = self.pristine
        titanium_chance = stats["titanium_chance"]
        titanium_chance += self.fiesta_titanium_chance * self.is_fiesta

        if self.ore in ("block", "hardstone"):
            mining_fortune += stats["block_fortune"]
            mining_fortune += self.block_fortune
            mining_spread += self.block_spread
            mining_spread += self.ore_and_block_spread
            if self.ore == "hardstone":
                mining_spread += stats["hardstone_spread"]
        elif self.ore == "ore":
            mining_speed += self.dwarven_mines_speed
            mining_speed += stats["ore_speed"]
            mining_fortune += self.ore_fortune
            mining_fortune += stats["ore_fortune"]
            mining_spread += self.ore_and_block_spread
            mining_spread += self.mines_of_divan_spread
        elif self.ore == "mithril":
            mining_speed += self.mithril_speed
            mining_speed += self.dwarven_mines_speed
            mining_speed += stats["dwarven_metal_speed"]
            mining_fortune += self.dwarven_mines_fortune
            mining_fortune += self.dwarven_metal_fortune
        elif self.ore == "titanium":
            mining_fortune += self.titanium_fortune
            mining_speed += self.dwarven_mines_speed
            mining_speed += stats["dwarven_metal_speed"]
            mining_fortune += self.dwarven_mines_fortune
            mining_fortune += self.dwarven_metal_fortune
        elif self.ore == "amber":
            mining_fortune += self.crystal_hollows_fortune
        elif self.ore == "topaz":
            pristine += self.magma_fields_pristine
        elif self.ore == "glacite":
            mining_speed += self.dwarven_mines_speed
            mining_speed += stats["dwarven_metal_speed"]
            mining_fortune += self.mineshafts_fortune * 0.3
            mining_spread += stats["mineshaft_mining_spread"]
        elif self.ore == "aquamarine":
            # TODO: tweak this based on cold resist
            # TODO: or a more accurate average
            mining_speed += self.dwarven_mines_speed
            mining_fortune += self.mineshafts_fortune * 0.3
            mining_spread += stats["mineshaft_gemstone_spread"]

        blocks = 1
        cycle_time = 1
        if self.ore == "titanium":
            mithrils = 100 / titanium_chance
            mithril_str = BLOCK_MAP["blue_mithril"]["block_strength"]
            titanium_str = BLOCK_MAP["titanium"]["block_strength"]
            mithril_time = 1.5 * mithril_str / mining_speed
            titanium_time = 1.5 * titanium_str / mining_speed
            if do_round:
                mithril_time = round_tick(mithril_time)
                titanium_time = round_tick(titanium_time)
            cycle_time = mithril_time * mithrils + titanium_time
            blocks = mithrils + 1
        else:
            block_str = block["block_strength"]
            block_time = 1.5 * block_str / mining_speed
            if do_round:
                block_time = round_tick(block_time)
            cycle_time = block_time
        cycle_time += self.reaction_speed * blocks

        if self.consider_fortune:
            if is_gemstone:
                mining_speed += self.gemstone_speed
                mining_speed += stats["gemstone_speed"]
                mining_fortune += self.gemstone_fortune
                mining_fortune += stats["gemstone_fortune"]
            mining_fortune *= 1 + self.mining_fortune_mult
            fortune_mult = 1 + mining_fortune / 100
            if self.ore == "titanium":
                fortune_mult *= stats["titanium_drop"]
            elif is_gemstone:
                pristine_chance = pristine / 100
                fortune_mult = fortune_mult * (1 - pristine_chance) + \
                    fortune_mult * 20 * pristine_chance

        value = 0
        if self.mode in ("ores", "exp"):
            value = block["drops"][1]
            if not is_gemstone and self.compact_level > 0:
                value += 160 * COMPACT_CHANCES[self.compact_level - 1] / 100
            if self.consider_fortune:
                value *= fortune_mult
            if self.mode == "exp":
                value *= 1 + mining_wisdom / 100
            value *= 1 + mining_spread / 100
        elif self.mode == "powder":
            if self.powder_type == "mithril":
                powder_rate += self.mithril_powder_boost
                powder_rate += stats["mithril_powder"]
                value = 5 + (self.cotm >= 4)
                if self.use_titanium:
                    mithrils = 100 / titanium_chance
                    value = value * mithrils + self.titanium_powder_gain
            elif self.powder_type == "gemstone":
                powder_rate += self.gemstone_powder_boost
                powder_rate += stats["gemstone_powder"]
                chance_boost = self.treasure_chest_chance
                chance_boost += stats["treasure_chest_chance"] / 100
                chest_chance = 0.002 * (1 + chance_boost)
                great_explorer_level = levels["great_explorer"]
                chests = (1 + mining_spread / 100) * chest_chance
                if great_explorer_level == 0:
                    locks = 5
                else:
                    if do_round:
                        locks = 4 - great_explorer_level // 5
                    else:
                        locks = 4 - great_explorer_level / 5
                cycle_time += chests * \
                    (locks + self.reaction_speed) + self.reaction_speed
                value = 349.0054361184384
            elif self.powder_type == "glacite":
                powder_rate += stats["glacite_powder"]
                value = 1
                powder_rate += self.glacite_powder_boost
                powder_rate += self.glacite_powder_gain
            else:
                raise ValueError(f"unknown powder type: {self.powder_type}")
            value *= powder_rate
            if self.consider_fortune:
                value *= fortune_mult
            if self.powder_type != "gemstone":
                value *= 1 + mining_spread / 100

        return value / cycle_time * 60


class Optimizer:
    def __init__(self, config):
        self.profile = Profile(config)
        if self.profile.given_tree is None:
            raise ValueError("tree pathfind not implemented yet")
        self.trees = [to_set_pos(self.profile.given_tree)]

        self.levels = defaultdict(int)
        self.mithril_powder = 0
        self.gemstone_powder = 0
        self.glacite_powder = 0

    def find_trees(self):
        abilities = []
        nodes = []
        trees = find_trees(abilities, nodes,
                           self.profile.hotm, self.profile.tokens)

    def print_info(self):
        self.profile.print_info()

    def get_cost(self, name: str) -> tuple[str, int]:
        if self.levels[name] == 0:
            raise ValueError(f"cannot level up node"
                             f" that is not selected: {name!r}")
        return get_cost_type(name), get_cost(name, self.levels[name])

    def can_afford_and_cost(self, name: str) -> tuple[bool, int]:
        if self.levels[name] >= MAX_LEVELS[name]:
            return False, 0
        powder_type, cost = self.get_cost(name)
        if powder_type == "mithril":
            return self.mithril_powder >= cost, cost
        elif powder_type == "gemstone":
            return self.gemstone_powder >= cost, cost
        else:
            return self.glacite_powder >= cost, cost

    def can_afford(self, name: str) -> bool:
        if self.levels[name] >= MAX_LEVELS[name]:
            return False
        powder_type, cost = self.get_cost(name)
        if powder_type == "mithril":
            return self.mithril_powder >= cost
        elif powder_type == "gemstone":
            return self.gemstone_powder >= cost
        else:
            return self.glacite_powder >= cost

    def optimize(self, tree: Iterable[tuple[int, int]] | None = None):
        if tree is None:
            if self.profile.given_tree is None:
                raise ValueError("tree isn't given in config or argument")
            tree = to_set_pos(self.profile.given_tree)
        else:
            tree = tuple(pos for pos in tree
                         if to_name(pos) != "core_of_the_mountain")
            if len(tree) > self.profile.tokens:
                raise ValueError(f"tokens not enough to build this tree: "
                                 f"{len(tree)}>{self.profile.tokens}")
        if self.profile.mode in ("ores", "exp"):
            stats_used = TASK_STATS[self.profile.ore]
        elif self.profile.mode == "powder":
            if self.profile.consider_fortune:
                if self.profile.use_titanium:
                    stats_used = TASK_STATS["titanium"]
                else:
                    stats_used = TASK_STATS[self.profile.powder_type]
                stats_used.append("powder_gain")
            else:
                stats_used = TASK_STATS[f"{self.profile.powder_type}_powder"]
        else:
            raise ValueError(f"unknown mode: {self.profile.mode!r}")

        sig_nodes = [pos for pos in tree if len(
            {*NODE_STATS[to_name(pos)]} & {*stats_used})]
        sig_names = [to_name(pos) for pos in sig_nodes]
        print(f"Relevant Stats: {stats_used}")
        print(f"Significant Nodes: {sig_names}")
        opti_names = [name for name in sig_names if isinstance(
            HOTM_PERKS[name], dict) and HOTM_PERKS[name]["type"] == "stat"
            and "max_level" in HOTM_PERKS[name]]
        print(f"Optimizable Nodes: {opti_names}")
        self.levels = defaultdict(int)
        for pos in tree:
            self.levels[to_name(pos)] = 1

        self.mithril_powder = self.profile.mithril_powder
        self.gemstone_powder = self.profile.gemstone_powder
        self.glacite_powder = self.profile.glacite_powder

        # Check if each powder is sufficient to max the optimizable perks to refine the result
        mithril_nodes = []
        gemstone_nodes = []
        glacite_nodes = []
        for name in opti_names:
            if get_cost_type(name) == "mithril":
                mithril_nodes.append(name)
            elif get_cost_type(name) == "gemstone":
                gemstone_nodes.append(name)
            else:
                glacite_nodes.append(name)
        if sum(TOTAL_COSTS[name][-1] for name in mithril_nodes) <= self.mithril_powder:
            for name in mithril_nodes:
                self.levels[name] = MAX_LEVELS[name]
        if sum(TOTAL_COSTS[name][-1] for name in gemstone_nodes) <= self.gemstone_powder:
            for name in gemstone_nodes:
                self.levels[name] = MAX_LEVELS[name]
        if sum(TOTAL_COSTS[name][-1] for name in glacite_nodes) <= self.glacite_powder:
            for name in glacite_nodes:
                self.levels[name] = MAX_LEVELS[name]

        i = 0
        while True:
            pairs = [(name, pair[1]) for name in opti_names
                     if (pair := self.can_afford_and_cost(name))[0]]
            if len(pairs) == 0:
                break
            current_score = self.profile.eval(self.levels)
            best_name = None
            best_ratio = -inf
            best_cost = 0
            for name, cost in pairs:
                new_levels = self.levels.copy()
                new_levels[name] += 1
                new_score = self.profile.eval(new_levels)
                ratio = (new_score - current_score) / cost
                if ratio > best_ratio:
                    best_name = name
                    best_ratio = ratio
                    best_cost = cost
            if best_ratio < 0 or best_name is None:
                print(f"{best_name=}")
                print(f"{best_ratio=}")
                print(f"{best_cost=}")
                raise ValueError("something is wrong and the"
                                 " best purchase hurts score")
            self.levels[best_name] += 1
            cost_type = get_cost_type(best_name)
            # print(best_name, cost_type)
            if cost_type == "mithril":
                self.mithril_powder -= best_cost
            elif cost_type == "gemstone":
                self.gemstone_powder -= best_cost
            else:
                self.glacite_powder -= best_cost
            i += 1
        levels_items = [(name, level) for name, level in self.levels.items()]
        print('\n')
        print('-' * 20 + " Tree Used " + '-' * 20)
        print_tree_coords(tree)
        print('-' * 20 + " Results " + '-' * 20)
        for name, level in sorted(levels_items, key=lambda pair: NODE_NAMES.index(pair[0])):
            if name in opti_names:
                print(f" - {snake_to_title(name)}: {level}")
        result_eval = self.profile.eval(self.levels)
        if self.profile.mode == "powder":
            mode_str = snake_to_title(f"{self.profile.powder_type}_powder")
        else:
            mode_str = snake_to_title(self.ore)
        print(f"Optimized Efficiency: {result_eval:.2f} {mode_str} per minute.\n"
              f"                    : {result_eval*60:.2f} {mode_str} per hour.")
        print('-' * 20 + " Powder Left " + '-' * 20)
        print(f" - Mithril Powder: {self.mithril_powder}")
        print(f" - Gemstone Powder: {self.gemstone_powder}")
        print(f" - Glacite Powder: {self.glacite_powder}")
        if self.profile.target_amount is not None:
            time = floor(self.profile.target_amount /
                         result_eval * 60)  # in seconds
            print('-' * 20 + " Time Estimation " + '-' * 20)
