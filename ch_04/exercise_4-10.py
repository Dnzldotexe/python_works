# Slices
# Description: Create a list with 9 items
# - Print the first three items in the list using slice
# - Print the middle three items in the list using slice
# - Print the last three items in the list using slice

# creates a list with 9 items
nums = list(range(1,10))

# prints the first three items in the list
for value in nums[:3]:
    print(f"The first three items in the list are: {value}.")

# prints the middle three items in the list
for value in nums[3:6]:
    print(f"The items from the middle of the list are: {value}.")

# prints the last three items in the list
for value in nums[6:9]:
    print(f"The last three items in the list are: {value}.")