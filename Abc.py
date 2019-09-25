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
    return False

def check_singles(letter, x, y):
    appears_once_horiz = False
    appears_once_vert = False
    for i in range(size):
        #Only one in line?
        if letter in grid[x][i+1]:
            if appears_once_horiz == False:
                appears_once_horiz = True
            else:
                appears_once_horiz = False
                break
        #Only one in column?
        if letter in grid[i+1][y]:
            if appears_once_vert == False:
                appears_once_vert = True
            else:
                appears_once_vert = False
                break
    if appears_once_horiz or appears_once_vert:
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
            if letters == 3:
                line.append(["A", "B", "C"])
            if letters == 4:
                line.append(["A", "B", "C", "D"])
            if letters == 5:
                line.append(["A", "B", "C", "D", "E"])    
        else:
            line.append("/")
    grid.append(line)

#Add the side letters
for i in range(size):
    grid[0][i+1] = alph_order[hor_order[i]]
    grid[size+1][i+1] = alph_order[hor_order[-i-1]]
    grid[i+1][0] = alph_order[ver_order[i]]
    grid[i+1][size+1] = alph_order[ver_order[-i-1]]

#Drawing the STARTING grid
print("\n" + "\x1b[1;33;44m" + " STARTING GRID "  + "\x1b[0m" + "\n")
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

#Dominating letters per line
complete = False
while complete == False:
    complete = True
    for i in range(size):
        for j in range(size):
            if isinstance(grid[i+1][j+1], str):
                continue
            if grid[i+1][j+1].count("_") == 3:
                grid[i+1][j+1] = "_"
            if only_letter(grid[i+1][j+1]) != False:
                check_singles(only_letter(grid[i+1][j+1]), i+1, j+1)
                for k in range(size):
                    if isinstance(grid[k][j+1], list) and grid[i+1][j+1] in grid[k][j+1]:
                        remove(grid[i+1][j+1], grid[k][j+1])
                    if isinstance(grid[i+1][k], list) and grid[i+1][j+1] in grid[i+1][k]:
                        remove(grid[i+1][j+1], grid[i+1][k])
            else:
                complete = False
    for i in range(len(hor_order)):
        for j in range(size - (letters - 1)):
            if alph_order[hor_order[i]] == grid[j+1][i+1]:
                break
            if grid[j+1][i+1] == "_":
                continue
            if alph_order[hor_order[i]] in grid[j+1][i+1] and i == size - (letters - 1):
                grid[j+1][i+1] = alph_order[hor_order[i]]
        else:

    

#Drawing the FINAL grid
print("\n" + "\x1b[1;33;44m" + " FINAL GRID "  + "\x1b[0m" + "\n")
for i in range(size+2):
    print(grid[i])
