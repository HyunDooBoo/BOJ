import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    que = deque()
    que.append(1)
    visited[1] = 0

    while que:
        now = que.popleft()
        for i in graph[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                children[now].add(i)
                que.append(i)

N = int(input().rstrip())
graph = [[] for i in range(N+1)]
children = [set() for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
result = list(map(int, input().rstrip().split()))
visited = [-1] * (N+1)
bfs()
switch = 0
idx = 1
for i in result:
    if idx == N:
        break
    child_length = len(children[i])
    a = set(result[idx:idx+child_length])
    b = children[i]
    if a!=b:
        print(0)
        switch = 1
        break
    idx += child_length
if switch == 0:
    print(1)