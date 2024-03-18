import sys

input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
dp = [[0] * N for i in range(N)]
for i in range(N):
    dp[i][i] = 1
for i in range(N-1):
    if nums[i] == nums[i+1]:
        dp[i][i+1] = 1

for i in range(N-2):
    for j in range(N-2-i):
        idx = j + i + 2
        if nums[j] == nums[idx]:
            if dp[j+1][idx-1]:
                dp[j][idx] = 1

for i in range(M):
    S, E = map(int,input().rstrip().split())
    print(dp[S-1][E-1])