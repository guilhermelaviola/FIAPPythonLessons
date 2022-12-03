from Functions.Functions import *

inventory = {}

option = callMenu()

while option > 0 and option < 4:
    if option == 1:
        register(inventory)
    elif option == 2:
        persist(inventory)
    elif option == 3:
        result = display()
        for line in result:
            print(line[line.find(";")+1:-1])
    option = callMenu()