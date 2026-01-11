def checkDriverAge(age):
# age = int(input("What is your age: "))

    if age < 18:
        print("Sorry, you are too young to drive this  car.Powering Off")
    elif age > 18:
        print("Powering on. Enjoy the ride!")
    elif age == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
    
checkDriverAge(12)    