import sys

input = sys.stdin.readline

def dfs(x, y, ball,depth):
    global clear
    if clear:
        return

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<= nx < N and 0<=ny<M:
            if depth>=4 and nx == start_x and ny == start_y:
                clear = True
                return
            if visited[nx][ny] != False:
                continue
            if ball == ball_graph[nx][ny]:
                visited[nx][ny] = True
                dfs(nx,ny,ball,depth + 1)
                visited[nx][ny] = False

N, M = map(int, input().rstrip().split())
ball_graph = []
visited = [[False] * M for i in range(N)]
clear = False
dx = [0,0,1,-1]
dy = [1,-1,0,0]

for i in range(N):
    ball_graph.append(list(map(str, input().rstrip())))

for i in range(N):
    for j in range(M):
        if visited[i][j] == False:
            visited[i][j] = True
            start_x, start_y = i, j
            dfs(i, j, ball_graph[i][j],1)
if clear:
    print("Yes")
else:
    print("No")