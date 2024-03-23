import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    q = deque()
    for i in range(1, N+1):
        if indegree[i] == 0:
            dp[i] = time[i]
            q.append(i)

    while q:
        x = q.popleft()
        for i in graph[x]:
            indegree[i] -= 1
            dp[i] = max(dp[x]+time[i], dp[i])
            if indegree[i] == 0:
                q.append(i)

T = int(input().rstrip())
for i in range(T):
    N, K = map(int, input().rstrip().split())
    time = [0] + list(map(int, input().rstrip().split()))
    indegree = [0] * (N+1)
    dp = [0 for i in range(N+1)]
    graph = [[] for i in range(N+1)]
    for i in range(K):
        X, Y = map(int, input().rstrip().split())
        graph[X].append(Y)
        indegree[Y] += 1
    W = int(input().rstrip())
    bfs()
    print(dp[W])
    