import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    que = deque()
    que.append([0,0,0])
    visited[0][0][0] = 1
    while que:
        x, y, wall = que.popleft()
        if x==N-1 and y==M-1:
            return visited[x][y][wall]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if maps[nx][ny] == 1 and wall == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    que.append([nx,ny,1])
                elif maps[nx][ny] == 0 and visited[nx][ny][wall] == 0:
                    visited[nx][ny][wall] = visited[x][y][wall] + 1
                    que.append([nx,ny,wall])
    return -1

N, M = map(int, input().rstrip().split())
maps = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
for i in range(N):
    maps.append(list(map(int, input().rstrip())))
print(bfs())