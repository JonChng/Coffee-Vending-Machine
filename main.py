
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

def check_resources(drink):
    global MENU
    global resources

    ingredients = MENU[drink]['ingredients']

    li = ["water", 'milk', 'coffee']

    for i in li:
        if ingredients[i] > resources[i]:
            print(f"Sorry there is not enough {ingredients[i]}.")
            return False
        else:
            resources[i] -= ingredients[i]
    return True

def print_report(resource):

    print(f"Water: {resource['water']}ml")
    print(f"Milk: {resource['milk']}ml")
    print(f"Coffee: {resource['coffee']}g")


def process_coins(drink, quarter, dime, nickel, penny):

    global MENU

    cost = MENU[drink]['cost'] * 100
    val = 0

    coin_value = {
        'quarter': 25,
        'dime': 10,
        'nickel': 5,
        'penny': 1,
    }

    val = val + quarter * coin_value['quarter'] + dime * coin_value['dime'] + coin_value['nickel'] + coin_value['penny']


    if val >= cost:
        change = (val - cost)/100
        print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry that is not enough money. Your money has been refunded.")
        return False

ok = True

while ok:
    drink_choice = input("What would you like? (espresso/latte/cappuccino):")

    if drink_choice == "report":
        print_report(resources)
        continue

    else:
        if check_resources(drink_choice) == True:

            print("Please insert coins:")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickel = int(input("How many nickels? "))
            penny = int(input("How many pennies? "))

            if process_coins(drink_choice, quarters,dimes,nickel,penny) == True:
                print(f"Here is your {drink_choice}. Enjoy!")

    if input("Would you like to order another drink? 'Y' or 'N': ").upper() == 'Y':
        ok = True
    else:
        ok = False
























