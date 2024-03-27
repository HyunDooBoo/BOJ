import sys

input = sys.stdin.readline

N = int(input().rstrip())
muls = []
dp = [[0] * N for i in range(N)]
for i in range(N):
    r, c = map(int, input().rstrip().split())
    muls.append([r,c])

for i in range(1, N):
    for start in range(N):
        if i + start == N:
            break
        dp[start][start+i] = int(1e9)
        for k in range(start, start+i):
            dp[start][start+i] = min(dp[start][start+i], 
                                     dp[start][k]+dp[k+1][start+i]+muls[start][0]*muls[k][1]*muls[start+i][1])
print(dp[0][N-1])