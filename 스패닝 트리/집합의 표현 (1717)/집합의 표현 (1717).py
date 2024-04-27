import sys
sys.setrecursionlimit(1000000)

input = sys.stdin.readline

def parent_find(x):
    if x != parent[x]:
        parent[x] = parent_find(parent[x])
    return parent[x]

def parent_union(x, y):
    x = parent_find(x)
    y = parent_find(y)

    if x>y:
        parent[x] = y
    else:
        parent[y] = x

n, m = map(int, input().rstrip().split())
parent = [i for i in range(n+1)]

for i in range(m):
    a, b, c = map(int, input().rstrip().split())
    if a == 0:
        parent_union(b, c)
    else:
        if parent_find(b) == parent_find(c):
            print("YES")
        else:
            print("NO")