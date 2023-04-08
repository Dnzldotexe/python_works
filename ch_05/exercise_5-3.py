# Alien Colors 1
# Description: Store value green, yellow, red in alien_color
# - If alien_color is green, print message player earned 5 points
# - Write one version that passes, and the other fails without output

# initializes variables
alien_color = ['green', 'yellow', 'red',]

# extracts each value in alien_color
for color in alien_color:

    # adds 5 points if color is green
    score = 0
    if color == 'green':
        score += 5

    # prints the player's score
    print(f"\nPlayer +{score} points.")