# Rivers
# Description: Make a dictionary that contains three major rivers as key
# and countries as value.
# • Use a loop to print a sentence about each river,
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

# empty dictionary for rivers
rivers = {}

# adds key-value pairs in dictionary
rivers['Nile'] = 'Egypt'
rivers['Amazon'] = 'Brazil'
rivers['Yangtze'] = 'China'

# prints a description about each river
desc = [print(f"The '{river.title()}' belongs to the top three longest rivers in the world.") for river in rivers.keys()]

# prints the names of each river
names = [print(f"-{river.title()}") for river in rivers.keys()]

# prints the name of each country
countries = [print(f"-{country.title()}") for country in rivers.values()]