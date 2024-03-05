import sys
from collections import deque

input = sys.stdin.readline

def bfs(x,y):
    que = deque()
    que.append((x,y))
    for water in waters:
        que.append((water[0],water[1]))
    while que:
        x, y = que.popleft()
        if maps[goal_x][goal_y] == 'S':
            print(dist[goal_x][goal_y])
            exit()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<R and 0<=ny<C:
                if (maps[nx][ny] =='.' or maps[nx][ny] == 'D') and maps[x][y] == 'S':
                    dist[nx][ny] = dist[x][y] + 1
                    maps[nx][ny] = 'S'
                    que.append((nx,ny))
                elif (maps[nx][ny] =='.' or maps[nx][ny] == 'S') and maps[x][y] == '*':
                    maps[nx][ny] = '*'
                    que.append((nx,ny))
    print("KAKTUS")

R, C = map(int, input().rstrip().split())
maps = []
for i in range(R):
    maps.append(list(map(str, input().rstrip())))

waters =[]
x, y = 0, 0
goal_x, goal_y = 0, 0
dx = [1,-1,0,0]
dy = [0,0,1,-1]
dist = [[0] * C for i in range(R)]

for i in range(R):
    for j in range(C):
        if maps[i][j] == '*':
            waters.append([i,j])
        elif maps[i][j] == 'D':
            goal_x, goal_y = i, j
        elif maps[i][j] == 'S':
            x, y = i, j

bfs(x,y)