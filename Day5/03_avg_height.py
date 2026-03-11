student_height = input("Input a list of student heights ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
# print(student_height)

total_height = 0
for height in student_height:
    total_height += height

# print(total_height)

count = 0
for a in student_height:
    count += 1
# print(count)

avrage_height = total_height / count
print(round(avrage_height))