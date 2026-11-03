### String ###
import random

nimi = "Joonas"


print(len(nimi)) # length

isikukood = "393565657654"
print("sünniaasta:", "19" + isikukood[1:3])

### Lists ###

animals = ["bird", "lion", "tiger", "cat", "dog"]
print(list(animals))
print(len(animals))

numbers = [69, 6, 7, 1337, 666, 42]
user_data = ["Joonas", 33, 3124543533.43543, True, False, "thinkpad"]
print(list(numbers))

students = ["German", "Karmo", "Vitaly", "Konstantin", "Anton", "Tanel"]
weapons = ["stick", "spoon", "sword", "chicken", "plunger", "fork"]
monsters = ["dragon", "goblin", "troll", "kraken", "human", "orc"]

print(students[2], "killed", numbers[4], monsters[4] + "s with a", weapons[5])


### MODULES // LIBRARY

print(
    random.choice(students),
    "killed",
    random.choice(numbers),
    random.choice(monsters) + "s with a",
    random.choice(weapons)
)

print(random.random())
print(random.randint(10,100))
print(random.choices(students, k=2))


### Loops ###

# n = 0
# while True:
#     n = n + 1
#     print(n)

password_in_database = "kitten"
entered_password = input("Enter password: ")

while password_in_database != entered_password:
    print("Wrong password")
    entered_password = input("Enter password: ")

print("Password correct")