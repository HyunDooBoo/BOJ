import sys

input = sys.stdin.readline

def dfs(node, cost):
    for i, j in tree[node]:
        if visited[i] == False:
            visited[i] = True
            dist[i] = cost+j
            dfs(i, cost+j)

V = int(input().rstrip())

tree = [[] for i in range(V+1)]
for i in range(V):
    a = list(map(int, input().rstrip().split()))
    node = a[0]
    for j in range(1, len(a), 2):
        if a[j] == -1:
            break
        tree[node].append((a[j], a[j+1]))

visited = [False] * (V+1)
visited[1] = True
dist = [0] * (V+1)

dfs(1, 0)
visited = [False] * (V+1)
visited[dist.index(max(dist))] = True
dfs(dist.index(max(dist)), 0)
print(max(dist))