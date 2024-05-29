import sys

input = sys.stdin.readline

N = int(input().rstrip())
maze = list(map(int, input().rstrip().split()))
dp = [(N+1) for i in range(N)]
dp[0] = 0
for i in range(N):
    for j in range(1, maze[i]+1):
        if i + j < N:
            dp[i+j] = min(dp[i+j], dp[i]+1)

if dp[-1] == N+1:
    print(-1)
else:
    print(dp[-1])