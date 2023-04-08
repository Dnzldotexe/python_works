# Ordinal Numbers
# Description: Most ordinal numbers end with th;
# - except of 1st, 2nd, and 3rd
# - store the numbers 1-9 in a list
# - loop through the list
# - print the proper ordinal output

# creates a list of numbers 1 to 9
numbers = list(range(1, 10))

# initializes suffix
suffix = ["st", "nd", "rd"] + ["th"] * 6

# extracts each number in numbers
for number in numbers:
    print(f"{number}{suffix[number - 1]}")

# list comprehension version
ordinal = [print(f"{item}{suffix[item - 1]}") for item in range(1, 10)]