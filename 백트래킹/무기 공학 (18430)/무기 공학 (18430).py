import sys

input = sys.stdin.readline

def dfs(idx, result):
    global answer

    if idx == N*M:
        answer = max(result, answer)
        return
    x, y = idx // M, idx % M
    if visited[x][y] == False:
        for i in range(4):
            x1, y1, x2, y2 = x + check[i][0], y + check[i][1], x + check[i][2], y + check[i][3]
            if 0<=x1<N and 0<=x2<N and 0<=y1<M and 0<=y2<M:
                if visited[x1][y1] == False and visited[x2][y2] == False:
                    visited[x][y] = True
                    visited[x1][y1] = True
                    visited[x2][y2] = True
                    dfs(idx+1, result + wood[x][y] * 2 + wood[x1][y1] + wood[x2][y2])
                    visited[x][y] = False
                    visited[x1][y1] = False
                    visited[x2][y2] = False
    dfs(idx+1, result)

N, M = map(int, input().rstrip().split())

wood = [list(map(int, input().rstrip().split())) for i in range(N)]
visited = [[False] * M for i in range(N)]
check = [[0, 1, 1, 0], [1, 0, 0, -1], [0, -1, -1, 0], [-1, 0, 0, 1]] # ┌, ┐, ┘, └
answer = 0
dfs(0, 0)
print(answer)