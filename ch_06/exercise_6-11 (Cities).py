# Cities
# Description: Make a dictionary 'cities'
# - name of three cities as keys
# - create a dictionary of information
# - country, population, gdp

# creates a nested dictionary
cities = {
    'Rome': {
        'country': 'Italy',
        'population': 2_873_000,
        'area': '1,285 km^2',
    },

    'Madrid': {
        'country': 'Spain',
        'population': 3_223_000,
        'area': '604.3 km^2',
    },

    'Paris': {
        'country': 'France',
        'population': 2_161_000,
        'area': '105.4 km^2',
    },
}

# prints the information of each city
for city, about in cities.items():
    print(f"\nSome information about the city of {city.title()}:")

    for key, value in about.items():
        print(f"\t{key.title()} of {value}")