print("welcome to rollercoaster!")
height = int(input("what is your height in cm?: "))
bill = 0
if height >= 120:
    print("You can ride rollercoaster!")
    age = int(input("Enter your age? : "))
    if age <= 12:
        bill = 5
        print("child ticket $5.")
    elif age <= 18:
        bill = 7
        print("youth ticket $7.")
    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride with us!")
    else:
        bill = 12
        print("adult ticket $12.")
    wants_photo = input("Do you want photo taken? Y or N.")
    if wants_photo == "Y":
        bill += 3
    print(f"your final bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride.")
