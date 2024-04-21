import sys

input = sys.stdin.readline

def parent_find(x):
    if parent[x] != x:
        parent[x] = parent_find(parent[x])
    return parent[x]

def parent_union(x, y):
    x = parent_find(x)
    y = parent_find(y)

    if x>y:
        parent[x] = y
    else:
        parent[y] = x

god = [0]
answer = 0
N, M = map(int, input().rstrip().split())
parent = [i for i in range(N+1)]
for i in range(N):
    X, Y = map(int, input().rstrip().split())
    god.append([X, Y])

for i in range(M):
    X, Y = map(int, input().rstrip().split())
    parent_union(X, Y)

cost = []
for i in range(1,len(god)-1):
    for j in range(i+1, len(god)):
        x1, y1 = god[i]
        x2, y2 = god[j]
        dis = (abs(x1-x2) ** 2 + abs(y1-y2) ** 2) ** 0.5
        cost.append([dis, i, j])

cost.sort()
for li in cost:
    c, x, y = li

    if parent_find(x) != parent_find(y):
        parent_union(x, y)
        answer += c
print("{:.2f}".format(answer))