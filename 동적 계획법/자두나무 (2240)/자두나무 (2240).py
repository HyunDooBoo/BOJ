import sys

input = sys.stdin.readline

T, W = map(int, input().rstrip().split())
tree = [0] + [int(input().rstrip()) for i in range(T)]
dp = [[0] * (W+1) for i in range(T+1)]
if tree[1] == 1:
    dp[1][0], dp[1][1] = 1, 0
else:
    dp[1][0], dp[1][1] = 0, 1

for i in range(2, T+1):
    for j in range(W+1):
        k = 0
        if j % 2 == 0:
            k = tree[i]%2
        else:
            k = tree[i]//2
        dp[i][j] = max(dp[i-1][0:j+1])+k
print(max(dp[-1]))