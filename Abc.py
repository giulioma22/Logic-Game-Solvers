import math

#Data of playing grid

# size = 5
# letters = 3
# hor_order = [0, 0, 2, 2, 0]
# hor_order_rev = [0, 1, 0, 3, 0]
# ver_order = [0, 2, 2, 0, 0]
# ver_order_rev = [0, 1, 0, 0, 0]

size = 5
letters = 3
hor_order = [3, 1, 1, 2, 2]
hor_order_rev = [2, 2, 2, 3, 1]
ver_order = [3, 1, 2, 2, 2]
ver_order_rev = [2, 3, 1, 1, 1]

# size = int(input("Enter grid size: "))
# letters = int(input("Enter number of different letters (e.g. 3 if A, B and C): "))
# hor_order = []
# hor_order_rev = []
# ver_order = []
# ver_order_rev = []

# print("Enter top-border letters, left to right one at a time (0 = blank, 1 = A, 2 = B, ...): ")
# for i in range(size):    
#     hor_order.append(int(input()))
# print("Enter bottom-border letters, left to right: ")
# for i in range(size):    
#     hor_order_rev.append(int(input()))
# print("Enter each left-border letter, top to bottom: ")
# for i in range(size):    
#     ver_order.append(int(input()))
# print("Enter each right-border letter, top to bottom: ")
# for i in range(size):    
#     ver_order_rev.append(int(input()))

for i in range(size):
    hor_order.append(hor_order_rev[-i-1])
    ver_order.append(ver_order_rev[-i-1])

lower_limit = size - (letters - 1)
alph_order = ["_", "A", "B", "C", "D", "E", "F"]

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

#Remove letter from cell
def remove(letter, cell):
    if letter in cell and letter != "_":
        cell[cell.index(letter)] = "_"
    return

#Keep only that letter in cell
def keep_letter(letter, cell):
    if letter != "_":
        for i in range(len(cell)):
            if cell[i] != letter:
                cell[i] = "_"
    return

#Clear lines
def clear_lines():
    complete_grid = 0
    for i in range(size):
        for j in range(size):
            if isinstance(grid[i+1][j+1], str):
                complete_grid += 1
                if grid[i+1][j+1] != "_":
                    for k in range(size):
                        if isinstance(grid[k+1][j+1], list) and grid[i+1][j+1] in grid[k+1][j+1]:
                            remove(grid[i+1][j+1], grid[k+1][j+1])
                        if isinstance(grid[i+1][k+1], list) and grid[i+1][j+1] in grid[i+1][k+1]:
                            remove(grid[i+1][j+1], grid[i+1][k+1])
    return complete_grid

#Checks if array has only 1 letter
def only_letter(cell):
    if cell.count("_") == 2:
        for char in cell:
            if char.isalpha(): 
                return char
    return False

#Check single letters
def check_singles(letter, x, y):
    appears_once_horiz = False
    appears_once_vert = False
    switch_hor = False
    switch_ver = False

    for i in range(size):
        #Only one in line?
        if letter in grid[x][i+1]:
            if appears_once_horiz == False and switch_hor == False:
                appears_once_horiz = True
            else:
                appears_once_horiz = False
                switch_hor = True
                #break
        #Only one in column?
        if letter in grid[i+1][y]:
            if appears_once_vert == False and switch_ver == False:
                appears_once_vert = True
            else:
                appears_once_vert = False
                switch_ver = True
                #break

    if appears_once_horiz == True or appears_once_vert == True:
        grid[x][y] = letter
        return
    else:
        return False

#Check side letter conditions
def side_priority(grid_side):
    for i in range(size):
        switch_top = False
        switch_bottom = False
        switch_left = False
        switch_right = False
        for j in range(lower_limit):
            # if j == lower_limit:
            #     cell_value = side_letter
            #     break
            if grid_side == "top":
                cell_value = grid[j+1][i+1]
                if alph_order[hor_order[i]] != "_":
                    side_letter = alph_order[hor_order[i]]
                    if side_letter in cell_value:
                        switch_top = True
                        if side_letter == cell_value:
                            break
                    if side_letter not in cell_value and switch_top == False:
                        grid[j+1][i+1] = "_"
            if grid_side == "bottom":
                cell_value = grid[-j-1][i+1]
                if alph_order[hor_order[-i-1]] != "_":
                    side_letter = alph_order[hor_order[-i-1]]
                    if side_letter in cell_value:
                        switch_bottom = True
                        if side_letter == cell_value:
                            break
                    if side_letter not in cell_value and switch_bottom == False:
                        grid[-j-1][i+1] = "_"
            if grid_side == "left":
                cell_value = grid[i+1][j+1]
                if alph_order[ver_order[i]] != "_":
                    side_letter = alph_order[ver_order[i]]
                    if side_letter in cell_value:
                        switch_left = True
                        if side_letter == cell_value:
                            break
                    if side_letter not in cell_value and switch_left == False:
                        grid[i+1][j+1] = "_"
            if grid_side == "right":
                cell_value = grid[i+1][-j-1]
                if alph_order[ver_order[-i-1]] != "_":
                    side_letter = alph_order[ver_order[-i-1]]
                    if side_letter in cell_value:
                        switch_right = True
                        if side_letter == cell_value:
                            break
                    if side_letter not in cell_value and switch_right == False:
                        grid[i+1][-j-1] = "_"

    return


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


#Create the playing grid
grid = []

for i in range(size+2):
    line = []
    for j in range(size+2):
        if i != 0 and i != size+1 and j != 0 and j != size+1:
            line.append("_")  
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

grid = []

for i in range(size+2):
    line = []
    for j in range(size+2):
        if i != 0 and i != size+1 and j != 0 and j != size+1:
            if letters == 3:
                line.append(["A", "B", "C"])
            if letters == 4:
                line.append(["A", "B", "C", "D"])
            if letters == 5:
                line.append(["A", "B", "C", "D", "E"])
            if letters == 6:
                line.append(["A", "B", "C", "D", "E", "F"])      
        else:
            line.append("/")
    grid.append(line)

#Add the side letters
for i in range(size):
    grid[0][i+1] = alph_order[hor_order[i]]
    grid[size+1][i+1] = alph_order[hor_order[-i-1]]
    grid[i+1][0] = alph_order[ver_order[i]]
    grid[i+1][size+1] = alph_order[ver_order[-i-1]]

# print("\n")
# for i in range(size+2):
#     print(grid[i])

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

# print("\n")
# for i in range(size+2):
#     print(grid[i])

#Dominating letters per line
complete_grid = 0
last_grid = []
same_grid = False

while complete_grid != size**2:# and same_grid == False:
    for i in range(size):
        for j in range(size):
            if grid[i+1][j+1].count("_") == letters:
                grid[i+1][j+1] = "_"
                continue
            if isinstance(grid[i+1][j+1], list):
                for l in range(letters):
                    if alph_order[l+1] in grid[i+1][j+1]:
                        check_singles(alph_order[l+1], i+1, j+1)

    complete_grid = clear_lines()
    # if last_grid != grid:
    #     last_grid = grid
    # else:
    #     same_grid = True
    #     print("\n" + "\x1b[1;33;41m" + " ERROR: infine loop " + "\x1b[0m")

    print("\n")
    for t in range(size+2):
        print(grid[t])

    #Side constraints check
    side_priority("top")
    side_priority("bottom")
    side_priority("left")
    side_priority("right")

#Drawing the FINAL grid
print("\n" + "\x1b[1;33;44m" + " FINAL GRID " + "\x1b[0m" + "\n")
for i in range(size+2):
    print(grid[i])
