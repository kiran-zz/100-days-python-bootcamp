row1 = ["0","00","000"]
row2 = ["1","11","111"]
row3 = ["2","22","222"]

# row1 = ["😂","😂","😂"]
# row2 = ["😂","😂","😂"]
# row3 = ["😂","😂","😂"]

map = [row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("where do want to put the tresure?\n")

row = int(position[0])
column = int(position[1])

select = map[row-1] 
select[column-1] = "X"

print(f"{row1}\n{row2}\n{row3}")

