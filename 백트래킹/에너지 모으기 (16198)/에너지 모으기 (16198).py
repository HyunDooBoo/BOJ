import sys

input = sys.stdin.readline

def dfs(x):
    global answer

    if len(W) == 2:
        answer = max(answer, x)
        return
    
    for i in range(1, len(W)-1):
        target = W[i-1] * W[i+1]

        v = W.pop(i)
        dfs(x + target)
        W.insert(i, v)


N = int(input().rstrip())
W = list(map(int, input().rstrip().split()))
answer = 0
dfs(0)
print(answer)