import sys
 
input = sys.stdin.readline

def back(x, y, d):
    nx = x+dx[d]
    ny = y+dy[d]

    if 0 <= nx < N and 0 <= ny < M:
        if maps[nx][ny] != 1:
            return True
    
    return False


N, M = map(int, input().rstrip().split())
r, c, d = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for i in range(N)]
visited = [[False]*M for i in range(N)]
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

visited[r][c] = True
count = 1

while True:
    switch = 0

    for i in range(4):
        d = (d+3)%4
        nx = r-dx[d]
        ny = c-dy[d]
        if 0 <= nx < N and 0 <= ny < M:
            if maps[nx][ny] == 0:
                if visited[nx][ny] == False:
                    visited[nx][ny] = True
                    count += 1
                    r = nx
                    c = ny
                    switch = 1
                    break
    
    if switch != 1:
        if back(r,c,d):
            r = r+dx[d]
            c = c+dy[d]
        else:
            print(count)
            break