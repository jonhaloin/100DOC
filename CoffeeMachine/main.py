from art import logo
from data import resources, money, drinks


def coffee_machine():
    """User inputs either a drink which is then made, query for a report which is printed, or the off command"""

    drink  = ""

    while drink != "off":
        if drink == "report":
            create_report()
            drink = ""

        elif drink in drinks.keys():
            if not enough_for(drink):
                drink = input(" What would you like? (espresso/latte/cappuccino): ")

            else:
                cash = process_coins()
                drink_cost = drinks[drink]["cost"]

                if cash >= drink_cost:
                    make_change(cash, drink_cost)
                    make_coffee(drink)
                    drink = ""

                else:
                    print(" Sorry that's not enough money. Money refunded.")
                    drink = input("What would you like? (espresso/latte/cappuccino): ")

        else:
            drink = input(" What would you like? (espresso/latte/cappuccino): ")

def enough_for(drink):
    """Enter drink to check if there are enough resources to make it. """
    for ingredient in resources.keys():
        if drinks[drink][ingredient] >= resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    """Gets user input for coins and returns the total value fo the coins"""
    print("Please insert coins")
    quarters = int(input("how many quarters? ")) * .25
    dimes = int(input("how many dimes? ")) * 0.10
    nickles = int(input("how many nickles? ")) * 0.05
    pennies = int(input("how many pennies? ")) * 0.01
    return quarters + dimes + nickles + pennies


def make_change(cash_provided, drink_cost):
    """Calculates change for cash provided and drink cost and adds the profit to value of money"""
    global money
    change = round(cash_provided - drink_cost, 2)
    money += drink_cost
    print(f"Here is ${change:.2f} dollars in change")
    return

def make_coffee(drink):
    for ingredient in resources.keys():
        resources[ingredient] -= drinks[drink][ingredient]
    print(f"Here is your {drink}. Enjoy!")
    return

def create_report():
    """Print a report showing the current resources and money"""
    for item in resources.keys():
        print(f"{item}: {resources[item]} ml")
    print(f"Money: $%.2f" % money)
    return

print(logo)
coffee_machine()