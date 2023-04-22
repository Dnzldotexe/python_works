# Pets
# Description: Make several dictionaries representing pets
# - include kind animal and owner's name
# - store dictionaries in list 'pets'
# - print using a loop

# creates an empty dictionaries for each animal
animal_one = {}
animal_two = {}
animal_three = {}

# creates an empty list
pets = []

# stores information for animal
animal_one['Animal Type'] = 'Rabbit'
animal_one['Owner'] = 'Anon'

# stores information for animal
animal_two['Animal Type'] = 'Cat'
animal_two['Owner'] = 'Jenny'

# stores information for animal
animal_three['Animal Type'] = 'Bird'
animal_three['Owner'] = 'Debbie'

pets.append(animal_one)
pets.append(animal_two)
pets.append(animal_three)

# prints information on each pet
for pet in pets:
    print("I know the pet's name and his/her owner.")

    for key, value in pet.items():
        print(f"{key}: {value}")