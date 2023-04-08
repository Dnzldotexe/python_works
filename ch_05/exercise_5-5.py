# Alien Colors 3
# Description: create if-elif-else chain from exercise 5-4
# - if green, print 5 points
# - if yellow, print 10 points
# - if red, print 15 points

# initializes variables
alien_color = ['green', 'yellow', 'red',]

# extracts each value in alien_color
for color in alien_color:

    # adds 15 points if red
    score = 0
    if color == 'red':
        score += 15

    # adds 10 points if yellow
    elif color == 'yellow':
        score += 10

    # adds 5 points if green
    else:
        score += 5

    # prints the additional points
    print(f"\nYou just earned +{score} points.")