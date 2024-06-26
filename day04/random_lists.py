# import a general module
import random
# import a module created by myself
import my_module

# using general module
random_integer = random.randint(1, 10)
print(random_integer)

# using my module
print(my_module.pi)

# random = 0 to 1
random_float = random.random()
print(random_float)
# to extend further from 1: * number
random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

# -------------------

states_of_america = ["Delaware", "Pennsylvania"]
# lists have order starting from 0
print(states_of_america[0])  # Delaware
print(states_of_america[-1])  # Pennsylvania = last item of the list
# there can be negative index

# change an item of the list
states_of_america[1] = "Pencilvania"
# add an item at the end of the list
states_of_america.append("Angelaland")
# extending with another list
other_states = ["Ardurikiland", "Jack Bauer Land"]
states_of_america.extend(other_states)
# to avoid IndexError
num_of_states = len(states_of_america)
print(states_of_america[num_of_states - 1])

print(states_of_america)  # Delaware, Pencilvania, Angelaland, Ardurikiland, Jack Bauer Land

# ---------------------

# Nesting two lists
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]

print(dirty_dozen)  # Two lists inside another list
print(dirty_dozen[1][1])  # Takes the second list, and the second item from there.
