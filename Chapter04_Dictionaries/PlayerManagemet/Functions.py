# Asking the user what function he would like the program to perform
def askUser():
    answer = input("What would you like to do?\n"
             +
            "I - to INSERT a new player\n"
             +
            "S - to SEARCH for a playe\n"
             +
            "D - to DELETE a player\n"
             +
            "L - to LIST a player\n").upper()
    return answer

# Inserting items (players) into the dictionary
def insertPlayer(dictionary):
    dictionary[input("Login: ").upper()] = [input("Name: ").upper(),
                                            input("Number: "),
                                            input("At club since: ")]

# Searching for a player in the dictionary
def searchPlayer(dictionary, key):
    list = dictionary.get(key)
    if list != None:
        print("Name...............: " + list[0])
        print("Number.............: " + list[1])
        print("At club since......: " + list[2])

# Deleting a player from the dictionary
def deletePlayer(dictionary, key):
    if dictionary.get(key) != None:
        del dictionary[key]
    print("Player deleted.")

# Displaying all the players in the dictionary
def getPlayers(dictionary):
    for key, value in dictionary.items():
        print("Object..........: ")
        print("Login...........: ", key)
        print("Data............: ", value)