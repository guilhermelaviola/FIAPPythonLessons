users = {}
answer = "Y"
emails = []

# The email(s) will be append(ed) to the emails list as long as if you keep typing 'Y'
while answer == "Y":
    emails.append(input("Enter an email:").lower())
    answer == input("Type 'Y' to continue").upper()

    # Once you continue, the emails will be stores into a tuple, then displayed, and inside of that tuple you'll be able
    # to associate two more attributes to the email (which is the key): its name and level (values)
    tuple = list(enumerate(emails))
    for key in range(0, len(tuple)):
        print("Email: ", tuple[key][1])
        users[tuple[key]] = [input("Type the name: "), input("Type the level: ")]

        # Displaying all item in the tuple
        for key, data in users.items():
            print("User: ", key[0])
            print("Email: ", key[1])
            print("Name: ", data[0])
            print("Level: ", data[1])