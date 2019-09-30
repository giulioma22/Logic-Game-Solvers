
# I N P U T   D A T A - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# size = 6
# letters = 4
# hor_order = [3, 0, 0, 4, 0, 1]
# hor_order_rev = [0, 1, 4, 2, 0, 3]
# ver_order = [0, 0, 4, 4, 4, 1]
# ver_order_rev = [0, 0, 1, 0, 2, 3]

# size = 5
# letters = 3
# hor_order = [0, 2, 3, 2, 3]
# hor_order_rev = [0, 0, 1, 3, 1]
# ver_order = [0, 3, 3, 2, 2]
# ver_order_rev = [0, 0, 2, 1, 1]

size = int(input("Enter grid SIZE: "))
letters = int(input("Enter number of DIFFERENT LETTERS (e.g. 3 if A, B and C): "))
hor_order = []
hor_order_rev = []
ver_order = []
ver_order_rev = []

#User input commands
print("Enter TOP-border letters, left to right one at a time (0 = blank, 1 = A, 2 = B, ...): ")
for i in range(size):    
    hor_order.append(int(input()))
print("Enter BOTTOM-border letters, left to right: ")
for i in range(size):    
    hor_order_rev.append(int(input()))
print("Enter LEFT-border letters, top to bottom: ")
for i in range(size):    
    ver_order.append(int(input()))
print("Enter RIGHT-border letters, top to bottom: ")
for i in range(size):    
    ver_order_rev.append(int(input()))

#Ordering arrays
for i in range(size):
    hor_order.append(hor_order_rev[-i-1])
    ver_order.append(ver_order_rev[-i-1])

lower_limit = size - (letters - 1)
alph_order = ["_", "A", "B", "C", "D", "E", "F"]


# F U N C T I O N S - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

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

#Check and confirm single letters
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
        #Only one in column?
        if letter in grid[i+1][y]:
            if appears_once_vert == False and switch_ver == False:
                appears_once_vert = True
            else:
                appears_once_vert = False
                switch_ver = True
    
    #Confirm single letters
    if appears_once_horiz == True or appears_once_vert == True:
        grid[x][y] = letter
        return
    else:
        return False

#Check side letter conditions
def side_priority(grid_side):
    for i in range(size):
        switch_encount = 0
        first_cell = []
        for j in range(lower_limit):
            if grid_side == "top":
                cell_value = grid[j+1][i+1]
                if alph_order[hor_order[i]] != "_":
                    side_letter = alph_order[hor_order[i]]
                    if side_letter in cell_value:
                        if switch_encount == 0:
                            first_cell = [j+1, i+1]
                        switch_encount += 1
                        if side_letter == cell_value:
                            break
                    else:
                        if switch_encount == 0:
                            grid[j+1][i+1] = "_"
                        if isinstance(cell_value, str) and cell_value != "_" and switch_encount == 1:
                            grid[first_cell[0]][first_cell[1]] = side_letter
                            break
            if grid_side == "bottom":
                cell_value = grid[-j-2][i+1]
                if alph_order[hor_order[-i-1]] != "_":
                    side_letter = alph_order[hor_order[-i-1]]
                    if side_letter in cell_value:
                        if switch_encount == 0:
                            first_cell = [-j-2, i+1]
                        switch_encount += 1
                        if side_letter == cell_value:
                            break
                    else:
                        if switch_encount == 0:
                            grid[-j-2][i+1] = "_"
                        if isinstance(cell_value, str) and cell_value != "_" and switch_encount == True:
                            grid[first_cell[0]][first_cell[1]] = side_letter
                            break
            if grid_side == "left":
                cell_value = grid[i+1][j+1]
                if alph_order[ver_order[i]] != "_":
                    side_letter = alph_order[ver_order[i]]
                    if side_letter in cell_value:
                        if switch_encount == 0:    
                            first_cell = [i+1, j+1]
                        switch_encount += 1
                        if side_letter == cell_value:
                            break
                    else:
                        if switch_encount == 0:
                            grid[i+1][j+1] = "_"
                        if isinstance(cell_value, str) and cell_value != "_" and switch_encount == True:
                            grid[first_cell[0]][first_cell[1]] = side_letter
                            break
            if grid_side == "right":
                cell_value = grid[i+1][-j-2]
                if alph_order[ver_order[-i-1]] != "_":
                    side_letter = alph_order[ver_order[-i-1]]
                    if side_letter in cell_value:
                        if switch_encount == 0:
                            first_cell = [i+1, -j-2]
                        switch_encount += 1
                        if side_letter == cell_value:
                            break
                    else:
                        if switch_encount == 0:
                            grid[i+1][-j-2] = "_"
                        if isinstance(cell_value, str) and cell_value != "_" and switch_encount == True:
                            grid[first_cell[0]][first_cell[1]] = side_letter
                            break

    return

#Check if matrix did (not) change after 1 loop
def is_same_matrix(last_grid, grid):
    same_matrix = True
    for i in range(size):
        for j in range(size):
            if len(last_grid[i+1][j+1]) == len(grid[i+1][j+1]):
                if isinstance(last_grid[i+1][j+1], list):
                    for k in range(letters):
                        if last_grid[i+1][j+1][k] != grid[i+1][j+1][k]:
                            last_grid[i+1][j+1][k] = grid[i+1][j+1][k]
                            same_matrix = False
                else:
                    if last_grid[i+1][j+1] != grid[i+1][j+1]:
                        last_grid[i+1][j+1] = grid[i+1][j+1]
                        same_matrix = False
            else:
                same_matrix = False
                if isinstance(grid[i+1][j+1], list):
                    last_grid[i+1][j+1] = []
                    for k in range(letters):
                        last_grid[i+1][j+1].append(grid[i+1][j+1][k])
                else:
                    last_grid[i+1][j+1] = grid[i+1][j+1]
    return same_matrix


# I N I T I A L I Z E   G R I D - - - - - - - - - - - - - - - - - - - - - - - - - -

grid = []
last_grid = []

#Create the playing grid
for i in range(size+2):
    grid.append([])
    last_grid.append([])
    for j in range(size+2):
        if i != 0 and i != size+1 and j != 0 and j != size+1:
            grid[i].append("_")
            last_grid[i].append("_")
        else:
            grid[i].append("/")
            last_grid[i].append("/")

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

#Fill cells with all-letters array
for i in range(size):
    for j in range(size):
        if letters == 3:
            grid[i+1][j+1] = ["A", "B", "C"]
        if letters == 4:
            grid[i+1][j+1] = ["A", "B", "C", "D"]
        if letters == 5:
            grid[i+1][j+1] = ["A", "B", "C", "D", "E"]
        if letters == 6:
            grid[i+1][j+1] = ["A", "B", "C", "D", "E", "F"]


# M A I N   A L G O R I T H M - - - - - - - - - - - - - - - - - - - - - - - - - - -

exit_loop = False
same_grid = False
complete_grid = 0
offset = 1

while complete_grid != size**2 and exit_loop == False:
    same_grid = False

    #1st WHILE - Excluding possibilities
    while same_grid == False: 
        #print("\nNEW 1st WHILE\n")
        for i in range(size):
            top_max = letters - 1
            bottom_max = letters - 1
            left_max = letters - 1
            right_max = letters - 1

            #From opposite end
            for j in range(size):
                if top_max > 0:
                    if isinstance(grid[-j-2][i+1], list):
                        remove(alph_order[hor_order[i]], grid[-j-2][i+1])
                        top_max -= 1
                    else:
                        if grid[-j-2][i+1] != "_":
                            top_max -= 1
                if bottom_max > 0:
                    if isinstance(grid[j+1][i+1], list):
                        remove(alph_order[hor_order[-i-1]], grid[j+1][i+1])
                        bottom_max -= 1
                    else:
                        if grid[j+1][i+1] != "_":
                            bottom_max -= 1
                if left_max > 0:
                    if isinstance(grid[i+1][-j-2], list):
                        remove(alph_order[ver_order[i]], grid[i+1][-j-2])
                        left_max -= 1
                    else:
                        if grid[i+1][-j-2] != "_":
                            left_max -= 1
                if right_max > 0:
                    if isinstance(grid[i+1][j+1], list):
                        remove(alph_order[ver_order[-i-1]], grid[i+1][j+1])
                        right_max -= 1
                    else:
                        if grid[i+1][j+1] != "_":
                            right_max -= 1
            
            #From first cell close to border, skip when no border letter
            #TOP border
            if hor_order[i] != 0:
                for j in range(size):
                    if alph_order[hor_order[i]] not in grid[j+1][i+1]:
                        grid[j+1][i+1] = "_"
                    else:
                        keep_letter(alph_order[hor_order[i]], grid[j+1][i+1])
                        break
            #BOTTOM border
            if hor_order[-i-1] != 0:
                for j in range(size):
                    if alph_order[hor_order[-i-1]] not in grid[-j-2][i+1]:
                        grid[-j-2][i+1] = "_"
                    else:
                        keep_letter(alph_order[hor_order[-i-1]], grid[-j-2][i+1])
                        break
            #LEFT border
            if ver_order[i] != 0:
                for j in range(size):
                    if alph_order[ver_order[i]] not in grid[i+1][j+1]:
                        grid[i+1][j+1] = "_"
                    else:
                        keep_letter(alph_order[ver_order[i]], grid[i+1][j+1])
                        break
            #RIGHT border
            if ver_order[-i-1] != 0:
                for j in range(size):
                    if alph_order[ver_order[-i-1]] not in grid[i+1][-j-2]:
                        grid[i+1][-j-2] = "_"
                    else:
                        keep_letter(alph_order[ver_order[-i-1]], grid[i+1][-j-2])
                        break

        #Check if algorithm is stuck
        if is_same_matrix(last_grid, grid):
            same_grid = True

    # print("\nEnd 1st WHILE\n")
    # for i in range(size+2):
    #     print(grid[i])

    #Dominating letters per line
    same_grid = False
    cnt = 0

    #2nd WHILE - Clearing and checking constraints
    while complete_grid != size**2 and same_grid == False:
        #print("\nNEW 2nd WHILE\n")
        for i in range(size):
            for j in range(size):
                if grid[i+1][j+1].count("_") == letters:
                    grid[i+1][j+1] = "_"
                    continue
                if isinstance(grid[i+1][j+1], list):
                    for l in range(letters):
                        if alph_order[l+1] in grid[i+1][j+1]:
                            check_singles(alph_order[l+1], i+1, j+1)

        #Clear lines
        complete_grid = clear_lines()

        #Side constraints check
        side_priority("top")
        side_priority("bottom")
        side_priority("left")
        side_priority("right")

        #Check if algorithm is looping infinitely
        if is_same_matrix(last_grid, grid):
            if cnt == 0:
                same_grid = True
                exit_loop = True
            else:
                same_grid = True
                exit_loop = False

        #Count the loops of 2nd WHILE
        cnt += 1

        # print("\nEnd 2nd WHILE")
        # for t in range(size+2):
        #     print(grid[t])
        # print("\nPrevious grid")
        # for t in range(size+2):
        #     print(last_grid[t])

# R E S U L T - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if same_grid == True and complete_grid != size**2:
        print("\n" + "\x1b[1;33;41m" + " ERROR: infinite loop " + "\x1b[0m")

#Drawing the FINAL grid
print("\n" + "\x1b[1;33;44m" + " FINAL GRID " + "\x1b[0m" + "\n")
for i in range(size+2):
    print(grid[i])
