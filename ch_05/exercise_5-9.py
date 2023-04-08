# No Users
# Description: Test if the list is empty
# - If list is empty, print a message
# - Remove all usernames from list to make sure correct message is printed

# creates a list of usernames
usernames = ["admin", "D", "Da", "Dan", "Danz",]

# empties the list
usernames.clear()

# checks if usernames has items
if usernames:

    # extracts each item in username
    for name in usernames:

        # greets users
        if name.title() != 'Admin':
            print(f"\nHello {name}, thank you for logging in again.")

        # greets admin
        else:
            print(f"\nHello {name.title()}, would you like to see a status report?")

# checks if usernames has items
else:
    print("\nWe need to find some users!")