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
    "mining_speed": 0,
    # * Goblin Pet
    "ore_speed": 0,
    # * Mithril Golem Pet
    "mithril_speed": 0,
    # * Mithril and Titanium Equipments
    "dwarven_mines_speed": 0,
    # * Gemstone Drills, Lapidary Enchant
    "gemstone_speed": 0,

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
    "ore_and_block_spread": 0,

    # * Gemstone Drills, Gemstone Slots, Prismatic, Chilled Pristine Potato
    "pristine": 0,
    # * Bal Pet
    "magma_fields_pristine": 0,
    # * Glacite Golem
    "corpse_pristine": 0,

    "mining_fortune": 0,
    # * Auspicious
    "mining_fortune_mult": 0,
    # * Ore Oats
    "ore_fortune": 0,
    # * Block Bran, (Glossy) Mineral Armor, Armadillo Mask
    "block_fortune": 0,
    # * Mithraic Reforge
    "mithril_fortune": 0,
    # * Titanium Pickaxes, Mithraic Reforge
    "titanium_fortune": 0,
    # * Metallic Minis
    "dwarven_metal_fortune": 0,
    # * Rhinestone Infusion, Gemstone Grahams, Gemstone Drills, Lapidary Enchant
    # ! Include the bonus from Gemstone Equipments if applicable
    "gemstone_fortune": 0,
    # * Mithril and Titanium Equipments
    "dwarven_mines_fortune": 0,
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
    # ! Ignoring Jerry's Workshop Wisdom since XP gain is irrelevant and insignificant
    "mining_wisdom": 0,

    # ? Powder Boost bonuses are additive except 2x Powder Event,
    # ?     which doesn't affect the best powder use so ignored
    # ? All the powder boost and chance values are given in ratio instead of percentage.
    # ? For example, a 20% global powder boost from Omelette is entered as 0.2.
    # * Spicy Goblin Omelette
    "global_powder_boost": 0,
    # * Powder Hoarder
    "fiesta_powder_boost": 0,
    # * Mithril Drills, Mithril Golem Pet, Petrified Starfall, Powder Pumpkin
    "mithril_powder_boost": 0,
    # * Dimensional Reforge
    "titanium_powder_gain": 0,
    # * Gemstone Drills, Scatha
    "gemstone_powder_boost": 0,
    # * Glacite Golem Pet
    "glacite_powder_boost": 0,
    # * Scatha Pet
    "treasure_chest_chance": 0,

    "using_blue_cheese": False,

    # ! Mining Wisdom from Compact Enchant is added manually
    "compact_level": 0,
    # ? Simplified as always being maxed, so 200*level of MS
    # ? If your mining process is doing dwarven mines commissions
    # ? or travelling in tunnels where you might break the stack repetitively,
    # ? set it to your average flowstate stacks,
    # ? like 1.5 for an actual level of 3 for better results.
    "flowstate_level": 0,

    # ! Those two are currently unused for the optimization.
    # ! Will be supported in the future.
    # * Bal Pet, Heat Armor, Flamebreaker Armor, Yog Armor, Armor of Divan, Blazing Reforge
    "heat_resistance": 0,
    # * Glacite Golem & Mammoth Pet, Reaper Peppers, Dwarven Handwarmers, Pendant of Divan
    # * Ice Cold Enchant, Cold Resistance Effect
    "cold_resistance": 0,

    # ! Mineral mode not supported yet.
    # * Refined Mind
    "mineral_chance": 0,

    "heart_of_the_mountain": 1,
    "core_of_the_mountain": 0,

    "mithril_powder": 0,
    "gemstone_powder": 0,
    "glacite_powder": 0,

    "breaking_power": 5,

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
    "mode": "ores",
    "ore": "titanium",
    # ? Using precursor remnants chest powder gain for gemstone powder
    "powder_type": None,
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
        "mining_speed",
    ),
}
