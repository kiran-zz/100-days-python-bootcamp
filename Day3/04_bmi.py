height = input("Enter your height in m: \n")

weight = input("Enter your weight in kg: \n")

bmi = round(float(weight) / float(height) ** 2)
bmi_as_int = round(float(bmi))

if bmi_as_int < 18.5:
    print(f"Your bmi is {bmi_as_int} you are underweight")
elif bmi_as_int < 25:
    print(f"Your bmi is {bmi_as_int} you are normal weight")
elif bmi_as_int < 30:
    print(f"Your bmi is {bmi_as_int} you are overweight")
elif bmi_as_int < 35:
    print(f"Your bmi is {bmi_as_int} you are obese")
else:
    print(f"Your bmi is {bmi_as_int} you areclinically obese")