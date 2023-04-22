# People
# Description: From Exercise 6-1. Make two new dictionaries
# representing different people
# - store all three dictionaries in a list 'people'
# - loop through the list
# - print everything about the person

# Creating an empty dictionary
person = {}
person_one = {}
person_two = {}

# Creating an empty list
people = []

# adding information in the dictionary
person['first_name'] = 'Linus'
person['last_name'] = 'Torvalds'
person['age'] = 53
person['height'] = 1.77
person['city'] = 'Helsinki, Finland'

# adding information in the dictionary
person_one['first_name'] = 'Bill'
person_one['last_name'] = 'Gates'
person_one['age'] = 67
person_one['height'] = 1.77
person_one['city'] = 'Seattle, Washington, United States'

# adding information in the dictionary
person_two['first_name'] = 'Paul'
person_two['last_name'] = 'Allen'
person_two['age'] = 65
person_two['height'] = 1.78
person_two['city'] = 'Seattle, Washington, United States'

# stores dictionaries to a list
people = [
    person, 
    person_one, 
    person_two,
]

# prints each person and their information
for someone in people:
    first_name = someone['first_name']
    last_name = someone['last_name']
    age = someone['age']
    height = someone['height']
    city = someone['city']

    # doxxing those people
    print(f"\n{first_name} {last_name} lives in {city}, "
          f"his age is {age} and his height is {height}m.")