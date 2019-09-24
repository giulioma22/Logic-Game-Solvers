import math

#Code for the logic game "Abc"

size = 4
letters = 3
alph_order = ["A", "B", "C", "D", "E", "-"]
hor_order = [2, 1, 2, 0, 2, 0, 2, 1]
ver_order = [2, 0, 0, 1, 2, 1, 1, 0]

empty_arr = []
for i in range(letters):
    empty_arr.append("_")

# #Used to fill cells at the beginning

# init_fill = []

# for i in range(letters):
#     init_fill += alph_order[i]

#Function for removing letter

def remove(letter, cell):
    if letter in cell:
        cell[cell.index(letter)] = "_"
    return

def keep_letter(letter, cell):
    for i in range(len(cell)):
        if cell[i] != letter:
            cell[i] = "_"
    return

def only_letter(cell):
    if cell.count("_") == 2:
        for char in cell:
            if char.isalpha(): 
                return char 
    else:
        return False

def check_line(letter, x, y):
    appears_once = False
    for i in range(size):
        if letter in grid[x][i+1] or letter in grid[i+1][y]:
            if appears_once == False:
                appears_once = True
            else:
                appears_once = False
                break    
    if appears_once == True:
        grid[x][y] = letter
        return
    else:
        return False

#Create the playing grid
grid = []
for i in range(size+2):
    line = []
    for j in range(size+2):
        if i != 0 and i != 5 and j != 0 and j != 5:
            # line.append(init_fill)
            if letters == 3:
                line.append(["A", "B", "C"])
            if letters == 4:
                line.append(["A", "B", "C", "D"])
            if letters == 5:
                line.append(["A", "B", "C", "D", "E"])    
        else:
            line.append("///")
    grid.append(line)

#Add the side letters
for i in range(size):
    grid[0][i+1] = "------" + alph_order[hor_order[i]] + "------"
    grid[size+1][i+1] = "------" + alph_order[hor_order[-i-1]] + "------"
    grid[i+1][0] = "-" + alph_order[ver_order[i]] + "-"
    grid[i+1][size+1] = "-" + alph_order[ver_order[-i-1]] + "-"

#Drawing the STARTING grid
print("\n" + "STARTING GRID")
for i in range(size+2):
    print(grid[i])

#Solving function
for i in range(size):
    keep_letter(alph_order[hor_order[i]], grid[1][i+1])
    keep_letter(alph_order[hor_order[-i-1]], grid[-2][i+1])
    keep_letter(alph_order[ver_order[i]], grid[i+1][1])
    keep_letter(alph_order[ver_order[-i-1]], grid[i+1][-2])
    for j in range(letters-1):
        remove(alph_order[hor_order[i]], grid[-j-2][i+1])
        remove(alph_order[hor_order[-i-1]], grid[j+1][i+1])
        remove(alph_order[ver_order[i]], grid[i+1][-j-2])
        remove(alph_order[ver_order[-i-1]], grid[i+1][j+1])

for i in range(size):
    for j in range(size):
        if only_letter(grid[i+1][j+1]) != False:
            check_line(only_letter(grid[i+1][j+1]), i+1, j+1)

abc = ["_", "_", "C"]

#Drawing the FINAL grid
print("\n" + "FINAL GRID")
for i in range(size+2):
    print(grid[i])
