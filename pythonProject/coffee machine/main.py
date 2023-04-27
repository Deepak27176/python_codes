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
money_box = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_sufficent_ingrediants(ordered):
    for item in ordered:
        if ordered[item] < resources[item]:
            print("sorry shortage of ingredients")
            return False
    return True

def process_payment():
    total = 0
    total += int(input("enter no of 25 paise  coin:"))/4
    total += int(input("enter no of 50 paise  coin:"))/2
    total += int(input("enter no of 1 rupee "))
    if total == choice["cost"]:
        print(f"here is your{choice}")



is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):")
    if choice == "off":
        is_on = False
    if choice == "report":
        print(f"water:{resources['water']}ml")
        print(f"milk:{resources['milk']}ml")
        print(f"coffee:{resources['coffee']}g")
        print(f"Money:INR{money_box}")
    else:
        drink = MENU[choice]
        if check_sufficent_ingrediants(drink):
             process_payment()

