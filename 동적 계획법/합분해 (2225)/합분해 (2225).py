import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

dp = [[0] * (201) for i in range(201)]

for i in range(1, N+1):
    dp[1][i] = 1
    dp[2][i] = i + 1

for i in range(2, K+1):
    dp[i][1] = i
    for j in range(2, N+1):
        dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000000
        
print(dp[K][N])
