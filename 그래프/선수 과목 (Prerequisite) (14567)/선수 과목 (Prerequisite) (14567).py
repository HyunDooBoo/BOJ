import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            dp[i] = 1
            q.append(i)
    
    while q:
        x = q.popleft()
        for i in graph[x]:
            indegree[i] -= 1
            dp[i] = max(dp[x]+1, dp[i])
            if indegree[i] == 0:
                q.append(i)

N, M = map(int,input().rstrip().split())
graph = [[] for i in range(N+1)]
indegree = [0 for i in range(N+1)]
answer = []
dp = [0 for i in range(N+1)]
for i in range(M):
    A, B = map(int, input().rstrip().split())
    graph[A].append(B)
    indegree[B] += 1
bfs()
print(*dp[1:])