# Glossary 2
# Description: Use a loop on Activity 6-3 when printing
# - Add five (5) new Python terms

# creates a empty dictionary
glossary = {}

# add information to the dictionary
glossary['Omit'] = 'skip or not use'
glossary['Increment'] = 'add something to the original value'
glossary['Loop'] = 'to repeat'
glossary['Variable'] = 'label something'
glossary['Float'] = 'a number with decimal values'
glossary['Lambda'] = 'a keyword that lets you create lambda functions'
glossary['List'] = 'an ordered, mutable collection of objects'
glossary['List Comprehension'] = 'a way to create lists in a concise manner'
glossary['Methods'] = 'functions associated with an object'
glossary['Module'] = 'a file consisting of Python code'

# print each word and the corresponding informations
for word, meaning in glossary.items():
    print(f"\n{word.title()}: {meaning}.")

# list comprehension version
gloss = [print(f"\n{word.title()}: {meaning}.") for word, meaning in glossary.items()]