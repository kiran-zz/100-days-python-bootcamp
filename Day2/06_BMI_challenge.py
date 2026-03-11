height = input("Enter your height in m: \n")

weight = input("Enter your weight in kg: \n")

# My code solution
# height = float(height)
# weight = int(weight)
# heigght_new = height*2
# weight_new = weight/heigght_new

# print(float(weight_new))

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)