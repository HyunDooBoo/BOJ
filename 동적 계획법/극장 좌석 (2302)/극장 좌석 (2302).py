import sys

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
vips = list(int(input().rstrip()) for i in range(M))
dp = [0 for i in range(N+1)]
dp[0] = 1
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

answer = 1

if M > 0:
    tmp = 0
    for i in vips:
        answer *= dp[i - tmp - 1]
        tmp = i
    answer *= dp[N-tmp]
else:
    answer = dp[N]
print(answer)