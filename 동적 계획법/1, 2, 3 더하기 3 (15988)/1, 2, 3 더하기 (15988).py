import sys

input = sys.stdin.readline

T = int(input())
top = 0
n_list = []

dp = [0 for i in range(1000001)]

dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(T):
    n = int(input())
    if n>top:
        top = n
    n_list.append(n)

for i in range(4, top+1):
    dp[i] = (dp[i-1]+dp[i-2]+dp[i-3]) % 1000000009

for i in n_list:
    print(dp[i])
