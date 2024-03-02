import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    que = deque()
    que.append((0,0,K))
    visited[0][0][K] = 1
    while que:
        x, y, wall = que.popleft()
        if x == N-1 and y == M-1:
            print(visited[x][y][wall])
            exit()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M:
                if maps[nx][ny] == 1 and wall > 0 and visited[nx][ny][wall-1] == 0:
                    visited[nx][ny][wall-1] = visited[x][y][wall] + 1
                    que.append((nx, ny, wall - 1))
                elif maps[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    que.append((nx, ny, wall))
    print(-1)

dx = [1,-1,0,0]
dy = [0,0,1,-1]
N, M, K = map(int, input().rstrip().split())
visited = [[[0] * (K+1) for i in range(M)] for i in range(N)]
maps = []
for i in range(N):
    maps.append(list(map(int, input().rstrip())))
bfs()