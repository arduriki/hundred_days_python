# Simple Function
def greet():
    print("Hello")
    print("How are you?")
    print("I hope you're doing fine!")

greet()

# Function that allows for input
def greet_with_name(name):
    print("Hello " + name)
    print(f"How are you, {name}?")

greet_with_name("Jordi")

# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"What is it like in {location}?")

greet_with("Jordi", "Vic")

# Keyword arguments
greet_with(location="Barcelona", name="Piyuli")
