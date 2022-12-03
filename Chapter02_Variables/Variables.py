# This shows how variable declaration with and without user input work
manager = input("Enter the manager name: ")
employee = input("Enter the employee name: ")
event = "Python Basin Programming Workshop"
price = float(input("Enter the value to be refunded: "))

print("I declare to Mr(s) " + manager + ", that Mr(s) " + employee +
          " was present at " + event + " and spent a total value of US$ " + str(price))