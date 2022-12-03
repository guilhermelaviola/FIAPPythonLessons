# Here you can enter your name and gender and get a response based on it
userLevel = input("Enter your user level - ADMIN, USER or GUEST: ").upper()
userGender = input("Enter your gender - M or F: ").upper()

if (userGender == "M"):
    if (userLevel == "ADMIN"):
        print("Hello Mr. Admin")
    elif (userLevel == "USER"):
        print("Hello Mr. User")
    elif (userLevel == "GUEST"):
        print("Hello Mr. Guest")
    else:
        print("Enter a valid user level!")
elif (userGender == "F"):
    if (userLevel == "ADMIN"):
        print("Hello Mrs. Admin")
    elif (userLevel == "USER"):
        print("Hello Mrs. User")
    elif (userLevel == "GUEST"):
        print("Hello Mrs. Guest")
    else:
        print("Enter a valid user level!")
else:
    print("Enter a valid gender!")