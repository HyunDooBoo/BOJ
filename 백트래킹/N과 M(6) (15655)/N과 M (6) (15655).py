import sys

input = sys.stdin.readline

def dfs(idx):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(idx, N):
        answer.append(a[i])
        dfs(i+1)
        answer.pop()
        
    
N, M = map(int, input().split())
answer = []
a = list(map(int, input().rstrip().split()))
a.sort()
dfs(0)