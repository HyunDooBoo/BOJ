import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip().split()))

dp = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i],dp[j]+1)
print(max(dp))
