import sys

input = sys.stdin.readline

N, D = map(int, input().rstrip().split())
dp = list(range(D+1))
line = []

for i in range(N):
    start, goal, cross = map(int, input().rstrip().split())
    line.append([start, goal, cross])
line.sort()

for i in range(0, D+1):
    if i > 0:
        dp[i] = min(dp[i], dp[i-1]+1)
    for item in line:
        if item[0] == i and item[1] <= D:
            dp[item[1]] = min(dp[item[1]], dp[item[0]]+item[2])
print(dp[D])