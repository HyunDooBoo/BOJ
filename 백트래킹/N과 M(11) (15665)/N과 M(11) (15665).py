import sys

input = sys.stdin.readline

def dfs(start):
    duplicate_num = 0
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(N):
        if duplicate_num != a[i]:
            duplicate_num = a[i]
            answer.append(a[i])
            dfs(i)
            answer.pop()

N, M = map(int, input().split())
answer = []
a = list(map(int, input().split()))
a.sort()
dfs(0)