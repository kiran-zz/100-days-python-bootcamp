# checking odd or even number by using if else statement
number = int(input("which number do you want to check! "))
result = number % 2
if result == 1:
    print("This is an Odd number.")
else:
    print("This is an Even number.")

# or
    
if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")