# Calling the functions to test them on an empty list
from Chapter03_Lists.ListsWithFunctions.Functions import *

myInventory = []
print("Filling inventory...")
fillInventory(myInventory)

print("Displaying inventory...")
displayInventory(myInventory)

print("Searching product...")
searchProduct(myInventory)

print("Giving 10% discount...")
giveDiscount(myInventory)

print("Deleting product...")
deleteProduct(myInventory)

print("Displaying inventory...")
displayInventory(myInventory)

print("Displaying product stats...")
displayProductStats(myInventory)