import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    que = deque()
    que.append((0,0))
    dist[0][0] = 0

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N:
                if dist[nx][ny] == -1:
                    if walls[nx][ny] == 0:
                        dist[nx][ny] = dist[x][y]
                        que.appendleft((nx, ny))
                    else:
                        dist[nx][ny] = dist[x][y] + 1
                        que.append((nx, ny))

N, M = map(int, input().rstrip().split())
walls = []
dist = [[-1] * N for i in range(M)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(M):
    walls.append(list(map(int, input().rstrip())))

bfs()
print(dist[M-1][N-1])