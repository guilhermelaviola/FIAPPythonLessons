# Creating lists, inserting items into them as long as you type 'Y' after inserting a product will all the information
# and printing the items of all the lists after the product index
products = []
prices = []
serials = []
departments = []
answer = "Y"
while answer == "Y":
  products.append(input("Product: "))
  prices.append(float(input("Price: ")))
  serials.append(int(input("Serial Number: ")))
  departments.append(input("Departament: "))
  answer = input("Type 'Y' to continue: ").upper()

  for index in range(0, len(products)):
    print("Product index........: ", (index + 1))
    print("Product name.........: ", products[index])
    print("Price................: ", prices[index])
    print("Serial...............: ", serials[index])
    print("Departament..........: ", departments[index])

  # Searching an item in the list
  search = input("Enter the product you would like to search for: ")
  for index in range(0, len(products)):
    if search == products[index]:
      print("Product name.........: "), products[index]
      print("Price................: ", prices[index])
      print("Serial...............: ", serials[index])

  # Giving a 10% discount on a product
  deprecation = input("Enter the product name you would like to give a discount: ")
  for index in range(0, len(prices)):
    if deprecation == products[index]:
      formerPrice = prices[index]
      newPrice = prices[index] * 0.9
      print("The product value changed from " + str(formerPrice) + " to " + str(newPrice) + ".")

  # Deleting a product
  serial = int(input("Enter the serial number of the product that you want to delete: "))
  for index in range(0, len(departments)):
    if serials[index] == serial:
      del departments[index]
      del products[index]
      del serials[index]
      del prices[index]
      break

  # Printing products
  for index in range(0, len(products)):
    print("Product index........: ", (index+1))
    print("Product name.........: ", products[index])
    print("Price................: ", prices[index])
    print("Serial...............: ", serials[index])
    print("Departament..........: ", departments[index])