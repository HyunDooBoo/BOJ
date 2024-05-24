import sys
from collections import deque

def check_cheese():
    cheese = 0
    for i in maps:
        cheese += sum(i)
    return cheese

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if maps[nx][ny] == 0:
                    if visited[nx][ny] == -1:
                        visited[nx][ny] = 0
                        q.append((nx, ny))
                else:
                    if visited[nx][ny] == -1:
                        visited[nx][ny] = 1
                    else:
                        visited[nx][ny] += 1
    
    for i in range(N):
        for j in range(M):
            if visited[i][j] >= 2:
                maps[i][j] = 0

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

maps = [list(map(int, input().rstrip().split())) for i in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
days = 1

while True:
    visited = [[-1] * M for i in range(N)]
    bfs(0,0)
    if not check_cheese():
        print(days)
        break
    days+=1