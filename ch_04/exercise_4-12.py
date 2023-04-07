# More Loops
# Description: Write two for loops to print each items in food.py

# Creates a list of foods
my_foods = ['pizza', 'falafel', 'carrot cake']

# copies the list of foods to another list
friend_foods = my_foods[:]

# adds different items to each lists
my_foods.append('cannoli')
friend_foods.append('ice cream')

# prints each items in foods
print("My favorite foods are:")
for food in my_foods:
    print(f"- {food}")

# prints each items in friend_foods
print("\nMy friend's favorite foods are:")
for food in friend_foods:
    print(f"- {food}")