# Person
# Description: Using a dictionary
# - Store someone's information
# - Print each information

# Creating an empty dictionary
person = {}

# adding information in the dictionary
person['first_name'] = 'Linus'
person['last_name'] = 'Torvalds'
person['age'] = 53
person['height'] = 1.77
person['city'] = 'Helsinki'

# storing each information in variables
first_name = person['first_name']
last_name = person['last_name']
age = person['age']
height = person['height']
city = person['city']

# doxxing linus torvalds
print(f"\n{first_name} {last_name} lives in {city}, his age is {age} and his height is {height}m.")