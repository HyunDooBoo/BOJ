import sys

input = sys.stdin.readline

N = int(input().rstrip())
line = [0]
dp = [1 for i in range(N+1)]
for i in range(N):
    line.append(int(input().rstrip()))

for i in range(1, N+1):
    for j in range(1, i):
        if line[j] < line[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(N - max(dp))