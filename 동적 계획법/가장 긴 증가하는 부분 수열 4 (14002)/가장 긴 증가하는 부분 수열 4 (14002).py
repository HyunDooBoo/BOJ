import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int,input().rstrip().split()))

dp = [1 for i in range(N)]

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j]+1)

result = []
temp = max(dp)

for i in range(N-1, -1, -1):
    if dp[i] == temp:
        result.append(A[i])
        temp -= 1

result.reverse()
print(max(dp))
print(*result)
