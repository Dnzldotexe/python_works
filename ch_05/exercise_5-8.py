# Hello Admin
# Decription: Create a list of five usernames including admin
# Loop through list and greet user
# - if admin, print special Greeting.
# - otherwise, print a generic greeting.

# creates a list of usernames
usernames = ["admin", "D", "Da", "Dan", "Danz",]

# extracts each item in username
for name in usernames:

    # greets users
    if name.title() != 'Admin':
        print(f"\nHello {name}, thank you for logging in again.")

    # greets admin
    else:
        print(f"\nHello {name.title()}, would you like to see a status report?")