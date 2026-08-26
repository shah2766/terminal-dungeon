# Terminal Dungeon ⚔️ 

## Description

Terminal Dungeon is a command-line, turn-based dungeon RPG written in Python and developed as my CS50x Final Project.

The game places the player inside a dangerous dungeon where they must make decisions about exploration, combat, risk, and resource management. The player progresses through a series of chambers, encounters different enemies, earns experience and gold, collects potions, levels up, and eventually faces the final boss, the Dread Lord.

I created Terminal Dungeon as a way to apply the programming concepts I learned throughout CS50x to a larger interactive program. Instead of building a small isolated exercise, I wanted to create a project where multiple systems work together and where the player can make meaningful decisions during a game.

The game is intentionally built as a terminal application using Python's standard library. The current implementation uses functions and dictionaries to organize the game's different systems and state.

## How the Game Works

At the beginning of a run, the player starts with 100 HP, Level 1, 0 XP, and 0 Gold. The player may also begin with a small number of Health Potions.

The dungeon contains multiple chambers. In each chamber, the player chooses how to proceed:

```text id="7o8zfa"
1) 🛡️ Quiet Passage
2) 🔥 Blood Trail
3) 🔎 Search the Ruins
4) 🚪 Leave the Dungeon
```

The Quiet Passage provides lower-risk encounters with lower rewards, while the Blood Trail increases both danger and rewards. Searching the ruins can provide Health Potions, Gold, Super Potions after Level 10, or nothing useful.
The player progresses by surviving encounters and increasing the chamber number. After the final chamber, the player faces the Dread Lord.

## Combat

Combat is turn-based. The player has four choices:

```text id="k6oyee"
1) ⚡ Quick Attack
2) 🪓 Heavy Attack
3) 🧪 Use Potion
4) 🏃 Run
```

Quick Attack deals a moderate amount of reliable damage. Heavy Attack deals more damage but has a 25% chance to miss. Using a potion restores HP, while running ends the current encounter.

After a successful player action, the enemy attacks if it is still alive. If the player's HP reaches zero, the encounter ends in defeat. The `combat()` function returns `"win"`, `"lose"`, or `"run"` so that the main game loop can decide what happens next.

## Enemies

The game currently includes four enemy types:

| Enemy     |     HP | Damage | XP | Gold |
| --------- | -----: | -----: | -: | ---: |
| Goblin    |  20–50 |   3–10 | 10 |   10 |
| Skeleton  |  30–65 |   5–12 | 20 |   20 |
| Orc       |  50–90 |   8–16 | 30 |   30 |
| Elite Orc | 80–120 |  12–20 | 45 |   45 |

Enemy selection depends on the player's chamber. Early chambers are weighted toward Goblins and Skeletons, middle chambers contain more Orcs, and later chambers increase the chance of encountering Elite Orcs.

The Safe and Dangerous paths then modify an enemy's HP, damage, XP, and Gold depending on the player's choice.

## Character Progression

The player earns XP by defeating enemies.

The amount of XP needed for the next level is calculated using:

```text id="3x1o7y"
XP required = Level × 50
```

When the player reaches the required amount of XP, they level up. A level-up increases maximum HP by 10 and fully restores the player's HP. Every even-numbered level also provides one Health Potion. At Level 10, the Super Potion becomes unlocked.

This system gives the player an incentive to continue exploring while gradually making the character stronger.

## Potion System

Terminal Dungeon has two potion types.

### Health Potion

A Health Potion restores up to 30 HP without allowing the player to exceed maximum HP.

### Super Potion

A Super Potion restores up to 50% of the player's maximum HP. It becomes available after reaching Level 10 and can also be discovered through certain late-game supply or loot events.
Using a potion consumes the player's combat action because the combat system continues to the enemy's turn after a successful potion use.

## Rewards and Loot

Defeating an enemy awards XP and Gold. There is also a chance of receiving additional loot after combat.

The current loot system can provide Health Potions and, after Level 10, Super Potions.

The Search the Ruins event provides another way to obtain resources. Depending on the result of a random roll, the player may receive a Health Potion, Gold, a Super Potion if eligible, or nothing.

## Final Boss

After the player progresses beyond the final chamber, the game starts the final boss encounter.

The boss is the **Dread Lord**, with 220 HP, 18 damage, 120 XP, and 150 Gold. The boss uses the same combat system as normal enemies but has significantly stronger statistics and special presentation.

If the player defeats the Dread Lord, the run ends with a victory screen and the player receives the boss's XP and Gold rewards. If the player loses, the dungeon claims them and the run ends.

## Randomness and Player Choice

Randomness is an important part of the game. It is used for enemy statistics, enemy selection, supply searches, loot drops, and combat damage.
However, the game does not rely entirely on randomness. The player can choose between safer and more dangerous paths, decide whether to search for supplies, choose different combat actions, use limited potions, or retreat from an encounter.

The intention is to combine unpredictable events with meaningful decisions so that the player has some control over how they approach each run.

## User Interface

Because Terminal Dungeon is a terminal-based application, text is an important part of the game's presentation.

The project includes several UI helper functions:

* `slow_print()` creates a typewriter-style text effect.
* `divider()` creates visual separators.
* `section()` creates consistent section headings.
* `hp_bar()` displays health as a visual bar.
* `pause()` adds controlled delays for dramatic moments.

These functions are separated from the game logic so that the presentation can be changed without rewriting the underlying mechanics.

## Project Structure

```text id="1n8j6a"
terminal-dungeon/
│
├── main.py
└── README.md
```

### `main.py`

`main.py` contains the complete implementation of Terminal Dungeon.

It includes:

* UI helper functions
* XP and level progression
* Enemy generation
* Exploration path modifiers
* Supply-search events
* Loot drops
* Potion management
* Combat
* Final boss logic
* Player HUD
* Main game loop
* Main menu

The major functions are separated by responsibility so that different parts of the game can be modified independently.

### `README.md`

This file documents the project, explains how the game works, describes its major systems and design choices, and provides instructions for running the project.

## Design Choices

One of the main design decisions was to represent the player and enemies using Python dictionaries rather than classes. The project originally started as a smaller procedural program, so dictionaries provided a simple way to group related attributes such as HP, damage, XP, and Gold.

As the project became larger, I separated different responsibilities into individual functions. For example, combat is handled by `combat()`, potion management by `use_potion()`, enemy generation by `create_enemy()`, and progression by `level_up_check()`. This made the game easier to reason about and allowed individual systems to evolve without putting all the logic into one function.

Another important design decision was to reuse the same `combat()` function for both normal enemies and the final boss. This avoids duplicating the combat system while still allowing the boss to have different statistics and presentation.

The project also intentionally separates dungeon progression from player progression. The chamber number controls the types of enemies that can appear, while the player's level controls character strength, XP progression, and potion availability.

## Technologies Used

* Python 3
* `random`
* `time`

Both modules are part of Python's standard library, so no third-party packages are required.

## Installation and Usage

Clone the repository:

```bash id="0m9hrh"
git clone https://github.com/shah2766/terminal-dungeon.git
```

Change into the project directory:

```bash id="l9wq63"
cd terminal-dungeon
```

Run the game:

```bash id="i8y5g2"
python3 main.py
```

The project is designed to run directly in a terminal.

## Development

Terminal Dungeon started as a small combat prototype and was gradually expanded into a larger game.

The development process involved adding one system at a time and testing how each new piece affected the existing game. This resulted in separate systems for exploration, combat, progression, potions, loot, and the final boss.

The project also became an exercise in debugging program state. As the game grew, I had to distinguish between data that belonged to a single enemy encounter, data that belonged to a complete dungeon run, and data that represented long-term player progression.

## Future Improvements

The project is currently a playable prototype. Possible future improvements include:

* Refactoring the game into an object-oriented architecture
* Expanding the inventory system
* Adding weapons and equipment
* Adding more enemy and boss mechanics
* Improving combat balance
* Adding persistent save/load functionality
* Expanding the variety of dungeon events
* Adding additional strategic choices
* Improving terminal presentation further

## Conclusion

Terminal Dungeon was created to turn the programming concepts learned in CS50x into a larger, interactive software project.

The game combines Python functions, dictionaries, loops, conditional logic, randomization, state management, user input, and modular program structure in a single application.

More importantly, the project gave me practical experience designing a system incrementally, debugging unexpected behavior, thinking about program state, and deciding how separate pieces of functionality should interact.

