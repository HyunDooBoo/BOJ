import sys

input = sys.stdin.readline

N = int(input().rstrip())
maps = [list(map(int, input().rstrip().split())) for i in range(N)]
dp = [[[0 for i in range(N)] for i in range(N)] for i in range(3)]
answer = 0
dp[0][0][1] = 1
for i in range(2,N):
    if maps[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]
    
    for i in range(1, N):
        for j in range(2, N):
            if maps[i][j] == 0 and maps[i][j-1] == 0 and maps[i-1][j] == 0:
                dp[2][i][j] = dp[0][i-1][j-1] + dp[1][i-1][j-1] + dp[2][i-1][j-1]
            
            if maps[i][j] == 0:
                dp[0][i][j] = dp[0][i][j-1] + dp[2][i][j-1]
                dp[1][i][j] = dp[1][i-1][j] + dp[2][i-1][j]
    
for i in range(3):
    answer += dp[i][N-1][N-1]

print(answer)