import sys

input = sys.stdin.readline

N = int(input().rstrip())
consulting = [[0,0]] + [list(map(int, input().rstrip().split())) for i in range(N)]
dp = [0 for i in range(N+1)]

for i in range(1, N+1):
    dp[i] = max(dp[i], dp[i-1])
    if consulting[i][0] + i-1 <= N:
        dp[i+consulting[i][0]-1] = max(dp[i-1]+consulting[i][1],dp[i+consulting[i][0]-1])
print(dp[-1])