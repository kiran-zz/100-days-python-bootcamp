student_scores = [1,2,3,4,6,9,11,5,7,6]

highest_score = 0
for student in student_scores:
    if student > highest_score:
        highest_score = student
print(f"Highest score is: {highest_score}")

count = 0
for student in student_scores:
    count = count + 1
print(f"Total number of sudents: {count}")

total = 0
for student in student_scores:
    total = total + student
print(f"Total marks {total}")

avrage = round(total/count)
print(f"Avrage score: {avrage}")