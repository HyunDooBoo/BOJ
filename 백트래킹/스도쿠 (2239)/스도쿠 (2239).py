import sys

input = sys.stdin.readline

def chk_row(x,num):
    for i in range(9):
        if num == sudoku[x][i]:
            return False
    return True

def chk_col(y,num):
    for i in range(9):
        if num == sudoku[i][y]:
            return False
    return True

def chk_square(x,y,num):
    for i in range(3):
        for j in range(3):
            if sudoku[x//3*3+i][y//3*3+j] == num:
                return False
    return True

def dfs(depth):
    if depth == len(zero):
        for i in range(9):
            print(''.join(map(str,sudoku[i])))
        exit()
    
    for i in range(1,10):
        x, y = zero[depth][0], zero[depth][1]
        if chk_col(y,i) and chk_row(x,i) and chk_square(x,y,i):
            sudoku[x][y] = i
            dfs(depth+1)
            sudoku[x][y] = 0

sudoku = []
zero = []

for i in range(9):
    sudoku.append(list(map(int, input().rstrip())))

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zero.append((i,j))
dfs(0)