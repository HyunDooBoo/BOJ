import sys
input = sys.stdin.readline

a = [" "]+list(map(str, input().rstrip()))
b = [" "]+list(map(str, input().rstrip()))

dp = [["" for i in range(len(b))] for i in range(len(a))]

for i in range(1, len(a)):
    for j in range(1, len(b)):
        if a[i] == b[j]:
            dp[i][j] = dp[i-1][j-1] + a[i]
        else:
            if len(dp[i][j-1]) >= len(dp[i-1][j]):
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]
answer = dp[-1][-1]
print(len(answer), answer, sep="\n")