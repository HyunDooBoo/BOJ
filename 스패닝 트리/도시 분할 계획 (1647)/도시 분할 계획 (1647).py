import sys

input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x<y:
        parent[y] = x
    else:
        parent[x] = y

N, M = map(int, input().rstrip().split())
graph = []
parent = []
answer = 0

for i in range(0, N+1):
    parent.append(i)

for i in range(M):
    A, B, C = map(int, input().rstrip().split())
    graph.append([A,B,C])

graph.sort(key = lambda x:x[2])
for i in range(len(graph)):
    x, y, cost = graph[i][0], graph[i][1], graph[i][2]
    if find_parent(x) != find_parent(y):
        union_parent(x, y)
        answer += cost
        last = cost
print(answer-last)