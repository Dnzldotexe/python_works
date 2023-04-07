# Summing a Million
# Description: Make a list of numbers from one to one million
# - Use the min() and max() functions to check if there's one and one million
# - Use the sum() function to print the sum of the million numbers

# creates a list with numbers from one to one million
million = list(range(1, 1_000_001))

# prints the min and max of the list mil
print(f"The Minimum Number is: {min(million)}. \nThe Maximum Number is: {max(million)}.")

# calculates the sum of the million numbers
print(f"The Sum of One to One Million is: {sum(million)}.")