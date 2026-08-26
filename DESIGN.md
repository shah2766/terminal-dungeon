# Terminal Dungeon — Design Document

## 1. Project Overview

Terminal Dungeon is a command-line, turn-based dungeon RPG written in Python.

The game is structured around a repeated dungeon progression loop. The player enters the dungeon, chooses an exploration option, encounters events or enemies, manages health and resources, gains XP and Gold, levels up, and eventually reaches a final boss.

The project currently uses procedural Python programming with functions and dictionaries. The code is divided into separate functional areas so that user-interface behavior, combat, progression, enemies, potions, and the game loop are not all implemented in one large function.

## 2. Overall Architecture

The program is divided into the following major components:

```text id="n2qf4y"
UI Helpers
    slow_print()
    divider()
    section()
    hp_bar()
    pause()

Core Progression
    xp_needed_for_next_level()
    level_up_check()

Enemies & Events
    create_enemy()
    apply_path_modifiers()
    supply_search()
    maybe_drop_loot()

Potion System
    use_potion()

Combat
    combat()

Boss
    boss_fight()

Game
    show_player_hud()
    start_game()
    main_menu()
```

Each section has a specific responsibility.

## 3. Player State

The player is represented by a dictionary.

The current player data contains:

```python id="hbhp9u"
{
    "hp": 100,
    "max_hp": 100,
    "level": 1,
    "xp": 0,
    "gold": 0,
    "health_potions": ...,
    "super_potions": 0
}
```

A dictionary was chosen because the project began as a small procedural program and the player has a relatively small number of related attributes.

Using descriptive keys such as `"hp"`, `"level"`, and `"gold"` makes the state easy to access and modify.

## 4. Dungeon Progression

The dungeon is represented by a chamber counter called `depth`.

The game begins at:

```python id="qf8skl"
depth = 1
```

and progresses until it passes the configured final depth:

```python id="d9ct9m"
final_depth = 8
```

The depth controls which enemies are likely to appear.

Early chambers use a pool weighted toward Goblins and Skeletons. Middle chambers increase the chance of Orcs, while later chambers increase the chance of Elite Orcs.

This gives progression a direct impact on difficulty while retaining randomness.

## 5. Exploration Choices

Each chamber presents four choices:

```text id="s2shiu"
1. Quiet Passage
2. Blood Trail
3. Search the Ruins
4. Leave the Dungeon
```

The Quiet Passage reduces enemy HP, damage, XP, and Gold.

The Blood Trail increases enemy HP, damage, XP, and Gold.

This creates a risk-versus-reward mechanic.

The Search the Ruins action does not create an enemy. Instead, it performs a randomized supply search that may provide a potion, Gold, a Super Potion after Level 10, or nothing.

## 6. Enemy Model

Enemies are dictionaries containing:

```text id="7gppad"
name
hp
damage
xp
gold
```

Four enemy types currently exist:

* Goblin
* Skeleton
* Orc
* Elite Orc

The `create_enemy()` function constructs these enemies and chooses from an appropriate enemy pool based on dungeon depth.

After an enemy is selected, `apply_path_modifiers()` changes its statistics depending on the player's chosen path.

## 7. Combat System

The combat system is implemented by the `combat(player, enemy)` function.

A combat encounter continues while both the player and enemy have positive HP.

The player can choose:

```text id="0m7d0p"
1. Quick Attack
2. Heavy Attack
3. Use Potion
4. Run
```

Quick Attack deals random damage between 6 and 12.

Heavy Attack deals random damage between 12 and 20 but has a 25% chance to miss.

Potion use is delegated to `use_potion()`.

Running returns `"run"` immediately.

After a successful player action, the enemy receives its turn if it is still alive.

Combat returns one of three result values:

```text id="zp5e4w"
"win"
"lose"
"run"
```

This allows the higher-level game loop to decide what to do after combat without embedding exploration logic inside the combat function.

## 8. Progression System

XP required for the next level is calculated by:

```python id="w68bwa"
return level * 50
```

When the player's XP reaches the next threshold, `level_up_check()` increases the player's level, increases maximum HP by 10, and restores HP to maximum.

Every even-numbered level awards one Health Potion.

Level 10 unlocks the Super Potion.

A `while` loop is used inside `level_up_check()` so that the function can handle multiple level increases if a large amount of XP is awarded.

## 9. Potion System

The game contains two potion types.

### Health Potion

Health Potions restore 30 HP, with the player's HP capped at maximum HP.

### Super Potion

Super Potions restore half of the player's maximum HP, also capped at maximum HP.

The `use_potion()` function handles:

* Displaying the player's potion inventory
* Accepting the player's selection
* Checking whether a potion is available
* Updating potion counts
* Updating player HP
* Returning whether a potion was successfully used

## 10. Loot System

After defeating an enemy, `maybe_drop_loot()` performs a random loot roll.

There is currently a chance to receive a Health Potion and a smaller chance to receive a Super Potion once the player has reached Level 10.

The Supply Search system independently uses random results to award resources.

This creates multiple ways for the player to recover resources and continue a dungeon run.

## 11. Boss System

The final boss is represented by the Dread Lord.

The boss is created inside `boss_fight()` with its own HP, damage, XP, and Gold.

Instead of duplicating the combat system, `boss_fight()` calls:

```python id="9m4d7c"
combat(player, boss)
```

This was a deliberate design choice. Normal enemies and the boss share the same fundamental combat mechanics, so maintaining a single combat function avoids duplicate logic.

The boss function is responsible for:

* Creating the boss
* Presenting the final encounter
* Calling combat
* Awarding boss rewards
* Displaying victory or defeat

## 12. UI Architecture

The project uses several small functions to improve terminal presentation.

`slow_print()` produces a typewriter effect.

`divider()` and `section()` provide consistent section formatting.

`hp_bar()` displays health visually.

`pause()` creates short dramatic delays.

Separating these helpers from game logic means that presentation can be modified without rewriting combat or progression.

## 13. Randomness

Randomness is used throughout the game:

* Enemy HP
* Enemy damage
* Enemy selection
* Supply searches
* Loot drops
* Player attack damage
* Heavy Attack accuracy

Randomness gives each run variation.

However, randomness is constrained by dungeon progression and player choices. Enemy pools change depending on depth, while Safe and Dangerous paths allow the player to choose how much risk they are willing to take.

## 14. Design Decisions

### Why dictionaries?

The project started as a procedural Python program. Dictionaries provided a simple and readable way to represent structured game state.

For example:

```python id="pm8kpi"
enemy["hp"]
enemy["damage"]
enemy["xp"]
```

As the project grows, the player and enemy dictionaries could eventually become classes.

### Why separate functions?

Different game systems have different responsibilities.

For example, the combat system should not need to know how the main menu works. Similarly, the potion system should not need to create enemies.

Separating functions makes the program easier to debug and modify.

### Why reuse `combat()` for the boss?

The boss follows the same fundamental rules as normal enemies. Reusing the combat system avoids duplicating code and allows future changes to combat to affect both normal enemies and the boss.

### Why use randomness?

Randomness makes repeated runs less predictable and increases replayability. The game combines random outcomes with player decisions to avoid making every result completely deterministic.

## 15. Current Limitations

The current project is still a functional prototype.

The code remains procedural and uses dictionaries rather than a class-based architecture. The game also does not currently provide persistent save/load functionality.

The current version focuses on demonstrating a complete playable loop rather than implementing a large number of advanced systems.

## 16. Future Improvements

Possible future improvements include:

* Object-oriented refactoring
* Expanded inventory and equipment systems
* Weapons and armor
* Additional combat mechanics
* More enemies and bosses
* Persistent save/load functionality
* More advanced dungeon events
* More detailed player progression
* Improved balancing
* Additional terminal presentation effects

## 17. Conclusion

Terminal Dungeon was developed incrementally from a simple terminal combat prototype into a larger game containing exploration, combat, progression, resources, events, loot, potions, and a final boss.

The architecture intentionally separates major systems into functions while keeping the data structures simple enough to understand.

The project demonstrates how a collection of basic programming concepts can be combined into a larger interactive application and provides a foundation for future refactoring and expansion.
