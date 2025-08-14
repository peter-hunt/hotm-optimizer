# Hypixel Skyblock HOTM Optimizer

![](https://img.shields.io/github/repo-size/peter-hunt/hotm-optimizer)
![](https://img.shields.io/badge/license-CC_BY_4.0-green)
![](https://img.shields.io/github/issues/peter-hunt/hotm-optimizer)
![](https://img.shields.io/github/stars/peter-hunt/hotm-optimizer)

Optimizer for HotM (Heart of the Mountain) powder distribution made as of Hypixel Skyblock 0.23.3. A python version of at least 3.9 is expected to work version 3.13.5 is recommended for best stability since that's the version used for development.

The code looks for the best way to spend the powders in terms of levels to go for for each HOTM node with your total powder in terms of some task you tell the code to optimize for, like either powder mining or ore mining. This is only significant before you have maxed powder, however, since otherwise you will just get the max levels for all relevant nodes. The usage, limitations and future plans of the optimizer is explained in the following sections.

For simplicity of the code, a lot of the config data is not checked automatically, which is also partially since you can break the code in a lot of ways with the config file and you would just put valid data if you actually want to optimize your HOTM tree anyway. So, if you put 200 mining speed and -100 mithril speed for titanium mining, the code work will but will not lead to a significant optimization solution since the initial data is invalid, unless you just mean an initial 100 mining speed anyway. On the other hand, if you put -10000 mining speed, you are likely hit with the error saying `ValueError: something is wrong and the best purchase hurts score` anyway. **In short, the code will not catch you for throwing invalid config numbers; but for an optimizer usage, make sure to check your config and compare with the given example or init if necessary as to make it work properly.**

And similarly, the code will not check for if the nodes in the given tree is connected, yet. If you put all the relevant nodes in the optimizer as the given tree, the optimizer will optimize for it but you will not be able to use it anyway.

## Usage

If you need to install a modern version of Python or check/find the correct version to run the project, view the Python Support section below.

If you're not sure how to edit the values in the config to, view the Python Support section below.

You can check your stats breakdown in the Skyblock Menu -> Your Skyblock Profile -> Gathering Stats on the right. In there, the components of the mining stats that you have is broken down, which you can check easier whether if there is something like the mining speed from Gone with the Wind event that you should not add to the config.

To start, edit the `config.py` data to your in-game stats. Follow the instructions and review the given example `config.py` for the integer/percentage formats and what should be added. Go into the stats break down in the menu after HOTM is reset to avoid event stats messing up the stats. And make sure to include additional related stats like mineral specific or regional stats. **Copy from the `config_init.py` for a clean copy to get started with to avoid incorrect default values from the `config.py`.** Remember to update the stats whenever you get an upgrade in the items or have a decent amount of extra powder available. Remember that the total powder is the powder that you have plus the total you will get back from respecing the HOTM tree (just so you can see how much an increase it is from your current stats should you use the optimized result and decide if you wish to switch otherwise), or just the plain numbers after respecing.

A reminder that **the code doesn't automatically generate the best HOTM tree based on your HOTM/COTM levels yet and will require manually putting the used nodes**. You can do so by **entering the code name for the HOTM nodes under the `"given_tree"` value**, and you can **check for the code names for other nodes in the `data/hotm_tree.json` if not shown in the example**. This is due to the ability calculation not implemented in the main optimizer code yet, and that it gets more complicated with the code when you have to try all possible trees when you don't have enough tokens for all relevant perks. Don't worry, this will be implemented at some point in the future though, although the option of using a given tree will be supported just in case you have so much mana that you love Maniac Miner over anything else.

**Be careful that the `config_init.py` content will not work without your editing to put in your own stats as the mining speed is set to zero.**

A coding IDE like VSCode is recommended to edit and config the files. However, simpler setups like textedit to edit the `config.py` and running the code from terminal works, although textedit will not tell you when you enter the wrong Python value. In addition, the project folder includes the `.vscode` hidden folder for the settings of the Better Comments Extension by Aaron Bond for coloring the comments in the `config.py`, so VSCode is again recommended to use this project.

The mode and ores are all configured in the `config.py`. Run `main.py` with your IDE or with the following command in terminal in the project folder:

```bash
python3 main.py
```

### Python Support

If you don't have Python yet or your system Python is too outdated, go to the [official Python download webpage](https://www.python.org/downloads/) to get the latest version or the recommended 3.13.5 for running this project if the newest one doesn't work. Once the install package is downloaded, run it and follow the instructions in the download window. Once Python is downloaded, with a restarted terminal or a new terminal window, enter `python3` or with the corresponding version name, like `python3.13` to see if it's downloaded properly. If `python3` is linked to some older version of Python like 3.9.6, use `python3.13` or your newer version for the terminal command above.

- For the numbers in the relevant fields, enter the numbers either as integers or float numbers, like `123`, `4.5`, or `0.05`.
- The boolean values, or the Trues and Falses, are to switch a mode on or off, where obviously True is on and False is off. And for those, the Python literal for those are the capitalized word `True` or `False`.
- For some optional values where you don't have to put, enter the capitalized word `None` for an empty value.

Feel free to experiment with the confg files and don't be afraid to break it, since the worst case scenario is you copying the config from the template again and editing it again.

## Limitations (Nerdy Alert)

This part and the algorithms todo list explains on the implementation, limitations and future plans for the algorithm, which is quick nerdy for those.

The algorithm of the optimizer current start from an empty tree and always make the purchase with the highest ratio of powder spent and the linear efficiency increment. This **DOES NOT** currently find the best optimization for the given powder and tasks for the highest efficiency but is efficient in the algorithm implementation and runtime that it's guaranteed to generate a result instantly, thus the implementation of the current algorithm. However, due to the polynomial increment of powder costs, the benefits of the actual global maixmum will be much smaller than the different between using some random HOTM setup and using this optimizer anyway, but still room for improvements.

For those who are unfamiliar with **local maximums** and the **global maximum**, those are two terms commonly used in the realm of optimization problems. For an optimization problem, usually based on or related to math, consider the effectiveness or efficiency which you are optimizing for as some complicated surfaces to climb onto and find the highest point for. Unlike mountains, however, you cannot simply see the other points and see the highest point of the mountain easily, as that would require basically brute-forcing the solution, aka. trying all possible setups, which would be computationally inefficiency and against the goal of the optimization to find a good or the best solution efficiently. In math, the gradient of a multivariable function allows us to calculate the direction of the surface at a given point, and thus the best direction to go in for the fastest ascension. The global maximum is like the highest point of the mountains that everybody is trying to find. On the other hand, local maximums are points where you might get stuck with since every direction is downhill. And here, the current algorithm implementation is like going to the maximum height in the north-south direction, like the gemstone powder, and going from there to the maximum height in the east-west direction, like the mithril powder, which you can tell might not be the global maximum since the ridge probably doesn't go in the east-west direction.

A specific case of whenever one type of powder is maxed for the relevant perks, such as having maxed gemstone powder for mithril powder grinding but not maxed mithril powder for the task yet, all the gemstone powder is spent first since then the usage of the mithril powder in the algorithm will be better suited to tune the stats instead of going in the local maximum direction at the start with the speed/fortune/spread balance and so on.

In addition, as there are discrete improvements in the hypixel mechanics such as mining ticks and in HOTM tree such as the Great Explorer with the lock picking decreasing every 5 levels, the optimizer considers them as smooth curves for an easier time for the efficiency-cost ratio calculation. In turn, this would lead to situations where the result would not go for maxed Great Explorer but only level 19 where maxing it would be so much better. However, this doesn't affect much of the mining speed ticks, and the Great Explorer should pretty much always be prioritized as a powder dump at the start of gemstone powder mining. In addition, aspects of the game like Gone with the Wind event, Precision Mining perk, reaction speed and so on affect the efficiency much more than the mining tick, so this will not be put on much work in the short term.

## Todo List

### Features

- To check for data validity and tree validity;
- To support automated tree searching, which allows testing for the best ability for the current stats and powder;
- Alternatively, to provide some HOTM tree presets in the config.py below for each HOTM level with sufficient COTM for tokens for each purposes at each level and the powder required to max the tree;
- To include the calculation of abilities for optimization;
- To support dwarven commissions mode with averaging the different mining tasks;
- To overall support tunnels and mineshaft more accurately based on endgame methods;
- To support heat resistance and cold resistance better;
- To support Fiesta Mineral mode.

### Algorithms (Nerdy Alert)

- To find a global maximum based on the evaluation;
- Potentially to suport the config stats calculation to be automatic from more input but an easier time;
- To show when a better purchase could be waited for and what the future purchases are if the current task would generate a lot of powder;
- To potentially refine the reaction speed calculation;
- To support optimizing a tree over a task that the pet would level up during;
- To extract even the formulas and mechanics into editable data files, where this could then support rapid mechanics change that Skyblock probably won't have or even optimizing for other tasks like HOTF or other games completely with the change of the mechanics data files.

### Potential Future Projects

- Combat/Fishing/Mining/Foraging profit increment versus cost optimizer.

## Support for Future Skyblock Changes

This project is organized so that the mechanics is implemented in the code and the data are all editable in the files under the data folder, so it could be easily updated if Hypixel chooses to change some powder exponents or the stats gain from a node. The stats from the items and so on are already manually entered from the config, so they can also be modified easily.

## The History of PeterHunt's Previous HOTM Optimizer and the Potentials for This.

It became too long and I had to move it here: [History](./HISTORY.md)

## License

This project is under the Creative Commons Attribution 4.0 International License, which allows you to share or create based on this project while giving appropriate credits.

[CC BY 4.0](./LICENSE.txt)

The license to allow you guys to share and use the project but having to credit me in case you decide to build up from this and choose to credit me would be a great motivation for me to create more open-sourced tools and resources for Skyblock and potentially even more in the future. I have looked for HOTM optimizers but never found one that did what I expected, and there are other tools like bazaar/AH flipping trackers which just didn't really fit my need (and also just me not being a big bazaar/AH flipper myself), but I would create some more personalized trackers like those if I would help more Skyblock players with it.

## My Patreon

- [My Patreon Page](https://patreon.com/pypeterhunt)
