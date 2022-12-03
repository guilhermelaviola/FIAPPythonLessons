def callMenu():
    choice = int(input("Digite: "
                   "1 - to register asset"
                   "2 - to persist in file"
                   "3 - to display stored assets: "))
    return choice

def register(dictionary):
    answer = "Y"
    while answer == "Y":
        dictionary[input("Enter the id: ")] =[
            input("Enter the date of the last update: "),
            input("Enter the description: "),
            input("Enter the department: ")]
        answer = input("Type 'Y' to continue: ").upper()

def persist(dictionary):
    with open("inventory.csv", "a") as inv:
        for key, value in dictionary.items:
            inv.write(key + "; " + value[0] + ";" +
                      value[1] + "; " + value[2] + "")
            print("Data persisted successfully!")

def display():
    with open("inventory.csv", "r") as inv:
        lines = inv.readlines()
        return lines
