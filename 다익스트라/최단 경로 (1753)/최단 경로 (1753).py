import sys
import heapq

input = sys.stdin.readline

def bfs(start):
    heapq.heappush(q,(0, start))
    dis[start] = 0
    while q:
        cost, x = heapq.heappop(q)

        if dis[x] < cost:
            continue

        for next, val in graph[x]:
            if val+cost < dis[next]:
                heapq.heappush(q,(val+cost, next))
                dis[next] = val+cost

V, E = map(int, input().split())
K = int(input())
INF = int(1e9)
q = []
graph = [[] for i in range(V+1)]
dis = [INF for i in range(V+1)]

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))
bfs(K)
for i in range(1, len(dis)):
    if dis[i] == INF:
        print("INF")
    else:
        print(dis[i])