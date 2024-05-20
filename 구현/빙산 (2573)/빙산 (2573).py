import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x,y))
    visited[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if ice_m[nx][ny] == 0:
                    visited[x][y] += 1
                if ice_m[nx][ny] and visited[nx][ny] == -1:
                    q.append((nx,ny))
                    visited[nx][ny] = 0


N, M = map(int, input().rstrip().split())
ice_m = [list(map(int, input().rstrip().split())) for i in range(N)]
ice = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = -1

for i in range(N):
    for j in range(M):
        if ice_m[i][j] > 0:
            ice.append((i, j))

while ice:
    visited = [[-1] * M for i in range(N)]
    count = 0
    for i, j in ice:
        if ice_m[i][j] > 0 and visited[i][j] == -1:
            bfs(i, j)
            count += 1
    
    for i, j in ice:
        if visited[i][j] > 0:
            ice_m[i][j] -= visited[i][j]
            if ice_m[i][j] <= 0:
                ice_m[i][j] = 0
    answer += 1

    if count == 0:
        print(0)
        exit()
    
    if count >= 2:
        print(answer)
        exit()