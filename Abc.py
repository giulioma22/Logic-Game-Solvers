import math

#Code for the logic game "Abc"

size = 4
letters = 3
alph_order = ["A", "B", "C", "D", "E"]
order = [3, 2, 3, 1, 1, 2, 2, 3, 3, 1, 3, 2, 2, 1, 1, 3]

# def draw_grid(size):
#     for i in range(size):
#         print("+ - - - " * size + "+ \n" + ("|   " + str(letters) + "   ") * size + "|" )
#     print("+ - - - " * size + "+")
#     return

# draw_grid(4)

# grid = [[".", "A", "B", "C"], ["A", ".", "B", "C"], ["A", "B", ".", "C"], ["A", "B", "C", "."]]

#Used to fill cells at the beginning

init_fill = ""

for i in range(letters):
    init_fill += alph_order[i]
print(init_fill)

#Create the playing grid
grid = []
for i in range(size+2):
    for j in range(size+2):
        grid.append([])

# #Drawing the grid
# for i in range(size):
#     print(grid[i])