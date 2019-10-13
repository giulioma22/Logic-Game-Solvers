
# I N P U T   D A T A - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

alph_order = ["_", "A", "B", "C", "D", "E", "F", "G"]

# # Puzzle 30
# size = 6
# letters = 4
# hor_order = [3, 0, 0, 4, 0, 1]
# hor_order_rev = [0, 1, 4, 2, 0, 3]
# ver_order = [0, 0, 4, 4, 4, 1]
# ver_order_rev = [0, 0, 1, 0, 2, 3]

# # Puzzle 40
# size = 7
# letters = 5
# hor_order = [5, 3, 3, 2, 0, 4, 0]
# hor_order_rev = [0, 4, 4, 5, 3, 2, 5]
# ver_order = [0, 0, 0, 1, 5, 2, 0]
# ver_order_rev = [0, 1, 5, 2, 0, 4, 0]

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

#Add letters in starting grid
start_letters = []
start_array = []
start_check = str(input("Any letter already in the grid? y/n "))
while start_check != "y" and start_check != "n":
    print("Invalid input: press 'y' if yes, 'n' if not")
    start_check = str(input("Any letter already in the grid? y/n "))
if start_check == "y":
    n_already = int(input("How many letters already in grid? "))
    for i in range (n_already):
        let = int(input("Enter letter (1 = A, 2 = B, ...): "))
        start_letters.append(alph_order[let])
        row = int(input("In which row? "))
        clm = int(input("In which column? "))
        start_array.append([row, clm])

#Ordering arrays
for i in range(size):
    hor_order.append(hor_order_rev[-i-1])
    ver_order.append(ver_order_rev[-i-1])


lower_limit = size - (letters - 1)
guess_try = 0
guess_array_1 = [0, 0]
guess_array_2 = [0, 0]
guess_loop = 1
loop_1_over = False
first_guess_1 = True
first_guess_2 = True


# F U N C T I O N S - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#Print grid
def print_grid():
    for i in range(size+2):
        print(grid[i])
    return

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

#Detect single letter in cell
def only_in_cell(cell):
    only_letter = ""
    if isinstance(cell, str):
        return ""
    for i in range(len(cell)):
        if cell[i] != "_":
            if only_letter == "":
                only_letter = cell[i]
            else:
                return ""
    return only_letter

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
                cell_0 = j+1
                cell_1 = i+1
                side_letter = alph_order[hor_order[i]]
            elif grid_side == "bottom":
                cell_0 = -j-2
                cell_1 = i+1
                side_letter = alph_order[hor_order[-i-1]]
            elif grid_side == "left":
                cell_0 = i+1
                cell_1 = j+1
                side_letter = alph_order[ver_order[i]]
            elif grid_side == "right":
                cell_0 = i+1
                cell_1 = -j-2
                side_letter = alph_order[ver_order[-i-1]] 
            if side_letter != "_":
                if side_letter in grid[cell_0][cell_1]:
                    if switch_encount == 0:
                        first_cell = [cell_0, cell_1]
                    switch_encount += 1
                    if side_letter == grid[cell_0][cell_1]:
                        break
                else:
                    if switch_encount == 0:
                        grid[cell_0][cell_1] = "_"
                    if isinstance(grid[cell_0][cell_1], str) and grid[cell_0][cell_1] != "_" and switch_encount == 1:
                        grid[first_cell[0]][first_cell[1]] = side_letter
                        break
    return

#Copy and check if matrix did (not) change after 1 loop
def is_same_matrix(grid_1, grid_2):
    same_matrix = True
    for i in range(size):
        for j in range(size):
            if len(grid_1[i+1][j+1]) == len(grid_2[i+1][j+1]):
                if isinstance(grid_1[i+1][j+1], list):
                    for k in range(letters):
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
                    for k in range(letters):
                        grid_1[i+1][j+1].append(grid_2[i+1][j+1][k])
                else:
                    grid_1[i+1][j+1] = grid_2[i+1][j+1]
    return same_matrix

#Check if line has equal free spots and missing letters
def min_spaces_left():
    for i in range(size):
        n_empty_hor = 0
        n_letters_hor = 0
        n_empty_ver = 0
        n_letters_ver = 0
        for j in range(size):
            if isinstance(grid[i+1][j+1], str):
                if grid[i+1][j+1] == "_":
                    n_empty_hor += 1
                else:
                    n_letters_hor += 1
            if isinstance(grid[j+1][i+1], str):
                if grid[j+1][i+1] == "_":
                    n_empty_ver += 1
                else:
                    n_letters_ver += 1
        if n_empty_hor == size - letters:
            for k in range(size):
                if isinstance(grid[i+1][k+1], list) and only_in_cell(grid[i+1][k+1]) != "":
                    grid[i+1][k+1] = only_in_cell(grid[i+1][k+1])
        if n_empty_ver == size - letters:
            for k in range(size):
                if isinstance(grid[k+1][i+1], list) and only_in_cell(grid[k+1][i+1]) != "":
                    grid[k+1][i+1] = only_in_cell(grid[k+1][i+1])
    return

#Guess new letters
def guess():     #guess_array: 1st is idx letter, 2nd is side
    global exit_loop
    global guess_loop
    global loop_1_over
    global guess_array_1
    global guess_array_2
    global first_guess_1
    global first_guess_2
    
    guess_array = []
    keep_guessing = True

    while keep_guessing == True:

        if guess_loop == 1:
            guess_array = guess_array_1
        elif guess_loop == 2:
            guess_array = guess_array_2
        
        if guess_array[0] >= size:  #Check if line all read
            if guess_array[1] < 3:
                guess_array[0] = 0
                guess_array[1] += 1
            else:
                if guess_loop == 1:
                    if loop_1_over == False:
                        loop_1_over = True
                        print("\n > > > > > > INCREASING DEPTH to LEVEL 2 < < < < < <\n")
                        guess_array_1 = [0, 0]
                        continue
                    else:
                        exit_loop = True    #How to exit loop w/ error
                        return
                elif guess_loop == 2:
                    guess_array_2 = [0, 0]
                    guess_loop = 1
                    guess_array = guess_array_1
                    first_guess_2 = True
                    print("\nGoing back to 1st guess loop < < < < < < <\n")
                    is_same_matrix(grid, saved_matrix)
                    continue

        print("Guess array " + str(guess_array) + " - Guess loop " + str(guess_loop))

        for i in range(size):
            if guess_array[1] == 0:
                guess_letter = alph_order[hor_order[guess_array[0]]]
                print_side = "top"
                cell_0 = -i-2
                cell_1 = guess_array[0]+1
            elif guess_array[1] == 1:
                guess_letter = alph_order[hor_order_rev[guess_array[0]]]
                print_side = "bottom"
                cell_0 = i+1
                cell_1 = guess_array[0]+1
            elif guess_array[1] == 2:
                guess_letter = alph_order[ver_order[guess_array[0]]]
                print_side = "left"
                cell_0 = guess_array[0]+1
                cell_1 = -i-2
            elif guess_array[1] == 3:
                guess_letter = alph_order[ver_order_rev[guess_array[0]]]
                print_side = "right"
                cell_0 = guess_array[0]+1
                cell_1 = i+1
            if guess_letter != "_":
                if guess_letter in grid[cell_0][cell_1] and isinstance(grid[cell_0][cell_1], list):
                    grid[cell_0][cell_1] = guess_letter
                    print("\n Level " + str(guess_loop) + " - Letter " + str(guess_letter) + "(" + print_side + ") in [" + str(cell_0) + ", " + str(cell_1) + "]\n")
                    if guess_loop == 1 and loop_1_over:
                        print("\n Saving grid 2.2... " + str(guess_array_2[0]) + "\n")
                        print_grid()
                        is_same_matrix(saved_matrix_2, grid)
                        # complete_grid = clear_lines()
                        guess_loop = 2
                        first_guess_2 = False
                    else:
                        keep_guessing = False
                    break
        guess_array[0] += 1
    return

#Last check for all letters in rows and columns
def ultimate_check():
    for i in range(size):
        hor_letters = 0
        ver_letters = 0
        for j in range(size):
            if grid[i+1][j+1] != "_":
                hor_letters += 1
            if grid[j+1][i+1] != "_":
                ver_letters += 1
        if hor_letters == letters and ver_letters == letters:
            continue
        else:
            return False
    return


# I N I T I A L I Z E   G R I D - - - - - - - - - - - - - - - - - - - - - - - - - -

grid = []
last_grid = []
saved_matrix = []
saved_matrix_2 = []

#Create the playing grid
for i in range(size+2):
    grid.append([])
    last_grid.append([])
    saved_matrix.append([])
    saved_matrix_2.append([])
    for j in range(size+2):
        if i != 0 and i != size+1 and j != 0 and j != size+1:
            grid[i].append("_")
            last_grid[i].append("_")
            saved_matrix[i].append("_")
            saved_matrix_2[i].append("_")
        else:
            grid[i].append("/")
            last_grid[i].append("/")
            saved_matrix[i].append("/")
            saved_matrix_2[i].append("/")

#Add side letters
for i in range(size):
    grid[0][i+1] = alph_order[hor_order[i]]
    grid[size+1][i+1] = alph_order[hor_order[-i-1]]
    grid[i+1][0] = alph_order[ver_order[i]]
    grid[i+1][size+1] = alph_order[ver_order[-i-1]]

#Add letters already in grid (if any)
if start_check == "y":
    for i in range(len(start_letters)):
        grid[start_array[i][0]][start_array[i][1]] = start_letters[i]

#Drawing the STARTING grid
print("\n" + "\x1b[1;33;44m" + " STARTING GRID "  + "\x1b[0m" + "\n")
print_grid()

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
        if letters == 7:
            grid[i+1][j+1] = ["A", "B", "C", "D", "E", "F", "G"]

if start_check == "y":
    for i in range(len(start_letters)):
        grid[start_array[i][0]][start_array[i][1]] = start_letters[i]


# M A I N   A L G O R I T H M - - - - - - - - - - - - - - - - - - - - - - - - - - -

exit_loop = False
same_grid = False
complete_grid = 0
offset = 1
guess_try = False

while complete_grid != size**2 and exit_loop == False:
    same_grid = False
    guess_try = False

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
    # print_grid()

    same_grid = False
    cnt = 0

    #2nd WHILE - Clearing and checking constraints
    while complete_grid != size**2 and same_grid == False:
        # print("\nNEW 2nd WHILE\n")
        for i in range(size):
            for j in range(size):
                if grid[i+1][j+1].count("_") == letters:
                    grid[i+1][j+1] = "_"
                    continue
                if isinstance(grid[i+1][j+1], list):
                    for l in range(letters):
                        if alph_order[l+1] in grid[i+1][j+1]:
                            check_singles(alph_order[l+1], i+1, j+1)

        #Side constraints check
        side_priority("top")
        side_priority("bottom")
        side_priority("left")
        side_priority("right")

        #Clear lines
        complete_grid = clear_lines()

        #Check if minimum ammount of spaces left
        min_spaces_left()
        complete_grid = clear_lines()

        #Check if algorithm is looping infinitely
        if is_same_matrix(last_grid, grid) and complete_grid != size**2:
            same_grid = True
            if cnt == 0:    #If didn't change 1st try, means it will loop
                guess_try = True
                #exit_loop = True
                if not first_guess_1 and guess_loop == 1:
                    print(" ERROR 1.1: Restoring grid... \n")
                    is_same_matrix(grid, saved_matrix)
                elif not first_guess_2 and guess_loop == 2:
                    print(" ERROR 2.1: Restoring grid... \n")
                    is_same_matrix(grid, saved_matrix_2)
                complete_grid = clear_lines()

        #Count the loops of 2nd WHILE (iterations)
        cnt += 1

        #If grid complete but incorrect, continue guessing
        if complete_grid == size**2 and ultimate_check() == False:
            guess_try = True
            # exit_loop = True
            if guess_loop == 1 and not first_guess_1:
                print(" ERROR 1.2: Restoring grid... \n")
                is_same_matrix(grid, saved_matrix)
            elif guess_loop == 2 and not first_guess_2:
                print(" ERROR 2.2: Restoring grid... \n")
                is_same_matrix(grid, saved_matrix_2)
            complete_grid = clear_lines()
            break
            # print_grid()
            
    #If not logically solvable, try most plausible guesses
    if guess_try == True:
        if guess_loop == 1 and first_guess_1:
            print("\n Saving grid 1... \n")
            print_grid()
            is_same_matrix(saved_matrix, grid)
            first_guess_1 = False
        elif guess_loop == 2  and first_guess_2:
            print("\n Saving grid 2... \n")
            print_grid()
            is_same_matrix(saved_matrix_2, grid)
            first_guess_2 = False

        print("\n" + "\x1b[3m" + " Trying probable combination... " + "\x1b[0m")
        
        # > > > > > GUESS < < < < < < 
        guess()
            


# R E S U L T - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if exit_loop == True and complete_grid != size**2:
        print("\n" + "\x1b[1;33;41m" + " ERROR: infinite loop " + "\x1b[0m")

#Drawing the FINAL grid
print("\n" + "\x1b[1;33;44m" + " FINAL GRID " + "\x1b[0m" + "\n")
print_grid()
