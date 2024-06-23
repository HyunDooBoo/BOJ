import sys

input = sys.stdin.readline

T = int(input().rstrip())

for i in range(T):
    
    N = int(input().rstrip())
    cost = [0] + list(map(int, input().rstrip().split()))
    money = int(input().rstrip())
    dp = [[0] * (money+1) for _ in range(N+1)]
    for j in range(N+1):
        dp[j][0] = 1

    for j in range(1, N+1):
        for k in range(1, money + 1):
            dp[j][k] = dp[j-1][k]
            if k - cost[j] >= 0:
                dp[j][k] += dp[j][k-cost[j]]
    print(dp[N][money])