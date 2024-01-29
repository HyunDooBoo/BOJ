import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):

    graph[x][y] = 0

    for i in range(8):
        if (x+dx[i] < h and x+dx[i] >= 0) and (y+dy[i] < w and y+dy[i]>=0):
            if graph[x+dx[i]][y+dy[i]]:
                dfs(x+dx[i], y+dy[i])

dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [-1, 1, 0, 0, 1, -1, 1, -1]
while True:
    w, h = map(int, input().rstrip().split())
    if w == 0 and h == 0:
        break

    count = 0
    graph = []

    for i in range(h):
        graph.append(list(map(int, input().rstrip().split())))

    for i in range(h):
        for j in range(w):
            if graph[i][j]:
                dfs(i,j)
                count += 1
    
    print(count)