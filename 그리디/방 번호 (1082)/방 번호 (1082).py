import sys

input = sys.stdin.readline

N = int(input().rstrip())
room = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
dp = [0 for i in range(M+1)]

for i in range(N-1, -1, -1):
    cost = room[i]
    for j in range(cost, M+1):
        dp[j] = max(dp[j-cost]*10+i,i,dp[j])
print(dp[M])