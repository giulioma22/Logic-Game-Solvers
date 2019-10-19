
# I N P U T   D A T A - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

size = 4
hor_order = [3, 2, 2, 1]
hor_order_rev = [1, 3, 2, 2]
ver_order = [4, 2, 3, 1]
ver_order_rev = [1, 2, 2, 2]

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
def print_grid():
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
        return
    else:
        return False

#Count skyscrapers and keep track of number seen
def count_skys(side, line):
    in_line = []
    hidden = []
    cell = 0
    for i in range(size):
        if side == "Top":
            cell = grid[i+1][line+1]
        elif side == "Bottom":
            cell = grid[-i-2][line+1]
        elif side == "Left":
            cell = grid[line+1][i+1]
        elif side == "Right":
            cell = grid[line+1][-i-2]

        if isinstance(cell, int):
            if cell > in_line[-1]:
                in_line.append(cell)
            else:
                hidden.append(cell)
    return [in_line, hidden]

def side_constraint(side, line):
    cell = 0
    order = []
    for i in range(size):
        if side == "Top":
            cell = grid[i+1][line+1]
            order = hor_order
        elif side == "Bottom":
            cell = grid[-i-2][line+1]
            order = hor_order_rev
        elif side == "Left":
            cell = grid[line+1][i+1]
            order = ver_order
        elif side == "Right":
            cell = grid[line+1][-i-2]
            order = ver_order_rev
        
        # if cell count_skys(side, line)

    return

# I N I T I A L I Z E   G R I D - - - - - - - - - - - - - - - - - - - - - - - - - -

grid = []

#Create the playing grid
for i in range(size+2):
    grid.append([])
    for j in range(size+2):
        if i != 0 and i != size+1 and j != 0 and j != size+1:
            grid[i].append("_")
        else:
            grid[i].append("/")

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
print("\n" + "\x1b[1;33;44m" + " STARTING GRID "  + "\x1b[0m" + "\n")
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
    if hor_order_rev[i] == size:
        for j in range(size):
            grid[-j-2][i+1] = j+1
    elif hor_order_rev[i] == 1:
        grid[-2][i+1] = size
    else:
        for j in range(hor_order_rev[i] - 1):
            remove(size, grid[-j-2][i+1])
    if ver_order[i] == size:
        for j in range(size):
            grid[i+1][j+1] = j+1
    elif ver_order[i] == 1:
        grid[i+1][1] = size
    else:
        for j in range(ver_order[i] - 1):
            remove(size, grid[i+1][j+1])
    if ver_order_rev[i] == size:
        for j in range(size):
            grid[i+1][-j-2] = j+1 
    elif ver_order_rev[i] == 1:
        grid[i+1][-2] = size
    else:
        for j in range(ver_order_rev[i] - 1):
            remove(size, grid[i+1][-j-2])

print_grid()

clear_lines()

print_grid()

for i in range(size):
    for j in range(size):
        if isinstance(grid[i+1][j+1], list):
            for num in range(size):
                if isinstance(grid[i+1][j+1], list) and num+1 in grid[i+1][j+1]:
                    check_singles(num+1, i+1, j+1)

print_grid()



