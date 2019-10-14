
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

#Add numbers in starting grid
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

#Print grid
def print_grid():
    for i in range(size+2):
        print(grid[i])
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

#Add letters already in grid (if any)
if start_check == "y":
    for i in range(len(start_numbers)):
        grid[start_array[i][0]][start_array[i][1]] = start_numbers[i]

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

if start_check == "y":
    for i in range(len(start_numbers)):
        grid[start_array[i][0]][start_array[i][1]] = start_numbers[i]

print_grid()