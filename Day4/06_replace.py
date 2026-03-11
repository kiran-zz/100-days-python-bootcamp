# row1 = ["0","00","000"]
# row2 = ["1","11","111"]
# row3 = ["2","22","222"]

row1 = ["😂","😂","😂"]
row2 = ["😂","😂","😂"]
row3 = ["😂","😂","😂"]

map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do want to put the tresure?\n")

horizontal = int(position[0])
verticle = int(position[1])

selected_row = map[verticle - 1]
selected_row[horizontal - 1] = "X"

# map[verticle - 1][horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

