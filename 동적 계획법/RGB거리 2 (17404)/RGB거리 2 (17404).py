import sys

input = sys.stdin.readline

N = int(input().rstrip())
rgb = []
answer = 10000000

for i in range(N):
    rgb.append(list(map(int,input().rstrip().split())))

for first in range(3):
    dp = [[10000000, 10000000, 10000000] for i in range(N)]
    dp[0][first] = rgb[0][first]
    for i in range(1, N):
        dp[i][0] = rgb[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = rgb[i][1] + min(dp[i-1][0], dp[i-1][2])
        dp[i][2] = rgb[i][2] + min(dp[i-1][0], dp[i-1][1])
    for j in range(3):
        if j != first:
            answer = min(answer, dp[N-1][j])
print(answer)