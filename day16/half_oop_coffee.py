from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True

while machine_on == True:
    options = menu.get_items()
    user_choose = input("Choose one: ")

    if user_choose == "off":
        machine_on = False
        print()
        print("Turning off the machine...")
    elif user_choose == "report":
        print()
        coffee_maker.report()
        money_machine.report()
    else:
        coffee_chosen = menu.find_drink(user_choose)

        if coffee_maker.is_resource_sufficient(coffee_chosen) and money_machine.make_payment(coffee_chosen.cost):
            coffee_maker.make_coffee(coffee_chosen)
