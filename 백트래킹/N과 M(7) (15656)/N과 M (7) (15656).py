import sys

input = sys.stdin.readline

N, M = map(int,input().rstrip().split())

def dfs(depth):
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(N):
        answer.append(a[i])
        dfs(depth+1)
        answer.pop()

answer = []
a = list(map(int, input().rstrip().split()))
a.sort()
dfs(0)