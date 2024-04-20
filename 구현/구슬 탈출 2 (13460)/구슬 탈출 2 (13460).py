import sys
from collections import deque

input = sys.stdin.readline

def move(x, y, dir):
    count = 0
    while True:
        count += 1
        if maps[x+dx[dir]][y+dy[dir]] == "#":
            break
        x += dx[dir]
        y += dy[dir]
        if maps[x][y] == "O":
            break

    return x, y, count

def bfs(rx, ry, bx, by, depth):
    que = deque()
    que.append((rx, ry, bx, by, depth))
    visited[rx][ry][bx][by] = True
    while que:
        rx, ry, bx, by, depth = que.popleft()
        if depth >= 10:
            break
        for i in range(4):
            nrx, nry, rcount = move(rx, ry, i)
            nbx, nby, bcount = move(bx, by, i)
            if maps[nbx][nby] != "O":
                if maps[nrx][nry] == "O":
                    print(depth+1)
                    return
                if nrx == nbx and nry == nby:
                    if rcount > bcount:
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if visited[nrx][nry][nbx][nby] == False:
                    visited[nrx][nry][nbx][nby] = True
                    que.append((nrx,nry,nbx,nby,depth + 1))
    print(-1)

N, M = map(int, input().rstrip().split())
maps = []
visited = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
rx, ry, bx, by = 0, 0, 0, 0
for i in range(N):
    maps.append(input().rstrip())
    for j in range(M):
        if maps[i][j] == 'R':
            rx, ry = i, j
        if maps[i][j] == 'B':
            bx, by = i, j

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

bfs(rx, ry, bx, by, 0)