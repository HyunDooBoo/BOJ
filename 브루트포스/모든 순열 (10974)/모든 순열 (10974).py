import sys

input = sys.stdin.readline

N = int(input().rstrip())
a = []

def dfs():
    if len(a) == N:
        print(' '.join(map(str, a)))
        return
    for i in range(1, N+1):
        if i not in a:
            a.append(i)
            dfs()
            a.pop()
dfs()