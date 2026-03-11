import random
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

num_items = len(names)
rand_size = random.randint(0,num_items-1)
person_who_pay = names[rand_size]

# alternative code
# person_who_pay = random.choice(names)
print([rand_size])
print( person_who_pay + " is going to buy the meal today!")