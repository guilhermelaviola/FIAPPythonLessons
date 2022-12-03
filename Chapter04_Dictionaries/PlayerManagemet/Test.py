from Chapter04_Dictionaries.PlayerManagemet.Functions import *

# Creting an empty dictionary to store players
players = {}

# Calling the function to ask the user what he would like the software to perform
option = askUser()

while option == "I" or option == "S" or option == "D" or option == "L":
    if option == "I":
        insertPlayer(players)
    if option == "S":
        searchPlayer(players, input("What player would you like to search for? "))
    if option == "D":
        deletePlayer(players, input("What player would you like to delete? "))
    if option == "L":
        getPlayers(players)

option = askUser()
