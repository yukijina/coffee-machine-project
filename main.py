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


#Prompt user by asking
user_input = input(" What would you like? (espresso/latte/cappuccino): ").lower()

is_machine_operated = True

def check_resources(order):
  """check if there is enough ingredients to make a order"""
  ingredients = MENU[order]['ingredients']

  if order == "espresso":
    if ingredients['water'] < resources['water'] and ingredients['coffee'] < resources['coffee']:
      return True
    else:
      return False
  else:
    
    if ingredients['water'] < resources['water'] and ingredients['coffee'] < resources['coffee'] and ingredients['milk'] < resources['milk']:
      return True
    else:
       return False
  

def insert_coins(order):
  print("Please insert coins.")
  input("How many quarters?: ")
  input("How many dimes?: ")
  input("How many nickles?: ")
  input("How many pennies?: ")


if user_input == "report":
  print(f"Water: {resources['water']} \n Milk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: $0")


if user_input == "off":
  is_machine_operated = False
  
if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
  if check_resources(user_input):
    insert_coins(user_input)
  else:
    print(f"Sorry, there is not enough ingredients to make {user_input}")
  

'''
Coffee Machine Program Requirements
1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
a. b. Check the user’s input to decide what to do next.
The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.
2. Turn off the Coffee Machine by entering “ off ” to the prompt.
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.
3. Print report.
a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
4. Check resources sufficient?
a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “ Sorry there is not enough water.
”
c. The same should happen if another resource is depleted, e.g. milk or coffee.
5. Process coins.
a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.
b. c. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
6. Check transaction successful?
a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “ Sorry that's not enough money. Money refunded.
”
.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.
E.g.
places.
“Here is $2.45 dollars in change.
” The change should be rounded to 2 decimal
7. Make Coffee.
a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
b. E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”
. If
latte was their choice of drink.
'''
