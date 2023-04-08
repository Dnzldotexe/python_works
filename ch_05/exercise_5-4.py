# Alien Colors 2
# Description: Choose a color for alien_color
# - if green, print player earned 5 points
# - if not green, print player earned 10 points

# initializes variables
alien_color = ['green', 'yellow', 'red',]

# extracts each value in alien_color
for color in alien_color:

    # adds 10 points if not green
    score = 0
    if color != 'green':
        score += 10

    # adds 5 points if green
    else:
        score += 5

    # prints the additional points
    print(f"\nYou just earned +{score} points.")