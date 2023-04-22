# Polling
# Description: Use the code favourite_languages on page 96
# - Make a list of additional names
# - Thank them if they took the poll
# - Invite if not

# dictionary code from page 96
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

# list of additional names
people = [
    'james',
    'jenny',
    'jen',
    'rose',
    'debbie',
    'sarah',
    'edward',
    'phil',
]

# checks if the person took the poll
for person in people:

    # asks the person to take the poll
    if person not in favorite_languages.keys():
        print(f"{person.title()}, please take the poll :P.")

    # appreciation for taking the poll
    else:
        print(f"{person.title()}, thank you for taking the poll UwU.")