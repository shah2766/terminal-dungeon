import random
import time


# =========================
# UI HELPERS
# =========================

def slow_print(text, delay=0.02):
    """Print text with a typewriter effect for drama."""
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()


def divider(char="=", width=40):
    print(char * width)


def section(title):
    divider("=")
    print(f" {title}")
    divider("=")


def hp_bar(current, maximum, length=20):
    """Return a visual HP bar like [██████------]"""
    if maximum <= 0:
        maximum = 1
    filled = int((current / maximum) * length)
    filled = max(0, min(length, filled))
    empty = length - filled
    return f"[{'█' * filled}{'-' * empty}] {current}/{maximum}"


def pause(seconds=0.6):
    time.sleep(seconds)


# =========================
# CORE PROGRESSION
# =========================

def xp_needed_for_next_level(level):
    return level * 50


def level_up_check(player):
    while player["xp"] >= xp_needed_for_next_level(player["level"]):
        player["level"] += 1
        player["max_hp"] += 10
        player["hp"] = player["max_hp"]

        if player["level"] % 2 == 0:
            player["health_potions"] += 1

        section("✨ LEVEL UP! ✨")
        slow_print(f"You feel a surge of strength...")
        slow_print(f"⚔️ You have reached Level {player['level']}!")
        slow_print(f"❤️ Max HP increased to {player['max_hp']}.")
        slow_print("💚 Your wounds vanish as your HP is fully restored!")

        if player["level"] == 10:
            slow_print("🌟 Something powerful awakens within you...")
            slow_print("🧪 Super Potion unlocked!")


# =========================
# ENEMIES & EVENTS
# =========================

def create_enemy(depth):
    goblin = {
        "name": "Goblin",
        "hp": random.randint(20, 50),
        "damage": random.randint(3, 10),
        "xp": 10,
        "gold": 10,
    }

    skeleton = {
        "name": "Skeleton",
        "hp": random.randint(30, 65),
        "damage": random.randint(5, 12),
        "xp": 20,
        "gold": 20,
    }

    orc = {
        "name": "Orc",
        "hp": random.randint(50, 90),
        "damage": random.randint(8, 16),
        "xp": 30,
        "gold": 30,
    }

    elite_orc = {
        "name": "Elite Orc",
        "hp": random.randint(80, 120),
        "damage": random.randint(12, 20),
        "xp": 45,
        "gold": 45,
    }

    if depth <= 3:
        pool = [goblin, goblin, skeleton, skeleton, orc]
    elif depth <= 6:
        pool = [goblin, skeleton, skeleton, orc, orc]
    else:
        pool = [skeleton, orc, orc, elite_orc, elite_orc]

    return random.choice(pool)


def apply_path_modifiers(enemy, path_choice):
    if path_choice == 1:  # Safe
        enemy["hp"] = max(10, int(enemy["hp"] * 0.85))
        enemy["damage"] = max(1, int(enemy["damage"] * 0.85))
        enemy["xp"] = max(5, int(enemy["xp"] * 0.90))
        enemy["gold"] = max(5, int(enemy["gold"] * 0.90))
    elif path_choice == 2:  # Dangerous
        enemy["hp"] = int(enemy["hp"] * 1.20)
        enemy["damage"] = int(enemy["damage"] * 1.20)
        enemy["xp"] = int(enemy["xp"] * 1.25)
        enemy["gold"] = int(enemy["gold"] * 1.25)


def supply_search(player):
    section("🔎 SEARCHING THE RUINS")

    room_lines = [
        "You kick aside a pile of dusty bones...",
        "You inspect a cracked stone chest...",
        "You pull aside a rotted tapestry...",
        "You search beneath a pile of ancient rubble...",
        "You rummage through the remains of an old adventurer...",
    ]

    slow_print(random.choice(room_lines))
    pause(0.8)

    roll = random.randint(1, 100)

    if roll <= 35:
        player["health_potions"] += 1
        slow_print("🧪 You discover a Health Potion hidden among the debris!")

    elif roll <= 60:
        found_gold = random.randint(10, 30)
        player["gold"] += found_gold
        slow_print(f"💰 A forgotten coin pouch! You found {found_gold} gold.")

    elif roll <= 70 and player["level"] >= 10:
        player["super_potions"] += 1
        slow_print("🌟 JACKPOT!")
        slow_print("You uncover a glowing Super Potion!")

    else:
        slow_print("You find nothing but dust, bones, and disappointment.")


def maybe_drop_loot(player):
    roll = random.randint(1, 100)

    if roll <= 25:
        player["health_potions"] += 1
        slow_print("🧪 Loot Drop: Health Potion!")

    elif roll <= 33 and player["level"] >= 10:
        player["super_potions"] += 1
        slow_print("🌟 Loot Drop: Super Potion!")


# =========================
# POTIONS
# =========================

def use_potion(player):
    section("🧴 POTION BAG")

    print(f"1) Health Potion (+30 HP)       [{player['health_potions']}]")
    print(f"2) Super Potion (+50% Max HP)  [{player['super_potions']}]")
    print("3) Cancel\n")

    try:
        choice = int(input("Choose: "))
    except ValueError:
        slow_print("Invalid choice.")
        return False

    if choice == 1:
        if player["health_potions"] > 0:
            player["health_potions"] -= 1
            player["hp"] = min(
                player["max_hp"],
                player["hp"] + 30
            )

            slow_print("🧪 You swallow a Health Potion.")
            slow_print("Warmth spreads through your body...")
            slow_print(f"❤️ HP: {player['hp']}/{player['max_hp']}")
            return True

        slow_print("You reach for a Health Potion...")
        slow_print("...but your bag is empty.")
        return False

    if choice == 2:
        if player["super_potions"] > 0:
            player["super_potions"] -= 1
            heal = player["max_hp"] // 2
            player["hp"] = min(
                player["max_hp"],
                player["hp"] + heal
            )

            slow_print("🌟 You drink the Super Potion.")
            slow_print("A surge of energy tears through your veins!")
            slow_print(f"❤️ HP: {player['hp']}/{player['max_hp']}")
            return True

        slow_print("You search your bag for a Super Potion...")
        slow_print("Nothing. You're not carrying one.")
        return False

    if choice == 3:
        return False

    slow_print("Invalid choice.")
    return False


# =========================
# COMBAT
# =========================

def combat(player, enemy):
    hit_lines = [
        "⚡ Your blade flashes through the darkness!",
        "⚔️ Your attack lands hard!",
        "🎯 Right on target!",
        "💥 Your strike echoes through the chamber!",
    ]

    enemy_hit_lines = [
        "💥 The enemy lunges at you!",
        "💥 A brutal blow catches you off guard!",
        "💥 You stagger from the impact!",
        "💥 The attack sends pain through your body!",
    ]

    while player["hp"] > 0 and enemy["hp"] > 0:
        section(f"⚔️ BATTLE — {enemy['name'].upper()}")

        print(f"YOU   {hp_bar(player['hp'], player['max_hp'])}")
        print(f"ENEMY {hp_bar(enemy['hp'], enemy['hp_max'])}\n")

        print("1) ⚡ Quick Attack   (Reliable)")
        print("2) 🪓 Heavy Attack   (High Risk / High Reward)")
        print("3) 🧪 Use Potion")
        print("4) 🏃 Run\n")

        try:
            p_choice = int(input("Choose: "))
        except ValueError:
            slow_print("Numbers only.")
            continue

        if p_choice == 1:
            dmg = random.randint(6, 12)
            enemy["hp"] -= dmg

            slow_print(f"\n⚡ Quick Attack deals {dmg} damage!")
            slow_print(random.choice(hit_lines), 0.01)

        elif p_choice == 2:
            if random.randint(1, 100) <= 25:
                slow_print("\n💨 Heavy Attack MISSED!")
            else:
                dmg = random.randint(12, 20)
                enemy["hp"] -= dmg
                slow_print(
                    f"\n🪓 Heavy Attack crushes for {dmg} damage!"
                )

        elif p_choice == 3:
            used = use_potion(player)

            if not used:
                continue

        elif p_choice == 4:
            slow_print(
                f"\n🏃 You decide that fighting the {enemy['name']} "
                "is tomorrow's problem."
            )
            slow_print("You retreat into the darkness!")
            return "run"

        else:
            slow_print("Invalid choice.")
            continue

        if enemy["hp"] <= 0:
            enemy["hp"] = 0

            section("✅ ENEMY DEFEATED")
            slow_print(
                f"The {enemy['name']} crashes to the ground!"
            )

            return "win"

        # Enemy turn
        pause(0.5)

        e_dmg = enemy["damage"]
        player["hp"] -= e_dmg

        slow_print(
            f"\n💥 {enemy['name']} hits you for {e_dmg} damage!"
        )
        slow_print(random.choice(enemy_hit_lines), 0.01)

        if player["hp"] <= 0:
            player["hp"] = 0

            section("💀 YOUR JOURNEY ENDS HERE")
            slow_print(
                f"The {enemy['name']} stands victorious..."
            )

            return "lose"

    return "lose"


# =========================
# BOSS
# =========================

def boss_fight(player):
    boss = {
        "name": "Dread Lord",
        "hp": 220,
        "hp_max": 220,
        "damage": 18,
        "xp": 120,
        "gold": 150,
    }

    section("👑 THE ABYSSAL CHAMBER")

    slow_print("The temperature drops.")
    pause(0.7)

    slow_print("The torches die one by one.")
    pause(0.7)

    slow_print("Something enormous moves in the darkness...")
    pause(1)

    slow_print('A voice echoes through the chamber.')
    slow_print('"You should never have come this far."')
    pause(0.7)

    slow_print(f"\n⚔️ THE {boss['name'].upper()} APPEARS!")
    pause(0.7)

    result = combat(player, boss)

    if result == "win":
        player["xp"] += boss["xp"]
        player["gold"] += boss["gold"]

        level_up_check(player)

        section("🏆 DUNGEON CONQUERED")

        slow_print("The Dread Lord falls.")
        slow_print("For the first time, the dungeon is silent.")
        slow_print("You made it out alive.")

        print(f"Level: {player['level']}")
        print(f"XP: {player['xp']}")
        print(f"Gold: {player['gold']}")

        return True

    section("☠️ THE DUNGEON CLAIMS ANOTHER SOUL")
    slow_print("The Dread Lord stands victorious...")
    slow_print("Your journey ends in darkness.")

    return False


# =========================
# GAME LOOP
# =========================

def show_player_hud(player, depth):
    section(f"⚔️ THE DUNGEON — CHAMBER {depth}")

    print(f"❤️ HP:    {hp_bar(player['hp'], player['max_hp'])}")
    print(f"⭐ Level: {player['level']}")
    print(
        f"✨ XP:    "
        f"{player['xp']}/{xp_needed_for_next_level(player['level'])}"
    )
    print(f"💰 Gold:  {player['gold']}")
    print(f"🧪 Health Potions: {player['health_potions']}")
    print(f"🌟 Super Potions:  {player['super_potions']}")


def start_game():
    player = {
        "hp": 100,
        "max_hp": 100,
        "level": 1,
        "xp": 0,
        "gold": 0,
        "health_potions": random.randint(0, 1),
        "super_potions": 0
    }

    depth = 1
    final_depth = 8

    section("🕳️ ENTER THE DUNGEON")

    slow_print("The dungeon waits in silence.")
    slow_print("Torches flicker along the ancient walls.")
    slow_print("You take a deep breath and step inside.\n")

    while True:
        if player["hp"] <= 0:
            break

        if depth > final_depth:
            boss_fight(player)
            break

        show_player_hud(player, depth)

        print("\nThe passage splits ahead.")
        print("Your instincts tell you neither path is safe.\n")

        print("1) 🛡️ Quiet Passage")
        print("   Lower danger • Lower rewards\n")

        print("2) 🔥 Blood Trail")
        print("   Higher danger • Better rewards\n")

        print("3) 🔎 Search the Ruins")
        print("   You might find something useful...\n")

        print("4) 🚪 Leave the Dungeon\n")

        try:
            action = int(input("Choose: "))
        except ValueError:
            slow_print("Invalid input.")
            continue

        if action == 4:
            slow_print(
                "\nYou step back from the darkness."
            )
            slow_print(
                "The dungeon will still be here..."
            )
            break

        if action == 3:
            supply_search(player)
            depth += 1
            continue

        if action not in [1, 2]:
            slow_print("Invalid choice.")
            continue

        enemy = create_enemy(depth)
        apply_path_modifiers(enemy, action)
        enemy["hp_max"] = enemy["hp"]

        section("👀 ENCOUNTER")

        if enemy["name"] == "Goblin":
            slow_print(
                "A Goblin crawls from the shadows, "
                "grinning far too confidently."
            )
        elif enemy["name"] == "Skeleton":
            slow_print(
                "A rattling Skeleton rises from a pile "
                "of ancient bones."
            )
        elif enemy["name"] == "Orc":
            slow_print(
                "Heavy footsteps shake the corridor.\n"
                "An Orc emerges from the darkness."
            )
        else:
            slow_print(
                "The ground trembles beneath your feet.\n"
                "An Elite Orc steps into your path."
            )

        print()
        print(f"Enemy HP: {enemy['hp']}")
        print(f"Enemy Damage: {enemy['damage']}")
        print(
            f"Reward: +{enemy['xp']} XP, "
            f"+{enemy['gold']} Gold"
        )

        pause(0.8)

        result = combat(player, enemy)

        if result == "win":
            player["xp"] += enemy["xp"]
            player["gold"] += enemy["gold"]

            slow_print(f"\n✨ +{enemy['xp']} XP")
            slow_print(f"💰 +{enemy['gold']} Gold")

            maybe_drop_loot(player)
            level_up_check(player)

            depth += 1

        elif result == "run":
            slow_print(
                "\nYou live to fight another day."
            )
            depth += 1

        elif result == "lose":
            break

    # =========================
    # RUN SUMMARY
    # =========================

    section("📜 ADVENTURE SUMMARY")

    if player["hp"] > 0:
        slow_print(
            "You step back into the light, "
            "carrying what you managed to survive with."
        )
        slow_print(
            "The dungeon will still be waiting..."
        )
    else:
        slow_print("Your journey has come to an end.")
        slow_print(
            "The dungeon claims another soul."
        )

    print()
    print(f"Level: {player['level']}")
    print(f"HP: {player['hp']}/{player['max_hp']}")
    print(f"XP: {player['xp']}")
    print(f"Gold: {player['gold']}")
    print(f"🧪 Health Potions: {player['health_potions']}")
    print(f"🌟 Super Potions: {player['super_potions']}")


# =========================
# MAIN MENU
# =========================

def main_menu():
    while True:
        section(r"""
████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗
╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║
   ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║
   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║
   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗
   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝

██████╗ ██╗   ██╗███╗   ██╗ ██████╗ ███████╗ ██████╗ ███╗   ██╗
██╔══██╗██║   ██║████╗  ██║██╔════╝ ██╔════╝██╔═══██╗████╗  ██║
██║  ██║██║   ██║██╔██╗ ██║██║  ███╗█████╗  ██║   ██║██╔██╗ ██║
██║  ██║██║   ██║██║╚██╗██║██║   ██║██╔══╝  ██║   ██║██║╚██╗██║
██████╔╝╚██████╔╝██║ ╚████║╚██████╔╝███████╗╚██████╔╝██║ ╚████║
╚═════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝
""")

        print("1) Start Game")
        print("2) Exit\n")

        try:
            choice = int(input("Choose: "))
        except ValueError:
            slow_print("Invalid input.")
            continue

        if choice == 1:
            start_game()

            print("\n1) Play Again")
            print("2) Return to Main Menu\n")

            try:
                post = int(input("Choose: "))
            except ValueError:
                post = 2

            if post == 1:
                start_game()

        elif choice == 2:
            slow_print("\nGoodbye, adventurer. 👋")
            break

        else:
            slow_print("Choose 1 or 2.")


main_menu()