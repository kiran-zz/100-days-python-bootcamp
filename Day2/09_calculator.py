# tip/100*total amount
# 100/10*250 = result
# result / people = result
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $ "))
tip = int(input(f"What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split bill?"))
# tip_with_bill = tip / 100 * bill
tip_as_percentage = tip / 100
total_tip_amount = bill * tip_as_percentage
tatal_bill = bill + total_tip_amount
bill_per_person = tatal_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: $ {final_amount} ")