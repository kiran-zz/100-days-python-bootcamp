import os

os.system("cls")

# Simple function

# def greet():
#     print("Hello")
#     print("How do you do?")
#     print("Isn't the weather nice today?")

# greet()


# Function that allows for input

# name = "kiran"

# def greet_with_input(name):
#     print(f"Hello {name}")
#     print(f"How do you do? {name}")
#     print(f"Isn't the weather nice today? {name}")

# greet_with_input(name)

name = input("Enter your name: ")

def greet(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")
    print(f"Isn't the weather nice {name}")
greet(name)

def greet_with_input(name):
    print(f"Hello {name}")
    print(f"How do you do? {name}")
    print(f"Isn't the weather nice today? {name}")

greet_with_input("kiran")




