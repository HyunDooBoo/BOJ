import sys

input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if rank[a] > rank[b]:
        parent[b] = a
    elif rank[b] > rank[a]:
        parent[a] = b
    else:
        rank[b] += 1
        parent[a] = b

n, m = map(int, input().rstrip().split())
parent = [i for i in range(n)]
rank = [0] * n

for i in range(m):
    a, b = map(int, input().rstrip().split())
    if find_parent(a) == find_parent(b):
        print(i + 1)
        exit(0)
    union_parent(a, b)

print(0)