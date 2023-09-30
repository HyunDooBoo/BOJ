import sys

input = sys.stdin.readline

T = int(input())
for i in range(T):
    K = int(input())
    disk = [0] + list(map(int, input().rstrip().split()))
    dp = [[0]*(K+1) for i in range(K+1)]
    for i in range(1,K):
        dp[i][i+1]=disk[i]+disk[i+1]
    for i in range(K-1, 0, -1):
        for j in range(1, K+1):
            if dp[i][j] == 0 and j>i:
                dp[i][j] = min([dp[i][k]+dp[k+1][j] for k in range(i,j)])
                print(dp)
    print(dp[1][K])
