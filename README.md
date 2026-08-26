# Terminal Dungeon ⚔️

A terminal-based dungeon RPG built with Python.

**Terminal Dungeon** is a small turn-based adventure game where the player explores a dangerous dungeon, chooses between different paths, fights enemies, collects XP and gold, uses potions, levels up, and eventually faces a final boss.

The project was built as a hands-on Python learning project, with a focus on program structure, game-state management, control flow, randomization, and gradually developing a larger application from scratch.

## Features

* 🏰 Multi-stage dungeon exploration
* 🛡️ Safe and dangerous exploration paths
* 🔎 Supply-search events
* 👹 Multiple enemy types

  * Goblin
  * Skeleton
  * Orc
  * Elite Orc
* ⚔️ Turn-based combat
* ⚡ Quick Attack
* 🪓 Heavy Attack with a chance to miss
* 🧪 Health Potions
* 🌟 Super Potions
* ⭐ XP and character leveling
* ❤️ Increasing maximum HP through level progression
* 💰 Gold rewards
* 🎁 Random loot drops
* 👑 Final boss encounter
* 🎬 Typewriter-style text effects and terminal UI
* 🔄 Replayable runs with randomized encounters

## Gameplay

Each dungeon run begins with a fresh character and a set of basic stats:

```text
HP
Level
XP
Gold
Health Potions
Super Potions
```

As the player progresses through the dungeon, each chamber presents several choices:

```text
1. 🛡️ Quiet Passage
2. 🔥 Blood Trail
3. 🔎 Search the Ruins
4. 🚪 Leave the Dungeon
```

Different choices affect the difficulty and rewards of the encounters.

### Combat

When an enemy appears, the player can choose from several actions:

```text
1. ⚡ Quick Attack
2. 🪓 Heavy Attack
3. 🧪 Use Potion
4. 🏃 Run
```

Quick Attacks provide reliable damage, while Heavy Attacks deal more damage but have a chance to miss.

Defeating enemies rewards the player with:

* XP
* Gold
* A chance to find additional items

## Character Progression

The player gains XP by defeating enemies.

When enough XP is collected, the player levels up and:

* Maximum HP increases
* HP is fully restored
* Health Potions are awarded at certain levels
* The Super Potion becomes available at Level 10

The current XP progression follows:

```text
Level 1 → 50 XP
Level 2 → 100 XP
Level 3 → 150 XP
...
```

## Potions

### Health Potion

Restores up to **30 HP** without exceeding maximum HP.

### Super Potion

Restores up to **50% of maximum HP** and is unlocked at **Level 10**.

Potions can be used during combat and consume a turn.

## Enemies

Enemy difficulty increases as the player progresses deeper into the dungeon.

| Enemy     |     HP | Damage | XP | Gold |
| --------- | -----: | -----: | -: | ---: |
| Goblin    |  20–50 |   3–10 | 10 |   10 |
| Skeleton  |  30–65 |   5–12 | 20 |   20 |
| Orc       |  50–90 |   8–16 | 30 |   30 |
| Elite Orc | 80–120 |  12–20 | 45 |   45 |

Enemy statistics and encounters contain randomized elements, making individual runs different from one another.

## Final Boss

After progressing through the dungeon, the player eventually reaches the final area and faces:

**The Dread Lord 👑**

The final boss has significantly higher health and damage and provides a large XP and gold reward.

Defeating the boss completes the dungeon run.

## Running the Game

### Requirements

* Python 3.x

The game uses only Python's standard library, so no external packages are required.

### Run locally

Clone the repository:

```bash
git clone https://github.com/shah2766/terminal-dungeon.git
```

Navigate to the project directory:

```bash
cd terminal-dungeon
```

Run the game:

```bash
python3 main.py
```

## Project Structure

```text
terminal-dungeon/
│
├── main.py
└── README.md
```

## Architecture

The project is currently organized around several functional components:

```text
UI Helpers
├── slow_print()
├── divider()
├── section()
├── hp_bar()
└── pause()

Progression
├── xp_needed_for_next_level()
└── level_up_check()

Enemies & Events
├── create_enemy()
├── apply_path_modifiers()
├── supply_search()
└── maybe_drop_loot()

Potions
└── use_potion()

Combat
└── combat()

Boss
└── boss_fight()

Game
├── show_player_hud()
├── start_game()
└── main_menu()
```

This structure was developed incrementally as the game evolved from a simple combat prototype into a larger playable system.

## What I Learned

This project was built to practice practical Python development, including:

* Functions and modular program structure
* Lists and dictionaries
* Loops and nested loops
* `break` and `continue`
* Conditional logic
* User input and validation
* Random number generation
* Mutable program state
* Designing game systems
* Separating UI, game logic, combat, and progression
* Debugging and iterative development
* Git and GitHub version control

## Project Status

**Playable prototype — actively developed**

The current version contains the core dungeon, exploration, combat, progression, potion, loot, and boss systems. The project may be expanded and refactored in future iterations.

## Planned Improvements

Potential future improvements include:

* Refactoring the game into an object-oriented architecture
* Expanding the inventory and item system
* Adding more enemy and boss mechanics
* Improving balancing and player agency
* Adding equipment and weapons
* Adding persistent save/load functionality
* Improving combat effects and terminal presentation
* Expanding dungeon events and exploration variety

## Author

**Shah Amanat Chowdhury**

Built as a personal Python project while learning software development.
