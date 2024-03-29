
# I N P U T   D A T A - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Has to be False to ask for input (true will run example)
runExample = True

debugPrint = True
complete_grid = 0

if runExample:

    # # Grid 18
    # size = 6
    # hor_order = [5, 2, 2, 4, 3, 1]
    # hor_order_rev = [2, 2, 3, 1, 3, 3]
    # ver_order = [3, 2, 3, 2, 1, 3]
    # ver_order_rev = [1, 3, 2, 3, 2, 2]

    # Grid 19
    size = 6
    hor_order = [2, 1, 3, 4, 2, 3]
    hor_order_rev = [2, 5, 3, 2, 3, 1]
    ver_order = [2, 1, 3, 5, 4, 2]
    ver_order_rev = [3, 5, 2, 2, 3, 1]

    # # Grid 20
    # size = 6
    # hor_order = [2, 1, 5, 2, 4, 2]
    # hor_order_rev = [3, 4, 2, 5, 1, 2]
    # ver_order = [2, 3, 1, 3, 2, 4]
    # ver_order_rev = [3, 3, 3, 1, 3, 2]

    # # Grid 21
    # size = 6
    # hor_order = [2, 2, 1, 3, 5, 4]
    # hor_order_rev = [3, 2, 5, 2, 1, 2]
    # ver_order = [3, 1, 3, 4, 2, 4]
    # ver_order_rev = [4, 4, 3, 1, 2, 2]

    # # Grid 22
    # size = 6
    # hor_order = [2, 3, 4, 3, 2, 1]
    # hor_order_rev = [2, 1, 2, 4, 3, 4]
    # ver_order = [2, 4, 2, 3, 1, 2]
    # ver_order_rev = [1, 2, 2, 4, 3, 4]

    # # Grid 23
    # size = 6
    # hor_order = [0, 3, 1, 0, 4, 4]
    # hor_order_rev = [4, 0, 0, 0, 2, 1]
    # ver_order = [3, 0, 2, 2, 4, 4]
    # ver_order_rev = [3, 0, 2, 3, 2, 1]
else:
    size = int(input("Enter grid SIZE: "))
    hor_order = []
    hor_order_rev = []
    ver_order = []
    ver_order_rev = []

    # User input commands
    print("Enter TOP-border numbers, left to right one at a time (0 if blank): ")
    for i in range(size):    
        hor_order.append(int(input()))
    print("Enter BOTTOM-border numbers, left to right: ")
    for i in range(size):    
        hor_order_rev.append(int(input()))
    print("Enter LEFT-border numbers, top to bottom: ")
    for i in range(size):    
        ver_order.append(int(input()))
    print("Enter RIGHT-border numbers, top to bottom: ")
    for i in range(size):    
        ver_order_rev.append(int(input()))

    # Add numbers in starting grid
    start_numbers = []
    start_array = []
    start_check = str(input("Any number already in the grid? y/n "))
    while start_check != "y" and start_check != "n":
        print("Invalid input: press 'y' if yes, 'n' if not")
        start_check = str(input("Any number already in the grid? y/n "))
    if start_check == "y":
        n_already = int(input("How many numbers already in grid? "))
        for i in range (n_already):
            num = int(input("Enter number: "))
            start_numbers.append(num)
            row = int(input("In which row? "))
            clm = int(input("In which column? "))
            start_array.append([row, clm])

# F U N C T I O N S - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Print grid
def print_grid(message = ""):
    if message != "":
        print(message + "\n")
    for i in range(size+2):
        print(grid[i])
    print("\n")
    return

# Print columns
def print_columns():
    for i in range(size):
        print("\nCOLUMN " + str(1+i) + ": " + str(hor_order[i]) + ", " + str(hor_order_rev[i]))
        for j in range(size):
            print(grid[j+1][i+1])

# Remove number from cell
def remove(number, cell):
    if isinstance(cell, list) and number in cell:
        cell[cell.index(number)] = "_"
    return

# Last number of mixed array
def last_number_in(cell):
    if isinstance(cell, list):
        for i in range(len(cell)):
            if isinstance(cell[-1-i], int):
                return cell[-1-i]
    else:
        print("Not an array")
        return False

# Clear lines
def clear_lines():
    complete_grid = 0
    for i in range(size):
        for j in range(size):
            if isinstance(grid[i+1][j+1], int):
                int_num = grid[i+1][j+1]
                complete_grid += 1
                for k in range(size):
                    if isinstance(grid[k+1][j+1], list) and int_num in grid[k+1][j+1]:
                        remove(int_num, grid[k+1][j+1])
                    if isinstance(grid[i+1][k+1], list) and int_num in grid[i+1][k+1]:
                        remove(int_num, grid[i+1][k+1])
    return complete_grid

# Check for initial min and max side numbers
def initial_constraints():
    for i in range(size):
        if hor_order[i] == size:
            for j in range(size):
                grid[j+1][i+1] = j+1
        elif hor_order[i] == 1:
            grid[1][i+1] = size
        else:
            # Depth removal
            for j in range(hor_order[i] - 1):      # Loop for cell
                for k in range(size):   # Loop for numbers to remove
                    if not hor_order[i] > k + (j + 1):
                        break
                    remove(size-k, grid[j+1][i+1])
        # print_grid("Part 1")
        if hor_order_rev[i] == size:
            for j in range(size):
                grid[-j-2][i+1] = j+1
        elif hor_order_rev[i] == 1:
            grid[-2][i+1] = size
        else:
            for j in range(hor_order_rev[i] - 1):
                for k in range(size):   # Loop for numbers to remove
                    if not hor_order_rev[i] > k + (j+1):
                        break
                    remove(size-k, grid[-j-2][i+1])
        # print_grid("Part 2")
        if ver_order[i] == size:
            for j in range(size):
                grid[i+1][j+1] = j+1
        elif ver_order[i] == 1:
            grid[i+1][1] = size
        else:
            for j in range(ver_order[i] - 1):
                for k in range(size):   # Loop for numbers to remove
                    if not ver_order[i] > k + (j+1):
                        break
                    remove(size-k, grid[i+1][j+1])
        # print_grid("Part 3")
        if ver_order_rev[i] == size:
            for j in range(size):
                grid[i+1][-j-2] = j+1 
        elif ver_order_rev[i] == 1:
            grid[i+1][-2] = size
        else:
            for j in range(ver_order_rev[i] - 1):
                for k in range(size):   # Loop for numbers to remove
                    if not ver_order_rev[i] > k + (j+1):
                        break
                    remove(size-k, grid[i+1][-j-2])
        # print_grid("Part 4")
    return

# Check and confirm single numbers
def check_singles(number, x, y):
    appears_once_horiz = False
    appears_once_vert = False
    switch_hor = False
    switch_ver = False

    for i in range(size):
        #Only one in line?
        if isinstance(grid[x][i+1], int) and number == grid[x][i+1]:
            appears_once_horiz = False
            switch_hor = True
        elif isinstance(grid[x][i+1], list) and number in grid[x][i+1]:
            if appears_once_horiz == False and switch_hor == False:
                appears_once_horiz = True
            else:
                appears_once_horiz = False
                switch_hor = True    
        #Only one in column?
        if isinstance(grid[i+1][y], int) and number == grid[i+1][y]:    # If number already in line
            appears_once_vert = False
            switch_ver = True
        elif isinstance(grid[i+1][y], list) and number in grid[i+1][y]:
            if appears_once_vert == False and switch_ver == False:
                appears_once_vert = True
            else:
                appears_once_vert = False
                switch_ver = True
    
    #Confirm single numbers
    if appears_once_horiz == True or appears_once_vert == True:
        grid[x][y] = number
        clear_lines()
        return True
    else:
        return False

# Automatically check whole grid for single letters
def ultimate_check_singles():
    changes_check = True
    while changes_check:
        changes_check = False
        for i in range(size):
            for j in range(size):
                for num in range(size):
                    if isinstance(grid[i+1][j+1], list) and num+1 in grid[i+1][j+1]:
                        # check_singles(num+1, i+1, j+1)
                        if changes_check == False:
                            changes_check = check_singles(num+1, i+1, j+1)
                        else:
                            check_singles(num+1, i+1, j+1)

# Copy and check if matrix did (not) change after 1 loop
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

# Count skyscrapers and keep track of number seen
def count_skys(side, line):

    in_line = []
    see_line = []
    high_idx = -1
    remain_line = []
    next_empty = 0
    # cnt_empty = 0
    # prev_int = -1
    # visib_empty = 0
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
            # if cell - prev_int > 1:
            #     visib_empty += cnt_empty
            #     cnt_empty = 0
            #     prev_int = cell
        # Keep track of empty cells that could have a visible number placed in it
        # (Only cells that are not in between 2 consecutive numbers before highest number)
        # elif isinstance(cell, list) and size not in in_line:
        #     cnt_empty += 1
        # If I haven't seen any number, it's an empty space
        if in_line == []:
            next_empty += 1
        
        remain_line = [i+1 for i in range(size) if i+1 not in in_line]

    return in_line, see_line, high_idx, remain_line, next_empty

# Adding/removing numbers based on side letters
def side_constraint(side, line):

    in_line, see_line, high_idx, remain_line, next_empty = count_skys(side, line)
    all_empty = size - len(in_line)     # Number of empty cells
    only_small_left = False
    condition_met = False
    diff = abs(len(in_line) - len(see_line))

    if side == "Top":
        row_before = high_idx-1
        row_first = 1
        column_before = column_first = line+1
        row_mult = 1
        col_mult = 0
        side_number = hor_order[line]
        opposite_number = hor_order_rev[line]
    elif side == "Bottom":
        row_before = high_idx+1
        row_first = -2
        column_before = column_first = line+1
        row_mult = -1
        col_mult = 0
        side_number = hor_order_rev[line]
        opposite_number = hor_order[line]
    elif side == "Left":
        row_before = row_first = line+1
        column_before = high_idx-1
        column_first = 1
        row_mult = 0
        col_mult = 1
        side_number = ver_order[line]
        opposite_number = ver_order_rev[line]
    elif side == "Right":
        row_before = row_first = line+1
        column_before = high_idx+1
        column_first = -2
        row_mult = 0
        col_mult = -1
        side_number = ver_order_rev[line]
        opposite_number = ver_order[line]

    # Break if no side letter
    if side_number == 0:
        return    

    # Check if missSkr numbers are all smaller than ones in sight
    if all(see_line[0] > n for n in remain_line):
        only_small_left = True
    # Check if side condition is already true
    if side_number == len(see_line):
        condition_met = True
    
    # We see all skyscr and there is no empty space between them
    if condition_met and size - abs(high_idx) == all_empty:
        return

    # If side cond is already met:
    # - Break if all missSkr numbers will get covered anyways
    if condition_met and next_empty == 0 and only_small_left:
        return

    missSkr = side_number - len(see_line)

    # Check if all empty cells have all potentially visible numbers
    visib_empty = 0
    visib_switch = True
    visib_cont = True
    last_idx = 0
    for i in range(size):
        cell = grid[row_first + i*row_mult][column_first + i*col_mult]
        if isinstance(cell, int) and remain_line != []:
            if cell > remain_line[-1]:
                break
            if visib_empty > 0:
                visib_switch = False
        if isinstance(cell, list):
            visib_empty += 1
            last_idx = i+1
            if not visib_switch:
                visib_cont = False

    if size not in in_line:     # When highest number not in line
        if side_number == 2:    # Considering only case for side_number == 2
            if next_empty == 0 and all(grid[row_first][column_first] < n for n in remain_line):
                for i in range(size):
                    if isinstance(grid[row_first + i*row_mult][column_first + i*col_mult], list) and size in grid[row_first + i*row_mult][column_first + i*col_mult]:
                        grid[row_first + i*row_mult][column_first + i*col_mult] = size
                        clear_lines()
                        if debugPrint:
                            print(side+" 0) Added "+str(size)+" in "+str(row_first + i*row_mult)+", "+str(column_first + i*col_mult)+"\n")
                        break
            elif next_empty != 0 and len(in_line) == 0:
                switch01 = False
                for i in range(size): 
                    current_cell = grid[row_first + i*row_mult][column_first + i*col_mult]
                    # Continue if it's the first cell (not needed)
                    if row_first + i*row_mult == row_first and column_first + i*col_mult == column_first:
                        continue
                    # Remove (size-1) if haven't seen size and not first cell
                    if not switch01 and (size-1) in current_cell and size not in current_cell:
                        remove(size-1, grid[row_first + i*row_mult][column_first + i*col_mult])
                        if debugPrint:
                            print(side+" 0.1) Removed "+str(size-1)+" in "+str(row_first + i*row_mult)+", "+str(column_first + i*col_mult)+"\n")
                        ultimate_check_singles()
                    # Break if first cell w/ highest number has no (size-1)
                    if size in current_cell and (size - 1) not in current_cell:
                        break
                    # Change switch if we have both in same cell
                    elif size in current_cell and (size - 1) in current_cell:
                        if not switch01:
                            switch01 = True
                        else:
                            break
                    # Remove if (size-1) in cell w/ size or if we have a 2 also on the other side
                    if (size - 1) in current_cell and switch01 and (size in current_cell or side_number == opposite_number):
                        remove(size-1, grid[row_first + i*row_mult][column_first + i*col_mult])
                        if debugPrint:
                            print(side+" 0.2) Removed "+str(size-1)+" in "+str(row_first + i*row_mult)+", "+str(column_first + i*col_mult)+"\n")
                        ultimate_check_singles()
            if isinstance(grid[row_first + row_mult][column_first + col_mult], list) and size not in grid[row_first + row_mult][column_first + col_mult]:
                cell = grid[row_first][column_first]
                if isinstance(cell, list) and 1 in cell:
                    remove(1, grid[row_first][column_first])
                    if debugPrint:
                        print(side+" 0.3) Removed "+str(1)+" in "+str(row_first)+", "+str(column_first)+"\n")
        return

    # # - If some numbers could still be seen, remove them from sight
    # elif next_empty == 0 and condition_met and not only_small_left and visib_empty > 0:
    #     for i in range(size):
    #         if isinstance(grid[row_first + i*row_mult][column_first + i*col_mult], list):
    #             remove(remain_line[-1], grid[row_first + i*row_mult][column_first + i*col_mult])
    #             # TODO: Fix this constraint
    #             if debugPrint:
    #                 print(side+" 1) Removed "+str(remain_line[-1])+" in "+str(row_first + i*row_mult)+", "+str(column_first + i*col_mult)+"\n")
    #             ultimate_check_singles()
    #             break

    # ALL empty cells are visible
    if next_empty == all_empty > 0:
        # - When missSkr as many skyscr as empty visible cells 
        # or just miss 1 but some skyscr will be covered
        if missSkr == next_empty or (missSkr == 1 and not only_small_left):
            remain_idx = 0
            for i in range(size):
                if isinstance(grid[row_first + i*row_mult][column_first + i*col_mult], list): 
                    grid[row_first + i*row_mult][column_first + i*col_mult] = remain_line[remain_idx]
                    if debugPrint:
                        print(side+" 2.1) Added "+str(remain_line[remain_idx])+" in "+str(row_first + i*row_mult)+", "+str(column_first + i*col_mult)+"\n")
                    remain_idx += 1
                if remain_idx == len(remain_line):
                    break
        # - When missSkr only one skyscr, add to closest
        elif missSkr == 1 and only_small_left:
            grid[row_first][column_first] = remain_line[-1]
            if debugPrint:
                print(side+" 2.2) Added "+str(remain_line[-1])+" in "+str(row_first)+", "+str(column_first)+"\n")
        # Remove 2 when side number is 3 and see only highest number at distance 3
        elif side_number == 3 and next_empty == 3 and len(see_line) == 1 and 2 in grid[row_first + row_mult][column_first + col_mult]:
            remove(2, grid[row_first + row_mult][column_first + col_mult])
            if debugPrint:
                print(side+" 2.3) Removed "+str(2)+" in "+str(row_first + row_mult)+", "+str(column_first + col_mult)+"\n")
            ultimate_check_singles()

    # NOT ALL empty cells are visible
    elif all_empty != next_empty:

        if (missSkr < next_empty and next_empty > 1 and only_small_left) or \
            (missSkr == 1 and next_empty == 0):
            # Before which number we will remove
            before_this_number = size

            # To not see immediately a 1 when missSkr just one skyscr
            if missSkr == 1 and isinstance(grid[row_first][column_first], list):
                # Miss only one, remove more than just 1 (when the first number wouldn't be enough to cover all the next)
                for k in range(size):   # Loop for numbers to remove
                    if not next_empty > k + 1:
                        break
                    cell = grid[row_first][column_first]
                    if isinstance(cell, list) and k+1 in cell:
                        remove(k+1, grid[row_first][column_first])
                        if debugPrint:
                            print(side+" 3.1) Removed "+str(k+1)+" in "+str(row_first)+", "+str(column_first)+"\n")
                ultimate_check_singles()

                # # Remove highest from furthest, not to see one extra number
                # for j in range(size):
                #     if size - j not in in_line:
                #         for k in range(size):
                #             if grid[row_before - (k-1)*row_mult][column_before - (k-1)*col_mult] == before_this_number:
                #                 if visib_empty == 1 and isinstance(grid[row_before - k*row_mult][column_before - k*col_mult], list) and size-j in grid[row_before - k*row_mult][column_before - k*col_mult]:
                #                     # print_grid("CONSTRAINT 3.2")
                #                     grid[row_before - k*row_mult][column_before - k*col_mult] = size - j
                #                     if debugPrint:
                #                         print(side+" 3.2) Added "+str(size - j)+" in "+str(row_before - k*row_mult)+", "+str(column_before - k*col_mult)+"\n")                        
                #                 if visib_empty > 1 and missSkr == 1 and (diff == 0 or (diff > 0 and only_small_left)):
                #                     for l in range(size):
                #                         if not (row_before - (k+l)*row_mult == row_first and column_before - (k+l)*col_mult == column_first):
                #                             cell = grid[row_before - (k+l)*row_mult][column_before - (k+l)*col_mult]
                #                             if isinstance(cell, list) and size - j in cell:
                #                                 print_grid("CONSTRAINT 3.3")
                #                                 remove(size - j, grid[row_before - (k+l)*row_mult][column_before - (k+l)*col_mult])
                #                                 if debugPrint:
                #                                     print(side+" 3.3) Removed "+str(size - j)+" in "+str(row_before - (k+l)*row_mult)+", "+str(column_before - (k+l)*col_mult)+"\n")                        
                #                                 ultimate_check_singles()
                #                             continue
                #                         break
                #                 break
                #         break
                #     else:
                #         if size - j in see_line:
                #             before_this_number = size-j
    
            # Complete if missing as many numbers as empty visible cells
            else:
                # Fill cells if condition is true
                if visib_empty == all_empty or visib_empty == missSkr != 0:
                # if cnt_empty == all_empty or cnt_empty == missSkr:
                    count_up = 0
                    for i in range(last_idx):
                        cell = grid[row_first + i*row_mult][column_first + i*col_mult]
                        if isinstance(cell, list):
                            if missSkr == 1:
                                grid[row_first + i*row_mult][column_first + i*col_mult] = last_number_in(cell)
                                if debugPrint:
                                    print(side+" 3.4) Added "+str(remain_line[-1])+" in "+str(row_first + i*row_mult)+", "+str(column_first + i*col_mult)+"\n")
                                break
                            elif missSkr == all_empty:
                                grid[row_first + i*row_mult][column_first + i*col_mult] = remain_line[count_up]
                                count_up += 1
                                if debugPrint:
                                    print(side+" 3.4) Added "+str(remain_line[count_up])+" in "+str(row_first + i*row_mult)+", "+str(column_first + i*col_mult)+"\n")

        # If side constraint is completed and first cell is filled
        elif missSkr == 0 and next_empty == 0 and visib_empty > 0 and visib_cont:
            for i in range(size):
                cell = grid[row_first + i*row_mult][column_first + i*col_mult]
                if isinstance(cell, list):
                    # Next number we see after first empty cell
                    current_int = see_line[i-1]
                    next_int = see_line[i]
                    for j in range(size):
                        if isinstance(cell[j], int) and current_int < cell[j] < next_int:
                            if debugPrint:
                                print(side+" 3.2) Removed "+str(cell[j])+" in "+str(row_first + i*row_mult)+", "+str(column_first + i*col_mult)+"\n")
                            remove(cell[j], grid[row_first + i*row_mult][column_first + i*col_mult])
                            ultimate_check_singles()

        # Remove numbers that could hide others when we need to see all next empty spaces
        elif missSkr == next_empty and next_empty > 1:
            if only_small_left:
                # Count the numbers that are missing but cannot be placed in next empty cells
                # This gap is considered when removing numbers
                cnt_gap = 0
                for i in range(len(remain_line)):
                    none_in_line = True
                    for j in range(next_empty):
                        if remain_line[-1-i] in grid[row_first + j*row_mult][column_first + j*col_mult]:
                            none_in_line = False
                            break
                        if j+1 == next_empty and none_in_line:
                            cnt_gap += 1
                    if not none_in_line:
                        break

                for i in range(next_empty):
                    cell = grid[row_first + i*row_mult][column_first + i*col_mult]
                    for j in range(next_empty - i - 1):
                        if isinstance(cell, list) and remain_line[-1-j-cnt_gap] in cell:
                            remove(remain_line[-1-j-cnt_gap], cell)
                            if debugPrint:
                                print(side+" 4.1) Removed "+str(remain_line[-1-j-cnt_gap])+" in "+str(row_first+i*row_mult)+", "+str(column_first+i*col_mult)+"\n")
                            ultimate_check_singles()
                
            seenSwitch = False
            for i in range(size):
                # Make sure we are considering the first number we see before removing
                if grid[row_before - i*row_mult][column_before - i*col_mult] == see_line[0]:
                    seenSwitch = True
                # Stop when we get to first cell, only place where it cannot get hidden
                if row_before - (i+1)*row_mult == row_first and column_before - (i+1)*col_mult == column_first:
                    break
                elif seenSwitch:
                    cell = grid[row_before - (i+1)*row_mult][column_before - (i+1)*col_mult]
                    if isinstance(cell, list) and 1 in cell:
                        remove(1, grid[row_before - (i+1)*row_mult][column_before - (i+1)*col_mult])
                        if debugPrint:
                            print(side+" 4.2) Removed "+str(1)+" in "+str(row_before - (i+1)*row_mult)+", "+str(column_before - (i+1)*col_mult)+"\n")
                        ultimate_check_singles()

        # When missing one skyscr and only one number can be placed in first cell
        if next_empty == 1 and missSkr == 1:
            only_one = False
            current_cell = grid[row_first][column_first]
            for i in range(size):
                if isinstance(current_cell, list) and i+1 in current_cell and all(i+1 < n for n in see_line):
                    if not only_one:
                        only_one = True
                        saved_number = i+1
                    else:
                        only_one = False
                        break
            if only_one:
                grid[row_first][column_first] = saved_number
                if debugPrint:
                    print(side+" 4.3) Added "+str(saved_number)+" in "+str(row_first)+", "+str(column_first)+"\n")

    # When I already have skyline, but still have empty cells in sight
    if next_empty > 0 and condition_met:
        grid[row_first][column_first] = remain_line[-1]
        if debugPrint:
            print(side+" 5) Added "+str(remain_line[-1])+" in "+str(row_first)+", "+str(column_first)+"\n")

    # Remove possibility of 1st cell numbers when some high numbers got hidden
    if only_small_left and len(see_line) != len(in_line) and missSkr > 1:
        cell = grid[row_first][column_first]
        if isinstance(cell, list) and remain_line[-1] in cell:
            remove(remain_line[-1], grid[row_first][column_first])
            if debugPrint:
                print(side+" 6) Removed "+str(remain_line[-1])+" in "+str(row_first)+", "+str(column_first)+"\n")
            ultimate_check_singles()

    return

# I N I T I A L I Z E   G R I D - - - - - - - - - - - - - - - - - - - - - - - - - -

grid = []
last_grid = []

# Create the playing grid
for i in range(size+2):
    grid.append([])
    last_grid.append([])
    for j in range(size+2):
        if i != 0 and i != size+1 and j != 0 and j != size+1:
            grid[i].append(0)
            last_grid[i].append(0)
        else:
            grid[i].append(0)
            last_grid[i].append(0)

# Add side letters
for i in range(size):
    grid[0][i+1] = hor_order[i]
    grid[size+1][i+1] = hor_order_rev[i]
    grid[i+1][0] = ver_order[i]
    grid[i+1][size+1] = ver_order_rev[i]

# Add letters already in grid (if any)
if not runExample and start_check == "y":
    for i in range(len(start_numbers)):
        grid[start_array[i][0]][start_array[i][1]] = start_numbers[i]

# Drawing the STARTING grid
print_grid("\n\x1b[1;33;44m" + " STARTING GRID " + "\x1b[0m")

# Fill cells with all-letters array
for i in range(size):
    for j in range(size):
        if size == 4:
            grid[i+1][j+1] = [1, 2, 3, 4]
        if size == 5:
            grid[i+1][j+1] = [1, 2, 3, 4, 5]
        if size == 6:
            grid[i+1][j+1] = [1, 2, 3, 4, 5, 6]

if not runExample and start_check == "y":
    for i in range(len(start_numbers)):
        grid[start_array[i][0]][start_array[i][1]] = start_numbers[i]

# M A I N   A L G O R I T H M - - - - - - - - - - - - - - - - - - - - - - - - - - -

initial_constraints()

# print_grid("End initialization")

same_grid = False

while complete_grid != size**2 and same_grid == False:

    ultimate_check_singles()
    print_grid("New loop")

    for i in range(size):
        side_constraint("Top", i)
        # print_grid("Top " + str(i+1))
        side_constraint("Bottom", i)
        # print_grid("Bottom " + str(i+1))
        side_constraint("Left", i)
        # print_grid("Left " + str(i+1))
        side_constraint("Right", i)
        # print_grid("Right " + str(i+1))

    if is_same_matrix(last_grid, grid):
        same_grid = True

    complete_grid = clear_lines()
    # print_grid("End loop")
    # grid[1][2] = 1

if same_grid:
    print_grid("\x1b[1;33;41m" + " ERROR: infinite loop " + "\x1b[0m")
else:
    # Drawing the FINAL grid
    print_grid("\x1b[1;33;44m" + " FINAL GRID " + "\x1b[0m")

print_columns()