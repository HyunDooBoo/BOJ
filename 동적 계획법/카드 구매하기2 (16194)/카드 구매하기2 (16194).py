import sys

input = sys.stdin.readline
N = int(input())
cost = [0] + list(map(int, input().rstrip().split()))
dp = [0 for i in range(N+1)]

for i in range(1,N+1):
    for j in range(1,i+1):
        if dp[i]:
            dp[i] = min(dp[i], cost[j]+dp[i-j])
        else:
            dp[i] = dp[i-j]+cost[j]
print(dp[-1])
