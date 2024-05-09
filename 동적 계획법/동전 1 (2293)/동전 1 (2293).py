import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
coin = []
dp = [0 for i in range(k+1)]
dp[0] = 1
for i in range(n):
    coin.append(int(input().rstrip()))

for cost in coin:
    for i in range(cost, k+1):
        dp[i] += dp[i-cost]
print(dp[k])