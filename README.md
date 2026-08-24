# Terminal Dungeon 🎮

A small turn-based dungeon RPG built entirely with Python and played through the terminal.

This is a personal project created to practice Python programming by building a playable game from scratch. The project focuses on game loops, state management, randomization, dictionaries, functions, and control flow.

## 🎮 Current Features

* 🏰 Interactive terminal-based dungeon
* ❤️ Randomized player health
* 👹 Multiple enemy types:

  * Goblin
  * Skeleton
  * Orc
* 🎲 Randomized enemy health and damage
* ⚔️ Turn-based combat
* 🏃 Run away from encounters
* ⭐ XP rewards for defeating enemies
* 💰 Gold rewards for defeating enemies
* 🗺️ Continue exploring after defeating an enemy
* 🔄 Play again without restarting the program
* 🚪 Return to the main menu at any time

## 🕹️ How the Game Works

The player enters the dungeon and encounters a randomly selected enemy.

During combat, the player can:

```text
1. Attack
2. Run
```

When attacking:

1. The player deals random damage.
2. If the enemy survives, it attacks back.
3. The battle continues until either the player or enemy is defeated.

Defeating an enemy rewards the player with XP and gold.

The player can then choose to continue exploring and encounter another random enemy, allowing XP and gold to accumulate during the same dungeon run.

## 🧟 Enemies

Each enemy has its own statistics and rewards.

| Enemy    |    HP | Damage | XP | Gold |
| -------- | ----: | -----: | -: | ---: |
| Goblin   | 20–50 |   3–10 | 10 |   10 |
| Skeleton | 30–65 |   5–12 | 20 |   20 |
| Orc      | 50–90 |   8–16 | 30 |   30 |

Enemy statistics are randomized when an encounter begins.

## 🛠️ Technologies Used

* **Python 3**
* Python standard library
* `random` module

No external packages are currently required.

## 📁 Project Structure

```text
terminal-dungeon/
│
├── main.py
└── README.md
```

## ▶️ How to Run

Make sure Python 3 is installed.

Clone the repository:

```bash
git clone https://github.com/shah2766/terminal-dungeon.git
```

Enter the project directory:

```bash
cd terminal-dungeon
```

Run the game:

```bash
python3 main.py
```

## 🎯 Current Gameplay Flow

```text
Main Menu
    │
    ├── Start Game
    │       │
    │       ├── Random Enemy
    │       │
    │       ├── Battle
    │       │
    │       ├── Receive XP + Gold
    │       │
    │       └── Continue Exploring
    │               │
    │               └── Random Enemy
    │
    └── Exit
```

## 🧠 What I Am Learning

This project is helping me practice:

* Python functions
* `while` loops
* Conditional logic
* User input
* Lists and dictionaries
* Random number generation
* Mutable program state
* Nested loops
* `break` and `continue`
* Designing reusable game logic
* Debugging and incremental development

## 🚧 Planned Improvements

The game is still under development. Planned features include:

* Player leveling system
* Inventory and consumable items
* Health potions
* Weapons and equipment
* Shop and gold spending
* More enemy types
* Dungeon events and exploration choices
* Final boss
* Save/load functionality
* Improved input validation
* Cleaner project architecture
* Better terminal presentation

## 📌 Project Status

**Current status: Playable prototype**

The core gameplay loop and combat system are currently working. New features will be added incrementally as the project develops.

## 👨‍💻 Author

**Shah Amanat Chowdhury**

Built as a personal project while learning Python and software development.
