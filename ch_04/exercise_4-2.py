# Animals
# Description: Think of at least three animals
# - Store animal name in a list 
# - Use a for loop to print out each animal name inside a message
# - Add a message at the end stating their commonalities

# Assigning each animal name to a list: animals
animals = ["Penguin", 
           "Ostrich", 
           "Chicken",]

# prints each item in the list
for animal in animals:
    print(f"\nThe bird: {animal.title()}, can't fly.")

# prints commonalities of these animals
print("\nThese birds can't fly but can lay eggs.")