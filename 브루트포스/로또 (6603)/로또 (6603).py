import sys

input = sys.stdin.readline

answer = []

def dfs(pre):
    if len(answer) == 6:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, a[0]+1):
        if visited[i] == False and a[i] > pre:
            answer.append(a[i])
            visited[i] = True
            dfs(a[i])
            visited[i] = False
            answer.pop()


while(True):
    a = list(map(int, input().rstrip().split()))
    visited = [False] * (a[0]+1)
    if a[0] == 0:
        break
    dfs(0)
    print()