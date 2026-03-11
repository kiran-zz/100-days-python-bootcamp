# Nested if

print("welcome to rollercoaster!")
height = int(input("what is your height in cm?: "))

# if height >= 120:
#     print("You can ride rollercoaster!")
#     age = int(input("Enter your age? : "))
#     if age <= 18:
#         print("You have to $7.")
#     else:
#         print("You have to pay $12.")
# else:
#     print("Sorry, you have to grow taller before you can ride.")

if height >= 120:
    print("You can ride rollercoaster!")
    age = int(input("Enter your age? : "))
    if age <= 12:
        print("you have pay $5.")
    elif age <= 18:
        print("You have to $7.")
    else:
        print("You have to pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")
