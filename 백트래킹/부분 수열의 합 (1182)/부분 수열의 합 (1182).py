import sys

input = sys.stdin.readline

def dfs(depth, sum):
    global S
    global answer

    if depth == N:
        return
    
    sum += N_li[depth]

    if sum == S:
        answer += 1
    
    dfs(depth + 1, sum-N_li[depth])
    dfs(depth + 1, sum)

N, S = map(int, input().rstrip().split())
N_li = list(map(int, input().rstrip().split()))
answer = 0
dfs(0, 0)
print(answer)