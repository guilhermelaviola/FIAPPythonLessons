# A simple multiplication table algorithm, with user input
number = int(input("Enter the number you want to see printed in the multiplication table: "))
print("MULTIPLICATION TABLE ", number)
for value in range(1,11,1):
    print(str(number) + " x " + str(value) + " = " + str((number*value)))