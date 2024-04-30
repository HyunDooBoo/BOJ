import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append((x,y,0))
    visited = [[False] * N for i in range(N)]
    visited[x][y] = True
    candidates = []

    while q:
        x, y, count = q.popleft()
        if 0 < maps[x][y] < sw:
            candidates.append((count, x, y))

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == False:
                if sw >= maps[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx,ny,count + 1))
    if candidates:
        candidates.sort()
        return candidates[0][1], candidates[0][2], candidates[0][0]
    else:
        return -1, -1, 0

N = int(input().rstrip())
sw = 2
exp = 0
sx, sy = 0, 0
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
answer = 0
maps = []
for i in range(N):
    maps.append(list(map(int, input().rstrip().split())))
    for j in range(N):
        if maps[i][j] == 9:
            sx, sy = i, j
            maps[i][j] = 0

while True:
    sx, sy, cnt = bfs(sx, sy)

    if cnt == 0:
        break

    answer += cnt
    exp += 1
    if exp == sw:
        exp = 0
        sw += 1
    
    maps[sx][sy] = 0

print(answer)