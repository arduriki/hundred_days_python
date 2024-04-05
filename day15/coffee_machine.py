MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 1 Prompt user
def prompt_user():
    """Ask the user an action."""
    user_answer = input("What would you like? (espresso/latte/capuccino)\n")
    return user_answer


# TODO: 2 Process the user's answer
def coffee_machine(machine_resources, coffee_requirements):
    """Process the prompt from the user."""
    machine_on = True
    while machine_on == True:
        user_answer = prompt_user()
        if user_answer == "espresso":
            coffe_available = check_resources(user_answer, machine_resources, coffee_requirements)
            coins_available = process_coins(coffe_available, user_answer, coffee_requirements, machine_resources)
        elif user_answer == "latte":
            coffe_available = check_resources(user_answer, machine_resources, coffee_requirements)
            coins_available = process_coins(coffe_available, user_answer, coffee_requirements, machine_resources)
        elif user_answer == "capuccino":
            coffe_available = check_resources(user_answer, machine_resources, coffee_requirements)
            coins_available = process_coins(coffe_available, user_answer, coffee_requirements, machine_resources)
        # TODO: 3 Turn off the Coffee Machine
        elif user_answer == "off":
            print("Machine turning off...")
            machine_on = False
        elif user_answer == "report":
            resources_report(machine_resources)
        else:
            print("Enter a correct command, please.")

        print()


# TODO: 4 Resources report
def resources_report(resources_dict):
    """Prints a report about the machine's resources."""
    print()
    for key, value in resources_dict.items():
        if key == "coffee":
            print(f"{key}: {value}mg")
        elif key == "money":
            print(f"{key}: ${value}")
        else:
            print(f"{key}: {value}ml")


# TODO: 5 Enough resources?
def check_resources(user_answer, machine_resources, coffee_requirements):
    """Machine checks whether there's enough resources once the user has prompted a coffee"""
    required_ingredients = coffee_requirements[user_answer]["ingredients"]

    for ingredient, required_quantity in required_ingredients.items():
        if machine_resources.get(ingredient, 0) < required_quantity:
            print(f"Sorry, there is not enough {ingredient}.")
            return False

    return True


# TODO: 6 Process coins
def process_coins(coffee_available, user_answer, coffee_requirements, machine_resources):
    """User inserts coins to pay."""
    money = 0
    if coffee_available == True:
        penny = int(input("How many pennies?: "))
        if penny > 0:
            money += penny * 0.01
        nickel = int(input("How many nickles?: "))
        if nickel > 0:
            money += nickel * 0.05
        dime = int(input("How many dimes?: "))
        if dime > 0:
            money += dime * 0.1
        quarter = int(input("How many quarters?: "))
        if quarter > 0:
            money += quarter * 0.25

    # Check if there's enough money
    check_money(money, user_answer, coffee_requirements, machine_resources)


# TODO: 7 Check if there's enough money:
def check_money(money, user_answer, coffee_requirements, machine_resources):
    machine_resources["money"] = 0
    required_money = coffee_requirements[user_answer]["cost"]
    if money == required_money:
        machine_resources["money"] += required_money
        print()
        print("No change needed.")
        print(f"Making your {user_answer}...")
        print(f"Here is your {user_answer}. Enjoy!")
    elif money > required_money:
        machine_resources["money"] += required_money
        money_change = money - required_money
        print()
        print(f"Here is your change: ${money_change}")
        print(f"Making your {user_answer}")
        print(f"Here is your {user_answer}. Enjoy!")
    else:
        print("Sorry, that's not enough money. Money refunded.")


coffee_machine(resources, MENU)
