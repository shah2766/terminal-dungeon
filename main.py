import random


def start_game():   # Main Game Loop

    # Create Player
    p_hp = random.randint(10, 100)
    p_xp = 0
    p_gold = 0

    while True:     # Exploration Loop

        print("\nYou enter a dark chamber...\n")

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
            "gold": 20
        }

        orc = {
            "name": "Orc",
            "hp": random.randint(50, 90),
            "damage": random.randint(8, 16),
            "xp": 30,
            "gold": 30
        }

        enemies = [goblin, skeleton, orc]
        enemy = random.choice(enemies)

        while p_hp > 0 and enemy["hp"] > 0:   # Battle Loop

            print(f"Your HP: {p_hp}\n"
                  f"{enemy['name']} HP: {enemy['hp']}\n\n"
                  "1. Attack\n"
                  "2. Run\n\n")

            p_choice = int(input("Choose: "))

            if p_choice == 1:

                p_d = random.randint(5, 15)
                enemy["hp"] -= p_d

                print(f"\nYou hit the {enemy['name']} for {p_d} damage!!!")
                print(f"{enemy['name']} HP: {enemy['hp']}\n")

                if enemy["hp"] <= 0:

                    print(f"You defeated the {enemy['name']}!!!\n")

                    p_xp += enemy["xp"]
                    p_gold += enemy["gold"]

                    print(f"Your XP: {p_xp}")
                    print(f"Your Gold: {p_gold}")

                    break

                p_hp -= enemy["damage"]

                print(f"{enemy['name']} hits you for {enemy['damage']} damage!!!")
                print(f"Your HP: {p_hp}\n")

                if p_hp <= 0:
                    print("You were defeated!!!\n")
                    break

            elif p_choice == 2:

                print("\nYou freaking coward!!!")
                print(f"You ran away from the {enemy['name']}!!!\n")
                break

            else:
                print("\nInvalid choice. Choose 1 or 2.\n")

        # Battle is over here
        # Now decide whether the player continues exploring

        if p_hp <= 0:
            break

        print("\nContinue exploring?\n"
              "1. Continue exploring\n"
              "2. Leave dungeon\n")

        b_choice = int(input("Choice: "))

        if b_choice == 1:
            continue

        elif b_choice == 2:
            break

    # Exploration/Game Run is over here
    # This is where Game Over belongs

    print("\n===== GAME OVER =====\n")
    print(f"Final HP: {p_hp}")
    print(f"Final XP: {p_xp}")
    print(f"Final Gold: {p_gold}\n")

    print("1. Play again")
    print("2. Return to main menu")

    p_opt = int(input("Choice: "))

    if p_opt == 1:
        start_game()


while True:     # Main Menu

    print("\n==== TERMINAL DUNGEON ====\n")
    print("What do you do?\n"
          "1. Start Game\n"
          "2. Exit\n")

    choice = int(input("Choose: "))

    if choice == 1:
        start_game()

    elif choice == 2:
        break