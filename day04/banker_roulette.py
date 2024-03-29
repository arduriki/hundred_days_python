import random

names_string = input(
    "Write the names of the people that are going to participate:\n")
# Angela, Ben, Jenny, Michael, Chloe

names = names_string.split(", ")
random_number = random.randint(0, len(names) - 1)
who_pays = names[random_number]

print(f"{who_pays} is going to buy the meal today!")

"""-----------
OTHER SOLUTION
-----------"""

# Get the total number of items in list.
num_items = len(names)
# Generate random numbers between 0 and the last index.
random_choice = random.randint(0, num_items - 1)
# Pick out random person from list of names using the random number.
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to buy the meal today!")