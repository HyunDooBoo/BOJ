import sys
from collections import deque
input = sys.stdin.readline

def bfs(island, x, y):
    que = deque()
    que.append((x,y))
    maps[x][y] = island
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if maps[nx][ny] == 1:
                    maps[nx][ny] = island
                    que.append((nx, ny))

def bfs_distance(island):
    global answer
    distance = [[-1] * N for i in range(N)]
    que = deque()

    for i in range(N):
        for j in range(N):
            if maps[i][j] == island:
                que.append((i,j))
                distance[i][j] = 0
    
    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N:
                if maps[nx][ny] > 0 and maps[nx][ny] != island:
                    answer = min(answer, distance[x][y])
                    return
                if maps[nx][ny] == 0 and distance[nx][ny] == -1:
                    distance[nx][ny] = distance[x][y] + 1
                    que.append((nx, ny))


N = int(input().rstrip())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
maps = []
for i in range(N):
    maps.append(list(map(int,input().rstrip().split())))

island = 2
answer = N*N
for i in range(N):
    for j in range(N):
        if maps[i][j] == 1:
            bfs(island, i, j)
            island += 1
for i in range(2, island):
    bfs_distance(i)
print(answer)