
# I N P U T   D A T A - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

size = 4
hor_order = [3, 1, 2, 2]
hor_order_rev = [2, 3, 3, 1]
ver_order = [2, 3, 1, 2]
ver_order_rev = [2, 2, 3, 1]

complete_grid = 0

# size = int(input("Enter grid SIZE: "))
# hor_order = []
# hor_order_rev = []
# ver_order = []
# ver_order_rev = []

# #User input commands
# print("Enter TOP-border numbers, left to right one at a time (0 if blank): ")
# for i in range(size):    
#     hor_order.append(int(input()))
# print("Enter BOTTOM-border numbers, left to right: ")
# for i in range(size):    
#     hor_order_rev.append(int(input()))
# print("Enter LEFT-border numbers, top to bottom: ")
# for i in range(size):    
#     ver_order.append(int(input()))
# print("Enter RIGHT-border numbers, top to bottom: ")
# for i in range(size):    
#     ver_order_rev.append(int(input()))

# #Add numbers in starting grid
# start_numbers = []
# start_array = []
# start_check = str(input("Any number already in the grid? y/n "))
# while start_check != "y" and start_check != "n":
#     print("Invalid input: press 'y' if yes, 'n' if not")
#     start_check = str(input("Any number already in the grid? y/n "))
# if start_check == "y":
#     n_already = int(input("How many numbers already in grid? "))
#     for i in range (n_already):
#         num = int(input("Enter number: "))
#         start_numbers.append(num)
#         row = int(input("In which row? "))
#         clm = int(input("In which column? "))
#         start_array.append([row, clm])

# F U N C T I O N S - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#Print grid
def print_grid(message = ""):
    if message != "":
        print(message + "\n")
    for i in range(size+2):
        print(grid[i])
    print("\n")
    return

#Remove number from cell
def remove(number, cell):
    if isinstance(cell, list) and number in cell:
        cell[cell.index(number)] = "_"
    return

#Clear lines
def clear_lines():
    complete_grid = 0
    for i in range(size):
        for j in range(size):
            if isinstance(grid[i+1][j+1], int):
                complete_grid += 1
                for k in range(size):
                    if isinstance(grid[k+1][j+1], list) and grid[i+1][j+1] in grid[k+1][j+1]:
                        remove(grid[i+1][j+1], grid[k+1][j+1])
                    if isinstance(grid[i+1][k+1], list) and grid[i+1][j+1] in grid[i+1][k+1]:
                        remove(grid[i+1][j+1], grid[i+1][k+1])
    return complete_grid

#Check and confirm single numbers
def check_singles(number, x, y):
    appears_once_horiz = False
    appears_once_vert = False
    switch_hor = False
    switch_ver = False

    for i in range(size):
        #Only one in line?
        if isinstance(grid[x][i+1], list) and number in grid[x][i+1]:
            if appears_once_horiz == False and switch_hor == False:
                appears_once_horiz = True
            else:
                appears_once_horiz = False
                switch_hor = True    
        #Only one in column?
        if isinstance(grid[i+1][y], list) and number in grid[i+1][y]:
            if appears_once_vert == False and switch_ver == False:
                appears_once_vert = True
            else:
                appears_once_vert = False
                switch_ver = True
    
    #Confirm single numbers
    if appears_once_horiz == True or appears_once_vert == True:
        grid[x][y] = number
        clear_lines()
        return
    else:
        return False

def ultimate_check_singles():
    for i in range(size):
        for j in range(size):
            for num in range(size):
                if isinstance(grid[i+1][j+1], list) and num+1 in grid[i+1][j+1]:
                    check_singles(num+1, i+1, j+1)
    return

#Copy and check if matrix did (not) change after 1 loop
def is_same_matrix(grid_1, grid_2):
    same_matrix = True
    for i in range(size):
        for j in range(size):
            if type(grid_1[i+1][j+1]) == type(grid_2[i+1][j+1]):
                if isinstance(grid_1[i+1][j+1], list):
                    for k in range(size):
                        if grid_1[i+1][j+1][k] != grid_2[i+1][j+1][k]:
                            grid_1[i+1][j+1][k] = grid_2[i+1][j+1][k]
                            same_matrix = False
                else:
                    if grid_1[i+1][j+1] != grid_2[i+1][j+1]:
                        grid_1[i+1][j+1] = grid_2[i+1][j+1]
                        same_matrix = False
            else:
                same_matrix = False
                if isinstance(grid_2[i+1][j+1], list):
                    grid_1[i+1][j+1] = []
                    for k in range(size):
                        grid_1[i+1][j+1].append(grid_2[i+1][j+1][k])
                else:
                    grid_1[i+1][j+1] = grid_2[i+1][j+1]
    return same_matrix

#Count skyscrapers and keep track of number seen
def count_skys(side, line):
    in_line = []
    see_line = []
    high_idx = -1
    remain_line = []
    next_empty = 0
    for i in range(size):
        if side == "Top":
            idx = i+1
            cell = grid[idx][line+1]
        elif side == "Bottom":
            idx = -i-2
            cell = grid[idx][line+1]
        elif side == "Left":
            idx = i+1
            cell = grid[line+1][idx]
        elif side == "Right":
            idx = -i-2
            cell = grid[line+1][idx]

        if isinstance(cell, int):
            in_line.append(cell)
            if see_line == [] or cell > see_line[-1]:
                see_line.append(cell)
                if cell == size:
                    high_idx = idx
        if in_line == []:   # If I haven't seen any number, it's an empty space
            next_empty += 1
        
        remain_line = [i+1 for i in range(size) if i+1 not in in_line]

    return in_line, see_line, high_idx, remain_line, next_empty

def side_constraint(side, line):
    
    for i in range(size):

        in_line, see_line, high_idx, remain_line, next_empty = count_skys(side, line)
        all_empty = size - len(in_line)     # Number of empty cells

        if high_idx == -1:     # For now, break if highest number not in line
            break

        if side == "Top":
            row = high_idx-i-1
            column = line+1
            side_letter = hor_order[line]
        elif side == "Bottom":
            row = high_idx+i+1
            column = line+1
            side_letter = hor_order_rev[line]
        elif side == "Left":
            row = line+1
            column = high_idx-i-1
            side_letter = ver_order[line]
        elif side == "Right":
            row = line+1
            column = high_idx+i+1
            side_letter = ver_order_rev[line]

        if len(see_line) == side_letter:     # If side cond is already met, break
            break

        if high_idx != -1 and all_empty >= side_letter:  # Highest number in line          
            for j in range(size):    # Missing numbers in line
                if size - j not in in_line:
                    remove(size - j, grid[row][column])
                    ultimate_check_singles()
                    return
        # elif next_empty == all_empty:
        #     if side_letter > 
        else:
            break
        
        #N.B. If the sum of 2 opposite numbers is size+1, highest number
        #is at distance side_number from that side
        #Pseudo-code
        # if count_skys == side_number:
        #     skip

        # if highest_number in line and gap >= side_number:
        #     for j in range(size):
        #         if size-j not in line:
        #             if size-j == size - 1:

        # if gap == side_number-1 on both sides:
        #     skip

        # # #

    return

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

#Add side letters
for i in range(size):
    grid[0][i+1] = hor_order[i]
    grid[size+1][i+1] = hor_order_rev[i]
    grid[i+1][0] = ver_order[i]
    grid[i+1][size+1] = ver_order_rev[i]

# #Add letters already in grid (if any)
# if start_check == "y":
#     for i in range(len(start_numbers)):
#         grid[start_array[i][0]][start_array[i][1]] = start_numbers[i]

#Drawing the STARTING grid
print("\n\x1b[1;33;44m" + " STARTING GRID " + "\x1b[0m\n")
print_grid()

#Fill cells with all-letters array
for i in range(size):
    for j in range(size):
        if size == 4:
            grid[i+1][j+1] = [1, 2, 3, 4]
        if size == 5:
            grid[i+1][j+1] = [1, 2, 3, 4, 5]
        if size == 6:
            grid[i+1][j+1] = [1, 2, 3, 4, 5, 6]

# if start_check == "y":
#     for i in range(len(start_numbers)):
#         grid[start_array[i][0]][start_array[i][1]] = start_numbers[i]

# M A I N   A L G O R I T H M - - - - - - - - - - - - - - - - - - - - - - - - - - -

#Check for min and max side numbers
for i in range(size):
    if hor_order[i] == size:
        for j in range(size):
            grid[j+1][i+1] = j+1
    elif hor_order[i] == 1:
        grid[1][i+1] = size
    else:
        for j in range(hor_order[i] - 1):
            remove(size, grid[j+1][i+1])
        if hor_order[i] == size-1:
            remove(size-1, grid[1][i+1])
    if hor_order_rev[i] == size:
        for j in range(size):
            grid[-j-2][i+1] = j+1
    elif hor_order_rev[i] == 1:
        grid[-2][i+1] = size
    else:
        for j in range(hor_order_rev[i] - 1):
            remove(size, grid[-j-2][i+1])
        if hor_order_rev[i] == size-1:
            remove(size-1, grid[-2][i+1])
    if ver_order[i] == size:
        for j in range(size):
            grid[i+1][j+1] = j+1
    elif ver_order[i] == 1:
        grid[i+1][1] = size
    else:
        for j in range(ver_order[i] - 1):
            remove(size, grid[i+1][j+1])
        if ver_order[i] == size-1:
            remove(size-1, grid[i+1][1])
    if ver_order_rev[i] == size:
        for j in range(size):
            grid[i+1][-j-2] = j+1 
    elif ver_order_rev[i] == 1:
        grid[i+1][-2] = size
    else:
        for j in range(ver_order_rev[i] - 1):
            remove(size, grid[i+1][-j-2])
        if ver_order_rev[i] == size-1:
            remove(size-1, grid[i+1][-2])

# print_grid("End initialization")

same_grid = False

while complete_grid != size**2 and same_grid == False:
   
    ultimate_check_singles()
    # print_grid("New loop")

    for i in range(size):
        side_constraint("Top", i)
        side_constraint("Bottom", i)
        side_constraint("Left", i)
        side_constraint("Right", i)

    if is_same_matrix(last_grid, grid):
        same_grid = True

    complete_grid = clear_lines()
    # print_grid("End loop")

if same_grid:
    print("\n\x1b[1;33;41m" + " ERROR: infinite loop " + "\x1b[0m\n")
else:
    #Drawing the FINAL grid
    print("\n\x1b[1;33;44m" + " FINAL GRID " + "\x1b[0m\n")
print_grid()
