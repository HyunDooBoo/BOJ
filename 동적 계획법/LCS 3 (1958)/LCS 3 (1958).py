import sys

input = sys.stdin.readline

a = [0] + list(map(str, input().rstrip()))
b = [0] + list(map(str, input().rstrip()))
c = [0] + list(map(str, input().rstrip()))

la = len(a)
lb = len(b)
lc = len(c)

dp = [[[0] *(lc+1) for i in range(lb+1)] for j in range(la+1)]

for i in range(1, la):
    for j in range(1, lb):
        for k in range(1, lc):
            if a[i] == b[j] and b[j] == c[k]:
                dp[i][j][k] = dp[i-1][j-1][k-1] +1
            else:
                dp[i][j][k] = max(dp[i][j][k-1], dp[i][j-1][k], dp[i-1][j][k])

answer = -1

for i in range(la):
    for j in range(lb):
        answer = max(max(dp[i][j]), answer)
print(answer)