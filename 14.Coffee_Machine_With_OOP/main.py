from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
menu_item = MenuItem
money_machine = MoneyMachine()



should_continue = True

while should_continue:

    choice = input(f"What would you like? {menu.get_items()}")

    if choice == "off":

        should_continue = False

    elif choice == "report":

        coffee_maker.report()
        money_machine.report()


    else:

        drink  = menu.find_drink(order_name=choice)

        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)






