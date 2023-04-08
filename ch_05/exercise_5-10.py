# Checking Usernames
# Description: Simulate how websites ensure everyone's username is unique
# - List of five current users
# - Make another list of five new users, two should exist from current users
# - Using a loop, check;
# - If existing, print message asking to create another username
# - If not used, print message saying username is available
# - Make it case sensitive

# creates a list of existing users
current_users = ["admin", "D", "Da", "Dan", "Danz",]

# creates a list of new users
new_users = ["Tony", "D", "Stark", "Jarvis", "Danz",]

current_users_lower = [user.lower() for user in current_users]

# extracts each item in new_users
for user in new_users:
    
    # informs the user that username is available
    if user.lower() not in current_users_lower:
        print(f"\n{user} is available.")

    # prompts the user if username is existing
    else:
        print(f"\n{user} is unavailable, please create another username.")