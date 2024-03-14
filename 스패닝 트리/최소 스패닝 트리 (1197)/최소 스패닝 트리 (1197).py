import sys

input = sys.stdin.readline

def parent_find(x):
    if parent[x] != x:
        parent[x] = parent_find(parent[x])
    return parent[x]

def parent_union(a, b):
    a = parent_find(a)
    b = parent_find(b)

    if a<b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int,input().rstrip().split())

graph = []
parent = []
for i in range(V+1):
    parent.append(i)

for i in range(E):
    A, B, C = map(int, input().rstrip().split())
    graph.append([A,B,C])

graph.sort(key = lambda x:x[2])
answer = 0
for i in graph:
    a, b, cost = i[0], i[1], i[2]
    if parent_find(a) != parent_find(b):
        parent_union(a, b)
        answer += cost
print(answer)