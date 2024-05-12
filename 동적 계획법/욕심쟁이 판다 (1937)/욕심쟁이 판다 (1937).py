import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    if visited[x][y]:
        return visited[x][y]
    
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n:
            if maps[nx][ny] > maps[x][y]:
                visited[x][y] = max(visited[x][y], dfs(nx, ny)+1)
    
    return visited[x][y]

n = int(input().rstrip())

dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = 0
maps = [list(map(int, input().rstrip().split())) for i in range(n)]
visited = [[0]*n for i in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i,j)

for i in range(n):
    answer = max(answer, max(visited[i]))
print(answer)