# enemies = 1

# def increase_enemies():
#     print(f"enemies inside function: {enemies}")
#     return enemies + 1


# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

# # Local Scope - within the function
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)  # 2


# drink_potion()
# print(potion_strength)  # Error - NameError, not defined

# # Global Scope - outside the function
# player_health = 10

# def game():
#     # local function
#     def drink_potion():
#         # local variable
#         potion_strength = 2
#         print(player_health)
#     # has to be called inside the function
#     drink_potion()

# print(player_health)

# There is no Block Scope

# game_level = 3
# def create_enemy():
#     enemies = ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)

PI = 3.14159
URL = "https://www.google.com"