M = 9 
def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j],end = " ")
        print()
def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
             
    for x in range(9):
        if grid[x][col] == num:
            return False
 
 
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
def Suduko(grid, row, col):
 
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
     
        if solve(grid, row, col, num):
         
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False
 
'''0 means the cells where no value is assigned'''
print("Welcome to Sudoku solver! Provide the sudoku matrix ")
grid =[]
for i in range(9):
    while (1):
        print ("Enter the", i+1,"the row ")
        row = input()
        row_str = row.split()
        int_l = [int(i) for i in row_str]
        if len(int_l) != 9:
            print("Invalid input")
        else :
           grid.append(int_l)
           break 

print("")
if (Suduko(grid, 0, 0)):
    print("Valid soltution exists :) !")
    puzzle(grid)
else:
    print("Solution does not exist:(")
