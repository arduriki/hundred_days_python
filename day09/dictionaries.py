# Create a dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

# Call a key of the dictionary
print(programming_dictionary["Bug"])

"""
Number for indexing, doesn't exist.
Every Key has to have quotation marks, likewise then you call it.
Unless that the key is an int...
"""

# Adding new items to dictionary.
programming_dictionary["Loop"] = "The action of doing something over and over again."

print(programming_dictionary)

# Empty dictionary
empty_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer."
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
    # Print the key
    print(key)
    # Print the value
    print(programming_dictionary[key])


# Wipe an existing dictionary
programming_dictionary = {}
print(programming_dictionary)

# ------------------------

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in a dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nest dictionary in a dictionary -> access by the keys
travel_log = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "UK": {
        "cities_visited": ["London", "King's Lynn", "Norwich"],
        "total_visits": 3,
    },
}

# Nest a disctionary in a list -> access by position
travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "UK",
        "cities_visited": ["London", "King's Lynn", "Norwich"],
        "total_visits": 3
    }
]
