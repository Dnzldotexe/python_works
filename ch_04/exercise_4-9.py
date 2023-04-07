# Cube Comprehension
# Description: Use a list comprehension to generate a list of the first 10 cubes.

# creates a list of cubes from range 1 to 10
cubes = [cube ** 3 for cube in range(1,11)]

# prints each item in the list
for num in cubes:
    print(num)