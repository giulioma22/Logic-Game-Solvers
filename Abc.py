import math

#Code for the logic game "Abc"

size = 4
letters = 3
alph_order = ["A", "B", "C", "D", "E", "-"]
hor_order = [2, 1, 2, 0, 2, 0, 2, 1]
ver_order = [2, 0, 0, 1, 2, 1, 1, 0]

#Used to fill cells at the beginning

init_fill = ""

for i in range(letters):
    init_fill += alph_order[i]

# init_array = []
# for i in range(size+2):
#     init_array.append(init_fill)

#Create the playing grid
grid = []
for i in range(size+2):
    line = []
    for j in range(size+2):
        if i != 0 and i != 5 and j != 0 and j != 5:
            line.append(init_fill)
        else:
            line.append("___")
    grid.append(line)

#Add the side letters
for i in range(size):
    grid[0][i+1] = "_" + alph_order[hor_order[i]] + "_"
    grid[size+1][i+1] = "_" + alph_order[hor_order[-i-1]] + "_"
    grid[i+1][0] = "_" + alph_order[ver_order[i]] + "_"
    grid[i+1][size+1] = "_" + alph_order[ver_order[-i-1]] + "_"

#Drawing the grid
for i in range(size+2):
    print(grid[i])

#Heuristic function


