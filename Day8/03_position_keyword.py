# Positional argument 

# def greet_with(name, location):
#     print(f"Hii, i'm {name}")
#     print(f"I born in {location}")
# greet_with("kiran","mysore")

# Keyword argument

def greet_with(location = "Mysore",name = "kiran"):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
greet_with()

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
greet_with(location = "Mysore",name = "kiran")

greet_with(name = "kiran",location = "Mysore")