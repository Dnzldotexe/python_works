# Stages of Life
# - Description: determine stages of life using if-elif-else chain
# - set variable for age
# - if age less than 2, print baby 
# - if age less than 4, print toddler 
# - if age less than 13, print kid 
# - if age less than 20, print teenager 
# - if age less than 65, print adult
# - if age greater than 65, print elder

# initializes variables
ages = ['75', '1', '13', '22', '8', '2',]

# extracts each value in ages
for age in ages:

    # - if age less than 2, print baby 
    if int(age) < 2:
        person = 'a Baby'

    # - if age less than 4, print toddler 
    elif int(age) < 4:
        person = 'a Toddler'

    # - if age less than 13, print kid 
    elif int(age) < 13:
        person = 'a Kid'

    # - if age less than 20, print teenager
    elif int(age) < 20:
        person = 'a Teenager'

    # - if age less than 65, print adult
    elif int(age) < 65:
        person = 'an Adult'

    # - if age greater than 65, print elder
    else:
        person = 'an Elder'

    # prints stage in life
    print(f"\nYou're {person}!")