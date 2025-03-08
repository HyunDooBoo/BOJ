import sys

input = sys.stdin.readline

def check():
    for pos in t_pos:
        x, y = pos
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            while 0 <= nx < N and 0 <= ny < N and board[nx][ny] != 'O':
                if board[nx][ny] == 'S':
                    return 0
                else:
                    nx += dx[i]
                    ny += dy[i]
    return 1

def dfs(count):
    global switch

    if switch == 1:
        return

    if count == 3:
        switch = check()
        return

    for i in range(N):
        for j in range(N):
            if board[i][j] == 'X':
                board[i][j] = 'O'
                dfs(count+1)
                board[i][j] = 'X'

N = int(input().rstrip())
board = [list(map(str, input().rstrip().split())) for i in range(N)]
dx, dy = [1,-1,0,0], [0,0,1,-1]
switch = 0
t_pos = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 'T':
            t_pos.append((i, j))

dfs(0)
if switch:
    print("YES")
else:
    print("NO")