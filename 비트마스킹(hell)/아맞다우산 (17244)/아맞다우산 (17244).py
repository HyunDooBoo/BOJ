import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    q.append([x,y,1,0])
    visited[x][y][1] = True
    while q:
        x,y,count,move = q.popleft()
        if maps[x][y] == 'E' and count == (1 << code) - 1:
            print(move)
            return
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if maps[nx][ny] != '#':
                    try:
                        num = int(maps[nx][ny])
                        if visited[nx][ny][count|(1 << num)] == False:
                            visited[nx][ny][count|(1 << num)] = True
                            q.append([nx,ny,count|(1 << num), move + 1])           
                    except:
                        if visited[nx][ny][count] == False:
                            visited[nx][ny][count] = True
                            q.append([nx, ny, count, move + 1])
    print(-1)


N, M = map(int, input().rstrip().split())
maps = []
items = []
code = 1
for i in range(M):
    maps.append(list(input().rstrip()))
    for j in range(N):
        if maps[i][j] == 'S':
            start_x, start_y = i, j
        if maps[i][j] == 'X':
            items.append([i,j])
            maps[i][j] = code
            code += 1

visited = [[[False for i in range(2**code)]for i in range(N)]for i in range(M)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

bfs(start_x, start_y)