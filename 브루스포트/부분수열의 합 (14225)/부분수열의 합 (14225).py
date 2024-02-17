import sys

input = sys.stdin.readline

def dfs(idx, sum_num):
    if idx == N:
        check[sum_num] = 1
        return
    dfs(idx+1, sum_num+S[idx])
    dfs(idx+1, sum_num)

N = int(input().rstrip())
S = list(map(int, input().rstrip().split()))
check = [0] * 20000000
dfs(0, 0)
print(check.index(0))