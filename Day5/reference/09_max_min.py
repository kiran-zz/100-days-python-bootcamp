numbers = [6,4,88,1,2,9,66,99,201,8,3]

max_num = 0

for num in numbers:
    if num > max_num:
        max_num = num
print(max_num)


mini_num = numbers[0]

for num in numbers:
    if num < mini_num:
        mini_num = num
print(mini_num)
