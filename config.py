CONFIG = {
    # ? Estimated Reaction speed between the finish of mining
    # ? a block and moving on to the next one. The rhythm with
    # ? practice leads to a min and default of 0.1s since human reaction
    # ? speed averages at around 0.25s.
    # ? Cannot be set to 0 to ignore this calculation since leaving it
    # ? on is recommended since it tends to lead to more optimal results
    # ? especially from stopping inflated results with instamining
    "reaction_speed": 0.1,

    # * Extract the stat specifics for easier edits
    # ? For random perks like Quantum and Magic 8 Ball, put the average stat over all possibilities.
    # ! Do not include the HOTM tree stats here
    # Components: 455, Yog Armor, Haste Effect, Eager Miner, Scatha, Titanium Artifact, Rotten Pickaxe Attr,
    #             Mithril Equipments, Haste Artifact, Talisman of Power
    # "mining_speed": 1349+332+200+100+125+45+30+104+25+5,
    # "mining_speed": 1349+332+200+100+125+0+30+104+25+5,  # ! Titanium Artifact in Forge
    # "mining_speed": 1349+332+200+100+25+0+30+104+25+5,  # ! Titanium Artifact in Forge
    "mining_speed": 875+332+200+100+25+0+30+104+25+5,  # ! Titanium Artifact in Forge
    # Components: 455, Mineral+Divans, Haste Effect, Eager Miner, Scatha, Rotten Pickaxe Attr,
    #             Mithril Equipments, Haste Artifact, Talisman of Power
    # "mining_speed": 1369+287+200+100+125+30+104+25+5,
    # * Goblin Pet
    "ore_speed": 0,
    # * Mithril Golem Pet
    "mithril_speed": 0,
    # * Mithril and Titanium Equipments
    "dwarven_mines_speed": 30,
    # * Gemstone Drills, Lapidary Enchant
    # Components: Lapidary Enchant
    "gemstone_speed": 40,

    # ? With titanium, assuming the most efficient way:
    # ? leaving the titanium to be potentially mined with
    # ? mining spread with other titaniums around.
    # ? Otherwise mining spread doesn't make titanium mining faster.
    # ? Does not really matter if too much bedrock spawned though.
    # ? Just know that rate is calculated with the best use of
    # ? mining spread on titanium.
    "mining_spread": 0,
    # * Armadillo Pet
    "hardstone_spread": 0,
    # * Goblin Pet
    # ! Only use if the pure ore is mined in there
    "mines_of_divan_spread": 0,
    # * Snail Pet, Fleet Reforge
    "block_spread": 0,
    # * (Glossy) Mineral Armor
    "ore_and_block_spread": 300,

    # * Gemstone Drills, Gemstone Slots, Prismatic, Chilled Pristine Potato
    # Components: 455, Yog Armor
    "pristine": 1+4.8,
    # * Bal Pet
    "magma_fields_pristine": 0,
    # * Glacite Golem
    "corpse_pristine": 0,

    # Components: Mining Skill, 455, Yog Armor, Scatha, Spelunker Effect, Mithril Equipments, Mineral Talisman
    # Components: Refined Dark Cocoa Truffle
    # "mining_fortune": 172+123+140+135+25+24+3+2,
    "mining_fortune": 172+80+140+35+25+24+3+2,
    # * Auspicious
    # Components: Auspicious
    "mining_fortune_mult": 0,
    # * Ore Oats
    # Components: Ore Oats
    "ore_fortune": 10,
    # * Mossy Box, Block Bran, (Glossy) Mineral Armor, Armadillo Mask
    # Components: Mossy Box, Mineral Armor, Block Bran
    "block_fortune": 25+75+10,
    # * Mithraic Reforge
    # Components: Mithril Equipments
    "mithril_fortune": 20,
    # * Titanium Pickaxes, Mithraic Reforge
    "titanium_fortune": 0,
    # * Metallic Minis
    "dwarven_metal_fortune": 0,
    # * Rhinestone Infusion, Gemstone Grahams, Gemstone Drills, Lapidary Enchant
    # ! Include the bonus from Gemstone Equipments if applicable
    # Components: Scatha, Rhinestone Infusion, Lapidary Enchant, Gemstone Grahams
    "gemstone_fortune": 125+20+20+2,
    # * Mithril and Titanium Equipments
    "dwarven_mines_fortune": 5,
    # * Gemstone Equipments
    "crystal_hollows_fortune": 0,
    # * Glacite Golem Pet
    "mineshafts_fortune": 0,
    # * Scraped Reforge
    "scraped_fortune": 0,
    # * Glacial Reforge
    "cold_fortune": 0,
    # * Fortunate Festivity
    "fiesta_fortune": 0,

    # * Titanium Tenacity
    "fiesta_titanium_chance": 0,

    # * Dwarven Training, Silverfish Pet, Prospector's & Scraped & Refined & Dimensional Reforge
    # * Compact & Quantum Enchant, Actually Blue Abicase, Magic 8 Ball, Booster Cookie,
    # * Mining XP Boost Effect, Mayor Cole, Mining Fiesta
    # ! Ignoring Jerry's Workshop Wisdom since XP gain is irrelevant and insignificant.
    # Components: Booster Cookie, Mining XP Boost Effect, Dwarven Training, 455, Yog Armor,
    "mining_wisdom": 25+20+10+9+8,

    # ? Powder Boost bonuses are additive except 2x Powder Event,
    # ?     which doesn't affect the best powder use so ignored.
    # ? All the powder boost and chance values are given in ratio instead of percentage.
    # ? For example, a 20% global powder boost from Omelette is entered as 0.2.
    # * Spicy Goblin Omelette
    "global_powder_boost": 0.2,
    # * Powder Hoarder
    "fiesta_powder_boost": 0,
    # * Mithril Drills, Mithril Golem Pet, Petrified Starfall, Powder Pumpkin
    # Components: 326, Mithril Golem Pet, Powder Pumpkin
    "mithril_powder_boost": 0.40+0.25+0.05,
    # "mithril_powder_boost": 0.25+0.05,
    # * Dimensional Reforge
    "titanium_powder_gain": 40,
    # * Gemstone Drills, Scatha
    # Components: Scatha
    "gemstone_powder_boost": 0.2,
    # * Glacite Golem Pet
    "glacite_powder_boost": 0,
    # * Scatha Pet
    "treasure_chest_chance": 0.5,

    "using_blue_cheese": False,

    # ! Mining Wisdom from Compact Enchant is added manually.
    "compact_level": 10,
    # ? Simplified as always being maxed, so 200*level of MS
    # ? If your mining process is doing dwarven mines commissions
    # ? or travelling in tunnels where you might break the stack repetitively,
    # ? set it to your average flowstate stacks,
    # ? like 1.5 for an actual level of 3 for better results.
    "flowstate_level": 3,

    # ! Those two are currently unused for the optimization.
    # ! Will be supported in the future.
    # * Bal Pet, Heat Armor, Flamebreaker Armor, Yog Armor, Armor of Divan, Blazing Reforge
    "heat_resistance": 40,
    # * Glacite Golem & Mammoth Pet, Reaper Peppers, Dwarven Handwarmers, Pendant of Divan
    # * Ice Cold Enchant, Cold Resistance Effect
    "cold_resistance": 0,

    # ! Mineral mode not supported yet.
    # * Refined Mind
    "mineral_chance": 0,

    "heart_of_the_mountain": 8,
    "core_of_the_mountain": 7,

    "mithril_powder": 1750728,
    "gemstone_powder": 14827174,
    "glacite_powder": 89402,

    "breaking_power": 8,

    # ! blocks and ores outside mining islands are ignored
    # ! since it's just dumping powder into mining fortune
    # * ores, powder, exp
    # ? commissions and fiesta modes not supported yet
    # * ores: block, ore, mithril, titanium, glacite
    # *     : ruby, amber, topaz, jasper, aquamarine
    # ? block mode assumes instamining, use gemstone powder mode for hardstone
    # ? ore=pure diamond=pure redstone=...
    # ? amber=amethyst=jade=opal=sapphire, aquamarine=citrine=onyx=peridot, glacite=umber=tungsten
    # ? Remember to add the gemstone fortune from Gemstone Equipments if applicable
    # ! commissions mode is not supported yet since titanium, gemstone and metal mode could be used instead.
    # * powders: mithril, gemstone, glacite
    # * fiesta ores: refined_mineral, glossy_gemstone
    # ? but fiesta ores can be dropped with powder setup to mine titanium, gemstone and metal mode
    # * exp mode requires the ore to be specified for the mining wisdom to be considered upon it.
    # * titanium exp
    # "mode": "ores",
    # "ore": "ore",
    "mode": "powder",
    "ore": "titanium",
    # ? Using precursor remnants chest powder gain for gemstone powder
    "powder_type": "mithril",
    # * Toggles if drops should be optimized along powder rate.
    # ? This is always on even when set as False in ores mode
    # ? and this works for hardstone in gemstone powder mode.
    # ? This should be only off to support aggressively powder grinding
    # ? for mithril or gemstone that you don't care about fortune.
    "consider_fortune": True,
    # * Toggles fiesta titanium chance and powder boost
    "is_fiesta": False,
    # * Whether to consider titanium chance for ironman/goldenman/commissions purposes.
    # * Should also be on for mithril powder grinding with Dimensional reforge.
    # ? Should be turned off for purposes unrelated to titanium.
    "use_titanium": True,
    # "use_titanium": False,
    # * Also calculates the time taken if target amount is specified.
    "target_amount": None,
    # * Toggles the calculation to work for redstone/lapis with 9 base drop instead of 5
    "is_amplified": False,
    # * Forces ability if specified.
    # ! Abilities are ignored for the rates optimization.
    # ! Will be supported in the future.
    # ! Auto tree is also not supported yet, so a given tree
    # ! should be provided below to start the optimization.
    "force_ability": None,
    # * Uses the tree if given, data should be an iterable with the node names.
    "given_tree": (
        "mining_speed", "mining_fortune", "titanium_insanium", "pickobulus", "efficient_miner",
        "sky_mall", "old_school", "professional", "mole", "core_of_the_mountain",
        "blockhead", "subterranean_fisher", "keep_it_cool", "lonesome_miner",
        "great_explorer", "speedy_mineman", "powder_buff",
        "fortunate_mineman", "steady_hand", "strong_arm",
    ),
    # ? Here are some of the presets that I'm using for optimizing for my HOTM purposes.
    # ? You can use from those
    # H7C7 Ores
    # "mining_speed", "mining_fortune", "efficient_miner",
    # "sky_mall", "old_school", "professional", "mole", "seasoned_mineman",
    # "daily_grind", "core_of_the_mountain", "daily_powder",
    # "blockhead", "subterranean_fisher", "keep_it_cool",
    # "lonesome_miner", "great_explorer", "maniac_miner",
    # "speedy_mineman", "powder_buff", "fortunate_mineman",
    # H7C7 Gemstone without Heat Resistance
    # "mining_speed", "mining_speed_boost", "precision_mining", "mining_fortune",
    # "efficient_miner", "professional", "mole", "gem_lover", "seasoned_mineman",
    # "front_loaded", "core_of_the_mountain", "blockhead", "subterranean_fisher",
    # "keep_it_cool", "lonesome_miner", "great_explorer", "speedy_mineman",
    # "fortunate_mineman",,
    # H7C7 Mithril Powder while Titanium
    # "mining_speed", "mining_fortune", "titanium_insanium", "efficient_miner",
    # "sky_mall", "old_school", "professional", "mole", "core_of_the_mountain",
    # "blockhead", "subterranean_fisher", "keep_it_cool", "lonesome_miner",
    # "great_explorer", "maniac_miner", "speedy_mineman", "powder_buff",
    # "fortunate_mineman",
}
