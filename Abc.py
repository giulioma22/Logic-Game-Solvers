import math

#Data of playing grid

size = 5
letters = 3
hor_order = [0, 0, 2, 2, 0]
hor_order_rev = [0, 1, 0, 3, 0]
ver_order = [0, 2, 2, 0, 0]
ver_order_rev = [0, 1, 0, 0, 0]
available_letters = []

# size = 5
# letters = 3
# hor_order = [3, 1, 1, 2, 2]
# hor_order_rev = [2, 2, 2, 3, 1]
# ver_order = [3, 1, 2, 2, 2]
# ver_order_rev = [2, 3, 1, 1, 1]

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
alph_order = ["_", "A", "B", "C", "D", "E"]

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

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 


#Create the playing grid
grid = []
last_grid = []

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

grid = []

for i in range(size+2):
    line = []
    for j in range(size+2):
        if i != 0 and i != size+1 and j != 0 and j != size+1:
            if letters == 3:
                line.append(["A", "B", "C"])
                available_letters = ["A", "B", "C"]
            if letters == 4:
                line.append(["A", "B", "C", "D"])
                available_letters = ["A", "B", "C", "D"]
            if letters == 5:
                line.append(["A", "B", "C", "D", "E"])
                available_letters = ["A", "B", "C", "D", "E"]
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
exit_loop = False
same_grid = False
complete_grid = 0

while exit_loop == False:
    same_grid = False
    while same_grid == False: 
        print("\nNEW 1st CYCLE\n")
        for i in range(size):
            for j in range(letters-1):
                remove(alph_order[hor_order[i]], grid[-j-2][i+1])
                remove(alph_order[hor_order[-i-1]], grid[j+1][i+1])
                remove(alph_order[ver_order[i]], grid[i+1][-j-2])
                remove(alph_order[ver_order[-i-1]], grid[i+1][j+1])
            if hor_order[i] != 0:   #If there is no border letter, we skip
                for j in range(size):
                    # print("BANANA " + str(j+1) + " " + str(i+1) + " " + str(grid[j+1][i+1]))
                    if alph_order[hor_order[i]] not in grid[j+1][i+1]:
                        grid[j+1][i+1] = "_"
                    else:
                        keep_letter(alph_order[hor_order[i]], grid[j+1][i+1])
                        break
            if hor_order[-i-1] != 0:
                for j in range(size):
                    if alph_order[hor_order[-i-1]] not in grid[-j-2][i+1]:
                        grid[-j-2][i+1] = "_"
                    else:
                        keep_letter(alph_order[hor_order[-i-1]], grid[-j-2][i+1])
                        break
            if ver_order[i] != 0:
                for j in range(size):
                    if alph_order[ver_order[i]] not in grid[i+1][j+1]:
                        grid[i+1][j+1] = "_"
                    else:
                        keep_letter(alph_order[ver_order[i]], grid[i+1][j+1])
                        break
            if ver_order[-i-1] != 0:
                for j in range(size):
                    if alph_order[ver_order[-i-1]] not in grid[i+1][-j-2]:
                        grid[i+1][-j-2] = "_"
                    else:
                        keep_letter(alph_order[ver_order[-i-1]], grid[i+1][-j-2])
                        break
        
        for t in range(size+2):
            print(grid[t])
        print("\n")
        for t in range(size+2):
            print(last_grid[t])

        #Check if algorithm is stuck
        if is_same_matrix(last_grid, grid):
            print("\n1st CLOSED - - - - - - - - - - - - -")
            same_grid = True

    print("\n")
    for i in range(size+2):
        print(grid[i])

    #Dominating letters per line
    same_grid = False
    cnt = 0

    while complete_grid != size**2 and same_grid == False:
    # if complete_grid != size**2 and same_grid == False:
        print("\nNEW 2nd CYCLE\n")
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

        #Check if algorithm is stuck
        if is_same_matrix(last_grid, grid):
            print("2nd CLOSED - - - - - - - - - - - - -\n")
            if cnt == 0:
                same_grid = True
                exit_loop = True
            else:
                same_grid = True
                exit_loop = False

        #Count the loops of 2nd WHILE
        cnt += 1

        for t in range(size+2):
            print(grid[t])
        # print("\n")
        # for t in range(size+2):
        #     print(last_grid[t])

        # if same_grid:
        #     grid[3][3] = "B"
        #     same_grid = False

# - - - - End of WHILE - - - - - 

if same_grid == True:
        print("\n" + "\x1b[1;33;41m" + " ERROR: infinite loop " + "\x1b[0m")

#Drawing the FINAL grid
print("\n" + "\x1b[1;33;44m" + " FINAL GRID " + "\x1b[0m" + "\n")
for i in range(size+2):
    print(grid[i])
