# Favorite Places
# Description: Create a dictionary
# - with at least three key
# - value is a list

# creates an empty dictionary
friends = {}

# adds information to the dictionary
friends['Spongebob'] = ['Bikini Bottom', "Mariana's Trench", "Krusty Krab"]
friends['Patrick'] = ["Jellyfish Fields", "Krusty Krab"]
friends['Gary'] = ["Spongebob's House"]
friends['Squidward'] = ['Cash Register', "Theather", "Krusty Krab"]

# prints every information
for friend, places in friends.items():
    
    if len(places) < 2:
        print(f"\n{friend.title()}'s favorite place is {places[0].title()}")

    else:
        print(f"\n{friend.title()}'s favorite places are:")
        for place in places:
            print(f"\t-{place.title()}")