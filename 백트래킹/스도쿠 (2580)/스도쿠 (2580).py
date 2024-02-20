import sys

input = sys.stdin.readline

def row_find(num, row):
    for i in range(9):
        if num == sudoku[row][i]:
            return False
    return True

def col_find(num, col):
    for i in range(9):
        if num == sudoku[i][col]:
            return False
    return True

def square_find(x ,y, n):
    for i in range(3):
        for j in range(3):
            if sudoku[x//3*3+i][y//3*3+j] == n:
                return False
    return True

def dfs(depth):
    if depth == len(zero_list):
        for i in range(9):
            print(' '.join(map(str,sudoku[i])))
        exit()

    for i in range(1, 10):
        x = zero_list[depth][0]
        y = zero_list[depth][1]
        if row_find(i, x) and col_find(i, y) and square_find(x, y, i):
            sudoku[x][y] = i
            dfs(depth + 1)
            sudoku[x][y] = 0

sudoku = []
zero_list = []
for i in range(9):
    sudoku.append(list(map(int, input().rstrip().split())))

for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zero_list.append([i,j])

dfs(0)