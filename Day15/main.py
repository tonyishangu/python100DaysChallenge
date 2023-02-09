# COFFEE MACHINE
# Requirements
# ------Print Report
# ------check resources sufficient?
# ------process coins
# ------check transaction successful?
# ------make coffee

profit = 0
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
# TODO  Check resources sufficient?
def sufficient_resources(order_ingredients):
    '''return true if order can be made, false if there are insufficient resources'''
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f'Sorry, There is not enough {item}.')
            return False
    return True

# TODO  Process coins.
def process_coins():
    '''return total calculated coins inserted'''
    print('Please insert coins.')
    total = int(input('How many quaters')) * 0.25
    total += int(input('How many dimes')) * 0.1
    total += int(input('How many nickles')) * 0.05
    total += int(input('How many pennies')) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    '''return true if payment is accepted, false is money is insufficient'''
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f'Here is {change} in change.')
        global profit
        profit += drink_cost
        return True
    else:
        print('Insufficient funds. Money refunded')
        return False
    
# TODO  Make Coffee.
def make_coffee(drink_name, order_ingeridient):
    '''deduct resources as needed'''
    for item in order_ingeridient:
        resources[item] -= order_ingeridient[item]
    print(f'Here is your {drink_name}. Enjoy')

# TODO  Turn off the Coffee Machine by entering “off” to the prompt.
is_on = True

while is_on:
    # TODO  Prompt user by asking “What would you like? (espresso/latte/cappuccino)
    choice = input('What would you like? expresso/latte/cappuccino').lower()
    if choice == 'off':
        is_on = False
        print('Enjoy your coffee')
    # TODO  Print report.
    elif choice == 'report':
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}ml')
        print(f'Money: {profit}ml')
    else:
        drink = MENU[choice]
        if sufficient_resources(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])



