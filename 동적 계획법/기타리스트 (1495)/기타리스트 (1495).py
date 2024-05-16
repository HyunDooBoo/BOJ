import sys

input = sys.stdin.readline

N, S, M = map(int, input().rstrip().split())
volume = [0] + list(map(int, input().rstrip().split()))
dp = [[0] * (M+1) for i in range(N+1)]
dp[0][S] = 1
answer = -1

for i in range(1, N+1):
    for j in range(M+1):
        if dp[i-1][j] > 0:
            if 0 <= j + volume[i] <= M:
                dp[i][j+volume[i]] = 1
            if 0 <= j - volume[i] <= M:
                dp[i][j-volume[i]] = 1

for i in range(M+1):
    if dp[N][i] == 1:
        answer = max(answer, i)
print(answer)