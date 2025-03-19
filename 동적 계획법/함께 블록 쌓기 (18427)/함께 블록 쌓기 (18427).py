import sys

input = sys.stdin.readline

N, M, H = map(int, input().rstrip().split())
blocks = [list(map(int, input().rstrip().split())) for i in range(N)]
dp = [[0] * (H+1) for i in range(N+1)]
dp[0][0] = 1

for i in range(1, N+1):
    for j in range(H+1):
        dp[i][j] = dp[i-1][j]
    for block in blocks[i-1]:
        for j in range(block, H+1):
            dp[i][j] += dp[i-1][j-block]
print(dp[N][H]%10007)