import sys

input = sys.stdin.readline

def parent_find(x):
    if parent[x] != x:
        parent[x] = parent_find(parent[x])
    return parent[x]

def parent_union(x, y):
    x = parent_find(x)
    y = parent_find(y)
    if x > y:
        parent[x] = y
    else:
        parent[y] = x

N, P = map(int, input().rstrip().split())
cost = []
cross_cost = []

for i in range(N):
    C = int(input().rstrip())
    cost.append(C)
for i in range(P):
    S, E, L = map(int, input().rstrip().split())
    cross_cost.append([S,E,cost[S-1]+cost[E-1]+L*2])

cross_cost.sort(key=lambda x:x[2])

parent = [i for i in range(N+1)]
answer, count = 0, 0
answer += min(cost)
for li in cross_cost:
    a, b, c = li
    if parent_find(a) != parent_find(b):
        parent_union(a, b)
        answer += c
        count +=1
    if count == N-1:
        break
print(answer)