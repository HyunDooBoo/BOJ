import sys

input = sys.stdin.readline

N = int(input().rstrip())
power = list(map(int, input().rstrip().split()))
dp = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if power[i] < power[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(N-max(dp))