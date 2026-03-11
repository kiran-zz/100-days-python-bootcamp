year = int(input("which year do you want to check: \n"))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")


# if year % 4 == 0:
#     print("it is leap year")
# elif year % 100 == 0:
#     print("it is not leap year")
# elif year % 400 == 0:
#     print("it is leap year")
# else:
#     print("it is not leap year")
# print(year)