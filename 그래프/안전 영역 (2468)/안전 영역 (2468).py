import sys

input = sys.stdin.readline

def dfs(x, y, z):
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<N and 0<=ny<N and visited[nx][ny] == False and maps[nx][ny] > z:
            visited[nx][ny] = True
            dfs(nx, ny, z)

N = int(input().rstrip())

maps = [list(map(int, input().rstrip().split())) for i in range(N)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

answer = 1
maxi = 0
for i in maps:
    maxi = max(i)

for i in range(maxi):
    visited = [[False] * N for i in range(N)]
    count = 0

    for x in range(N):
        for y in range(N):
            if visited[x][y] == False and maps[x][y] > i:
                count += 1
                visited[x][y] = True
                dfs(x, y, i)
    
    answer = max(answer, count)
print(answer)