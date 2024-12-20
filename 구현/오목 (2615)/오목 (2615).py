import sys

input = sys.stdin.readline

board = [list(map(int, input().rstrip().split())) for i in range(19)]

dx = [0, 1, 1, -1]
dy = [1, 0, 1, 1]
switch = 1
for i in range(19):
    for j in range(19):
        if board[i][j]:
            color = board[i][j]
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                count = 1
                while 0 <= nx < 19 and 0 <= ny < 19 and board[nx][ny] == color:
                    count += 1
                    if count == 5:
                        if 0 <= i - dx[k] < 19 and 0 <= j - dy[k] < 19 and board[i - dx[k]][j - dy[k]] == color:
                            break
                        if 0 <= nx + dx[k] < 19 and 0 <= ny + dy[k] < 19 and board[nx + dx[k]][ny + dy[k]] == color:
                            break
                        print(color)
                        print(i+1, j+1)
                        switch = 0
                    nx += dx[k]
                    ny += dy[k]
if switch:
    print(0)