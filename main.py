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


def quantity(ingredients):
    """ return the quantity of the ingredients stage 0"""
    return resources[ingredients]


def report():
    """report the amount of ingredients left and money gained"""
    print(f" Water: {water_qu} ml\n Milk: {milk_qu} ml\n Coffee: {coffee_qu} g\n Money: {profit} ¥")


water_qu = quantity("water")
milk_qu = quantity("milk")
coffee_qu = quantity("coffee")
list_ingredients = [water_qu, coffee_qu, milk_qu]

profit = 0
is_over = False


def check_quantity(coffee):
    if water_qu < MENU[coffee]["ingredients"]["water"]:
        print("Sorry, there is not enough water")
        return True
    if coffee_qu < MENU[coffee]["ingredients"]["coffee"]:
        print("Sorry, there is not enough coffee")
        return True
    if "milk" in MENU[coffee]["ingredients"]:
        if milk_qu < MENU[coffee]["ingredients"]["milk"]:
            print("Sorry, there is not enough milk")
            return True


def deduct_amount(coffee):
    global water_qu
    global milk_qu
    global coffee_qu
    if "milk" in MENU[coffee]["ingredients"]:
        milk_qu -= MENU[coffee]["ingredients"]["milk"]
    water_qu -= MENU[coffee]["ingredients"]["water"]
    coffee_qu -= MENU[coffee]["ingredients"]["coffee"]


def payment():
    print("Please insert coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    money_inserted = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return money_inserted


def check_price(coffee):
    if money_inserted < MENU[coffee]["cost"]:
        return True


def money_back(coffee):
    change = money_inserted - MENU[coffee]["cost"]
    return change


while not is_over:
    choice = input("What would you like? espresso / latte / cappuccino").lower()
    if choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if not check_quantity(choice):
            money_inserted = payment()
            if check_price(choice):
                print("Not enough money")
            else:
                print(f"Here is your change: {money_back(choice)} ¥")
                print(f"Here is your {choice}. Enjoy!")
                deduct_amount(choice)
                profit += MENU[choice]["cost"]
    elif choice == "report":
        report()
    elif choice == "off":
        print("Goodbye")
        is_over = True
    else:
        print("Wrong input")




