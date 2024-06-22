import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

maps = [list(map(int, input().rstrip().split())) for i in range(N)]
dp = [[0 for i in range(M+1)] for i in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] += max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + maps[i-1][j-1]

print(dp[N][M])