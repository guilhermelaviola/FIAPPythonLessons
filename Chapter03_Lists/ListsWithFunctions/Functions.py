# It's basically the same code from SimpleList2.py, but now it's more structured and organized inside of functions

# Filling an inventory
def fillInventory(inventory):
    answer = "Y"
    while answer == "Y":
      product=[input("Product: "),
                float(input("Price: ")),
                int(input("Serial Number: ")),
                input("Department: ")]
      inventory.append(product)
      answer = input("Enter 'Y' to continue: ").upper()

# Displaying an inventory
def displayInventory(inventory):
    for e in inventory:
      print("Product.........: ", e[0])
      print("Price...........: ", e[1])
      print("Serial..........: ", e[2])
      print("Department......: ", e[3])

# Searching a product in an inventory
def searchProduct(inventory):
    search = input("Enter the name of the product you want to search for: ")
    for e in inventory:
        if search == e[0]:
            print("Price.........: ", e[1])
            print("Serial........: ", e[2])

# Giving product a 10% discount
def giveDiscount(inventory):
    discount = input("Enter the name of the product you want to give a 10% discount: ")
    for e in inventory:
      if discount == e[0]:
        print("Former price: ", e[1])
        e[1] = e[1] * 0.9
        print("New price (with discount): ", e[1])

# Deleting product from an inventory
def deleteProduct(inventory):
    serial = int(input("Enter the serial number of the product you want to delete: "))
    for e in inventory:
        if e[2] == serial:
            inventory.remove(e)
# Displaying product information such as the most expensive, the cheapest and the sum of all prices
def displayProductStats(inventory):
    prices = []
    for e in inventory:
        prices.append(e[1])
    if len(prices) > 0:
        print("The most expensive product costs: ", max(prices))
        print("The cheapest product costs: ", min(prices))
        print("The total price of all products is: ", sum(prices))