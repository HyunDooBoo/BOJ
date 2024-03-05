import sys

input = sys.stdin.readline

N = int(input().rstrip())
dp = [0] * (N+1)
for i in range(1,N+1):
    cost, front, *list = map(int, input().rstrip().split())
    dp[i] = cost
    for j in list:
        dp[i] = max(dp[i], dp[j]+cost)
print(max(dp))