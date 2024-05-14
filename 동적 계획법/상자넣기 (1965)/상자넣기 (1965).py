import sys

input = sys.stdin.readline

n = int(input().rstrip())
boxs = [0] + list(map(int, input().rstrip().split()))
dp = [1 for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i):
        if boxs[i] > boxs[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))