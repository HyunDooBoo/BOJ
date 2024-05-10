import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
cost = [int(input().rstrip()) for i in range(n)]
dp = [10001 for i in range(k+1)]
dp[0] = 0
for i in cost:
    for j in range(i, k+1):
        dp[j] = min(dp[j], dp[j-i]+1)

if dp[k] != 10001:
    print(dp[k])
else:
    print(-1)