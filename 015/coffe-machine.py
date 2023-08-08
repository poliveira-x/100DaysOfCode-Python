#
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


profit = 0.0


#
#
#

# Report
def report():
    print("="*15)
    for i in resources:
        print(f"{i}: {resources[i]}")
    print(f"profit ${profit:,.2f}")
    print("="*15)
    


# Check suficient ressources
def check_sufficient(option):
    for i in MENU[option]['ingredients']:
        if resources[i] < MENU[option]['ingredients'][i]:
            return i
    return True



# Make changes on ingredients and profit
def inventory(option):
    for i in MENU[option]['ingredients']:
        resources[i] -= MENU[option]['ingredients'][i]

    return MENU[option]['cost']
    


# Process Coins
def process_coins(option):
    cost =  MENU[option]['cost']
    print("\nPlease insert coins.")
    quarters = int(input("How many quarter? "))*0.25
    dimes = int(input("How many dimes? "))*0.1
    nickels = int(input("Hop many nickels? "))*0.05
    pennies = int(input("How many pennies? "))*0.01

    total = quarters+dimes+nickels+pennies
    
    if total < cost:
        print("\nSorry, that's not enough money. Money refunded.\n")
        return 0
    elif total > cost:
        print(f"\nHere is ${total-cost:,.2f} in change.\n")
    
    print(f"\nHere is your {option}. Enjoy!\n")
   
    return inventory(option)



#
# main
#
while True:
    option = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if option == 'off':
        print("\nTurning off...\n")
        break
    elif option == 'report':
        report()
        continue

    if option in ['espresso', 'latte', 'cappuccino']:
        sufficient = check_sufficient(option)
        if sufficient != True:
             print(f"\nThere's not enough {sufficient}.\n")
             continue

    if option == 'espresso' and sufficient:
        profit += process_coins(option)
    elif option == 'latte' and sufficient:
        profit += process_coins(option)
    elif option == 'cappuccino' and sufficient:
        profit += process_coins(option)
    else:
        print("\nInvalid option, try again.\n")


