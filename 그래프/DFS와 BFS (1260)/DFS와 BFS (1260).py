import sys
from collections import deque

input = sys.stdin.readline

def dfs(start):

    visited[start] = True
    print(start, end = " ")
    
    for i in range(1, N+1):
        if visited[i] == False and li[start][i]:
            dfs(i)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        idx = q.popleft()
        print(idx, end= ' ')
        for i in range(1, N+1):
            if visited[i] == False and li[idx][i]:
                q.append(i)
                visited[i] = True


N, M, V = map(int, input().rstrip().split())
li = [[False] * (N+1) for i in range(N+1)]
visited = [False] * (N+1)

for i in range(M):
    a, b = map(int, input().rstrip().split())
    li[a][b] = True
    li[b][a] = True

answer = []
visited = [False] * (N+1)
dfs(V)
print()
visited = [False] * (N+1)
bfs(V)