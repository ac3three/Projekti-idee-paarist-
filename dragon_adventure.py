import random


# Two simple functions

def show_status():
    print("\n--- HERO STATUS ---")
    print("Name:", name)
    print("Class:", hero)
    print("Health:", health)
    print("Gold:", gold)
    print("Potions:", potions)
    print("Attack power:", power)
    print("Monsters defeated:", wins)


def attack():
    damage = random.randint(5, 10) + power
    return damage


# Create a hero

print("========================")
print("    DRAGON ADVENTURE")
print("========================")
print("Defeat two goblins, then fight the dragon!")
name = input("Hero name: ")
print("1. Warrior")
print("2. Mage")
hero_choice = input("Choose your class: ")

if hero_choice == "2":
    hero = "Mage"
    power = 5
else:
    hero = "Warrior"
    power = 3

health = 100
gold = 20
potions = 1
wins = 0
dragon_defeated = False
print("Welcome,", name, "the", hero, "!")


# Main game menu

while health > 0 and not dragon_defeated:
    print("\n======= VILLAGE =======")
    print("1. Hero status")
    print("2. Fight a goblin")
    print("3. Shop")
    print("4. Rest at the inn")
    print("5. Fight the dragon")
    print("6. Exit")
    choice = input("Choose 1-6: ")

    if choice == "1":
        show_status()

    elif choice == "2" or choice == "5":
        if choice == "5" and wins < 2:
            print("Defeat two goblins before fighting the dragon!")
        else:
            if choice == "2":
                enemy = "Goblin"
                enemy_health = 30
                enemy_power = 7
            else:
                enemy = "Dragon"
                enemy_health = 65
                enemy_power = 14

            print("\nA", enemy, "appears!")
            while health > 0 and enemy_health > 0:
                print("\nYour health:", health)
                print(enemy, "health:", enemy_health)
                print("1. Attack")
                print("2. Drink a potion")
                action = input("Choose 1-2: ")

                if action == "1":
                    damage = attack()
                    enemy_health = enemy_health - damage
                    print("You dealt", damage, "damage!")
                elif action == "2":
                    if potions > 0:
                        potions = potions - 1
                        health = health + 30
                        if health > 100:
                            health = 100
                        print("You used a potion!")
                    else:
                        print("You have no potions!")
                        continue
                else:
                    print("Choose 1 or 2.")
                    continue

                if enemy_health > 0:
                    enemy_damage = random.randint(2, enemy_power)
                    health = health - enemy_damage
                    print("The", enemy, "dealt", enemy_damage, "damage!")

            if health > 0:
                if enemy == "Dragon":
                    dragon_defeated = True
                    print("You defeated the dragon and saved the village!")
                else:
                    wins = wins + 1
                    gold = gold + 10
                    print("You won! You received 10 gold.")
            else:
                print("You lost the battle!")

    elif choice == "3":
        print("\n====== SHOP ======")
        print("1. Potion - 10 gold")
        print("2. Better sword - 20 gold")
        print("3. Back")
        item = input("Choose 1-3: ")
        if item == "1":
            if gold >= 10:
                gold = gold - 10
                potions = potions + 1
                print("You bought a potion!")
            else:
                print("Not enough gold!")
        elif item == "2":
            if gold >= 20:
                gold = gold - 20
                power = power + 3
                print("Your attacks are stronger!")
            else:
                print("Not enough gold!")
        elif item == "3":
            print("You left the shop.")
        else:
            print("Invalid shop choice.")

    elif choice == "4":
        if gold >= 5:
            gold = gold - 5
            health = 100
            print("You rested. Health is now 100.")
        else:
            print("You need 5 gold to rest.")

    elif choice == "6":
        print("Goodbye! Thanks for playing.")
        break

    else:
        print("Choose a number from 1 to 6.")

if health <= 0:
    print("GAME OVER!")
if dragon_defeated:
    print("YOU WIN! Congratulations,", name, "!")
