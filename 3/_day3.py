print("Welcome to the rollercoaster!")
height = int(input("Insert your height in cm: "))
if height > 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry, you have grow taller tha 120 cm")


# Odd or Even
number = int(input("Number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Nested if - elif
print("Welcome to the rollercoaster!")
height = int(input("Insert your height in cm: "))
age = int(input("How old are you?"))
if height > 120:
    print("You can ride the rollercoaster")
    if age < 12:
        bill = 5
        print("You have to pay $5")
    elif age <= 18:
        bill = 7
        print("You have to pay $7")
    else:
        bill = 12
        print("You have to pay $12")
    wants_photo = input("Want a photo? [y/n]")
    if wants_photo == "y":
        bill += 3
    print(f"You have to pay ${bill}")
else:
    print("Sorry, you have grow taller tha 120 cm")




# Leap Year
year = int(input("Insert a year: "))
if year % 4 == 0:
    if  year % 100 == 0:
        if  year % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap Year")




# Logical operators
print("Diegod".lower().count("d"))

name1 = input("First Name: ")
name2 = input("Second Name: ")
combined_string = (name1+name2).lower()
t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")
true = t+r+u+e
l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")
love = l+o+v+e
score = int(str(true) + str(love))
if score > 10 and score < 90:
    if score < 10:
        print(f"Your scrore is {score}, you go together like coke and mentos")
    elif score > 40 and score < 50:
        print(f"Your scrore is {score}, you go good together")
    else:
        print(f"Your scrore is {score}")




