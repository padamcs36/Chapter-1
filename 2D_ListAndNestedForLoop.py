number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[0][0]) #access indivudual element in list
print(number_grid[2][2])

#Accessing each element in the list by using nested for loop
print("Nested For Loop :")
for row in number_grid:
    for col in row:
        print(col)