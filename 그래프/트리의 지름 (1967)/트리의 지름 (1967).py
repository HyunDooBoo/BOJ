import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, cost):
    for i,j in graph[node]:
        if visited[i] == False:
            visited[i] = True
            dist[i] = cost+j
            dfs(i, cost+j)

n = int(input().rstrip())

graph = [[] for i in range(n+1)]
for i in range(n-1):
    node, child, cost = map(int, input().rstrip().split())
    graph[node].append((child, cost))
    graph[child].append((node, cost))

dist = [0] * (n+1)
visited = [False] * (n+1)
visited[1] = True
dfs(1, 0)

visited = [False] * (n+1)
visited[dist.index(max(dist))] = True
dfs(dist.index(max(dist)), 0)
print(max(dist))