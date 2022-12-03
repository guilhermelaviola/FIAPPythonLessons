# Creating a list, inserting items into it as long as you type 'Y' after inserting a product will all the information
# and printing the 'inventory' list items
inventory = []
answer = "Y"
while answer == "Y":
  inventory.append(input("Product: "))
  inventory.append(float(input("Price: ")))
  inventory.append(int(input("Serial Number: ")))
  inventory.append(input("Departament: "))
  answer = input("Type 'Y' to continue: ").upper()

for e in inventory:
    print(e)