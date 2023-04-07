# More Conditional Tests
# Description: Create more conditional tests
# - Tests for equality and inequality with strings
# - Tests using the lower() method
# - Numerical tests involving equality and inequality, 
#       greater than and less than, greater than or equal to, 
#       and less than or equal to
# - Tests using the and keyword and the or keyword
# - Test whether an item is in a list
# - Test whether an item is not in a list

# Test for equality and inequality in strings
cat = 'mouse'
mouse = 'cat'
print(mouse == 'cat') # True
print(cat == 'cat') # False
print(mouse == 'mouse') # False
print(cat == 'mouse') # True

# Tests with lower() method
print(mouse.lower() == 'mouse') # False
print(cat.lower() == 'mouse') # True

# Numerical Tests
num, nums = 18, 19
print(num > nums) # False
print(num < nums) # True
print(num == nums) # False
print(num <= nums) # True

# Tests using the keyword and and keyword or
# Numerical Tests
num, nums = 18, 19
print((num > nums) and (num < nums)) # False
print((num == nums) and (num > nums)) # False
print((num > nums) or (num < nums)) # True
print((num == nums) or (num < nums)) # True

# Test if in and if item not in list
nums = list(range(1, 11))
print(19 in nums) # False
print(1 in nums) # True
print(0 in nums) # False
print(10 in nums) # True