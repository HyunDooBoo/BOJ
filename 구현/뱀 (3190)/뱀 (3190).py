import sys
from collections import deque

input = sys.stdin.readline

def change_direction(command, dir):
    if command == "D":
        dir = (dir + 1) % 4
    else:
        dir = dir - 1
        if dir < 0:
            dir = 3
    return dir

N = int(input().rstrip())
K = int(input().rstrip())
maps = [[0] * N for _ in range(N)]
for i in range(K):
    x, y = map(int, input().rstrip().split())
    maps[x-1][y-1] = 2
L = int(input().rstrip())
commands = [list(map(str, input().rstrip().split())) for i in range(L)]
time = 0
dx, dy = [0,1,0,-1], [1,0,-1,0]
snake = deque()
snake.append((0,0))
x, y= 0, 0
direction = 0
command_tmp = 0
while True:
    if command_tmp >= len(commands) or time < int(commands[command_tmp][0]):
        time += 1
        nx, ny = x + dx[direction], y + dy[direction]
        if 0 <= nx < N and 0 <= ny < N:
            if maps[nx][ny] == 1:
                break
            elif maps[nx][ny] == 2:
                maps[nx][ny] = 1
                maps[x][y] = 1
                snake.append((nx, ny))
            else:
                a, b = snake.popleft()
                maps[a][b] = 0
                maps[nx][ny] = 1
                snake.append((nx, ny))
            x, y = nx, ny
        else:
            break
        
    else:
        if command_tmp <= len(commands)-1:

            direction = change_direction(commands[command_tmp][1], direction)
            command_tmp += 1
        else:
            command_tmp += 1

print(time)