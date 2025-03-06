"""Coffee machine project"""
import art

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
machine_profit = 0

print(art.logo)


def check_resources(order):
  """check if there is enough ingredients to make a order"""
  ingredients = order['ingredients']
  for item in ingredients:
    if ingredients[item] <= resources[item]:
      return True
    else:
      print("There is not enough ingredients. Please start over the machine.")
      return False
      

def insert_coins():
  """User inserts coins, check change and give a coffee"""
  print("Please insert coins.")
  quarters = int(input("How many quarters?: ")) * 0.25
  dimes = int(input("How many dimes?: ")) * 0.1
  nickles = int(input("How many nickles?: ")) * 0.05
  pennies = int(input("How many pennies?: ")) * 0.01
  
  sum = quarters + dimes + nickles + pennies
  return sum

def is_transaction_successful(user_money, order):
  """check if user inserted enough money and if there is any change"""
  price = order["cost"]
  
  if user_money < price:
    print(f"{order} costs ${price}. Sorry that's not enough money. Money refunded.💰")
  
  elif user_money >= price:
    change = user_money - price
    global machine_profit
    machine_profit += price
    print(f"total {user_money}, change {change}")

    if change > 0:
      print(f"Here is ${round(change, 2)} in change.")
      
    return True

def make_coffee(order):
  """update resources and serve order"""
  order_ingredients = MENU[order]["ingredients"]
  for item in order_ingredients:
      resources[item] -= order_ingredients[item]
  print(f"Here is your {order}☕️ Enjoy!!") 
  

while IS_MACHINE_OPERATED:

  user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

  if user_input == "report":
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} ml")
    print(f"Money: ${machine_profit}")
  elif user_input == "off":
    #turn off machine -> End the loop
    IS_MACHINE_OPERATED = False
  elif user_input in MENU: 
    drink = MENU[user_input]
    print(f'user {user_input}')
    if check_resources(drink):
      total = insert_coins()
      if is_transaction_successful(total, drink):
        make_coffee(user_input)
      else:
        print(f"Sorry, there is not enough ingredients to make {user_input}")
  else:
    print("Invalid input. Please start again")


