# Buffet
# Description: Create a list with only five basic foods
# - Store in a tuple
# - Print each food using for loop
# - Modify one of the items, intentional mistake
# - Change the two items in the tuple and print using for loop

# Creates a tuple with five foods
menu = ('Bulalo', 
        'Sinigang', 
        'Tinola', 
        'Sinigang na Baboy', 
        'Tinolang isda',)

# prints each item in the tuple
print("\nFoods available at this Buffet:")
for soup in menu:
    print(f"- {soup}")

# try changing the tuple (make a mistake)
# menu[-1] = "Batchoy"

# Changes the last two items in the tuple
menu = ('Bulalo', 
        'Sinigang', 
        'Tinola', 
        'Batchoy', 
        'Nilaga',)

# prints each item in the changed tuple
print("\nFoods available at this Buffet:")
for soup in menu:
    print(f"- {soup}")