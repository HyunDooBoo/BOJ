import sys

input = sys.stdin.readline
N = int(input())
cost = [0] + list(map(int,input().rstrip().split()))
dp = [0] * (N+1)
for i in range(1,N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i],cost[j]+dp[i-j])
print(dp[-1])
