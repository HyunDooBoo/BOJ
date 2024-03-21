import sys

input = sys.stdin.readline

def moving(a, b):
    if a==b:
        return 1
    elif a == 0:
        return 2
    elif (a-b)%2!=0:
        return 3
    else:
        return 4
nums = list(map(int,input().rstrip().split()))
dp = [[[4*len(nums) for i in range(5)] for i in range(5)]for i in range(len(nums))]
dp[0][0][0] = 0
for i in range(len(nums)-1):
    tmp = nums[i]
    for r in range(5):
        for l in range(5):
            dp[i+1][r][tmp] = min(dp[i][l][r]+moving(l, tmp),dp[i+1][r][tmp])
            dp[i+1][tmp][l] = min(dp[i][l][r]+moving(r, tmp),dp[i+1][tmp][l])
answer = 4*len(nums)
for i in range(5):
    for j in range(5):
        answer = min(answer, dp[-1][i][j])
print(answer)