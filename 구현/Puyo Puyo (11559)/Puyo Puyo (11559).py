import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True

    blocks = [(x,y)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<12 and 0<=ny<6:
                if visited[nx][ny] == False and maps[nx][ny] == maps[x][y]:
                    q.append((nx,ny))
                    visited[nx][ny] = True
                    blocks.append((nx, ny))
    return blocks
def boom(same):
    for x, y in same:
        maps[x][y] = "."

def down():
    for y in range(6):
        for x in range(10, -1, -1):
            for tmp in range(11, x, -1):
                if maps[x][y] != "." and maps[tmp][y] == ".":
                    maps[tmp][y] = maps[x][y]
                    maps[x][y] = "."
                    break


maps = []
for i in range(12):
    maps.append(list(map(str, input().rstrip())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
answer = 0

while True:
    switch = False
    visited = [[False] * 6 for i in range(12)]

    for i in range(12):
        for j in range(6):
            if maps[i][j] != '.' and visited[i][j] == False:
                same = bfs(i, j)

                if len(same) >= 4:
                    switch = True
                    boom(same)

    if switch:
        down()
        answer += 1
    
    else:
        break

print(answer)