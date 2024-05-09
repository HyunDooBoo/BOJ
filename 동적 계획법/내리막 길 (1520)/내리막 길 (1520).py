import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

def dfs(x, y):

    if x == M-1 and y == N-1:
        return 1

    if dp[x][y] == -1:
        dp[x][y] = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < M and 0 <= ny < N:
                if maps[x][y] > maps[nx][ny]:
                    dp[x][y] += dfs(nx, ny)

    return dp[x][y]

M, N = map(int,input().rstrip().split())
maps = [list(map(int, input().rstrip().split())) for i in range(M)]
dp = [[-1] * N for i in range(M)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

print(dfs(0,0))