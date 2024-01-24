import sys

input = sys.stdin.readline

def dfs(depth, idx):

    global inssa
    visited[idx] = True

    if depth == 4:
        inssa = True
        return
    
    for i in friend[idx]:
        if visited[i] == False:
            dfs(depth+1, i)
    visited[idx] = False

N, M = map(int, input().rstrip().split())
friend = [[] for i in range(N)]
visited = [False] * N
inssa = False

for i in range(M):
    a, b = map(int, input().rstrip().split())
    friend[a].append(b)
    friend[b].append(a)

for i in range(N):
    
    dfs(0, i)
    
    if inssa:
        break

if inssa:
    print(1)
else:
    print(0)