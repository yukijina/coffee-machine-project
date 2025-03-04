"""Coffee machine project"""

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


IS_MACHINE_OPERATED = True


def check_resources(order):
  """check if there is enough ingredients to make a order"""
  ingredients = MENU[order]['ingredients']


  if order == "espresso":
    #Espresson does not have milk
    if ingredients['water'] <= resources['water'] and ingredients['coffee'] <= resources['coffee']:
      resources['water'] -= ingredients['water']
      resources['coffee'] -= ingredients['coffee']
      return True
    else:
      return False
  else:
    #Latte or cappuccino
    if ingredients['water'] <= resources['water'] and ingredients['coffee'] <= resources['coffee'] and ingredients['milk'] <= resources['milk']:
      resources['water'] -= ingredients['water']
      resources['coffee'] -= ingredients['coffee']
      resources['milk'] -= ingredients['milk']
      return True
    else:
      print("There is not enough ingredients. Please start over the machine.")
      return False
  
  
def insert_coins(order, profit):
  """User inserts coins, check change and give a coffee"""
  print("Please insert coins.")
  quarters = int(input("How many quarters?: "))
  dimes = int(input("How many dimes?: "))
  nickles = int(input("How many nickles?: "))
  pennies = int(input("How many pennies?: "))
  
  total = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
  price = MENU[order]["cost"]
  
  if total < price:
    print(f"{order} costs ${price}. Sorry that's not enough money. Money refunded.💰")
  
  elif total >= price:
    change = total - price
    profit += price
    print(f"total {total}, change {change}")

    if change > 0:
      print(f"Here is ${round(change, 2)} in change.")
      
    print(resources)
    print(profit)
    print(f"Here is your {order}☕️ Enjoy!!")
    return profit
  
machine_profit = 0

while IS_MACHINE_OPERATED:
  try:
    user_input = input(" What would you like? (espresso/latte/cappuccino): ").lower()

    if user_input == "report":
      print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${machine_profit}")
    elif user_input == "off":
      #turn off machine -> End the loop
      IS_MACHINE_OPERATED = False
    elif user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
      if check_resources(user_input):
        profit_result = insert_coins(user_input, machine_profit)
        machine_profit += profit_result 
      else:
        print(f"Sorry, there is not enough ingredients to make {user_input}")

  except ValueError:
    print("Invalid input. Please start again")

