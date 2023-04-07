# My Pizzas, Your Pizzas
# Description: Copy the program from exercise 4-1
# - Make a copy of the list and name it friend_pizzas
# - Add new pizza to the original list
# - Add new pizza to the friend_pizza list
# - print both lists

# Creates a list of favorite pizzas
my_pizzas = ["Mozzarella", 
          "Hawaiian", 
          "Pepperoni",]

# Creates a copy of list using slice
friend_pizzas = my_pizzas[:]

# Add new pizzas to each lists
my_pizzas.append("Italian")
friend_pizzas.append("Salami")

# prints each items in my_pizzas
for pizza in my_pizzas:
    print(f"My favorite pizzas are: {pizza}.")

# prints each items in friend_pizzas
for pizza in friend_pizzas:
    print(f"My friend's favorite pizzas are: {pizza}.")