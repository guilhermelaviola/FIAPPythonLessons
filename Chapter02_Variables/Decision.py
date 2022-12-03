# This simple program shows how decision-making in Python is easy to use to solve problems
# Here you can enter your name, age, and you will get a response based on the degree information you give
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if(age > 16):
    print("Congratulations! You were selected to participate to the next stage of our process!")
    degreeYN = input("Now tell us: Do you have a degree? YES or NO? ").upper()
    if(degreeYN == "YES"):
        degree = input("Tell us your degree: ")
        if(degree == "COMPUTER SCIENCE" or degree == "COMPUTER ENGINEERING"):
            print("Woow! We are really impressed with your academical achievements! We will be emailing you soon!")
        elif(degree == "MARKETING" or degree == "JOURNALISM" or degree == "HUMAN RESOURCES" or degree == "ACCOUNTABILITY"):
            print("Thank you so much for applying for this job! Unfortunately, we are looking for someone for the IT area,"
                  "but don't hesitate to apply for other positions in our company!")
    else:
        print("Thank you so much for applying for this job! Unfortunately, you are not the right fit for us right now.")
elif(age == 16):
    print("You are not qualified for the position yet! But please check out the courses in our website. They can help you"
          "achieve a great position in the future!")
elif(age < 16 and age != 0):
    print("You are still too young to work with us! Take your time, study and come back later! We are sure you can land"
          "a job in our company!")
else:
    print("Please enter a valid age number!")