import sys

input = sys.stdin.readline

def parent_find(x):
    if parents[x] != x:
        parents[x] = parent_find(parents[x])
    return parents[x]

def parent_union(x, y):
    x = parent_find(x)
    y = parent_find(y)

    if x > y:
        parents[x] = y
    else:
        parents[y] = x

N = int(input().rstrip())
x_li = []
y_li = []
z_li = []

for i in range(N):
    x,y,z = map(int, input().rstrip().split())
    x_li.append([i, x])
    y_li.append([i, y])
    z_li.append([i, z])

x_li.sort(key=lambda x:x[1])
y_li.sort(key=lambda x:x[1])
z_li.sort(key=lambda x:x[1])

cost = []

for planets in x_li, y_li, z_li:
    for i in range(1, N):
        pl, cst = planets[i-1]
        pl2, cst2 = planets[i]
        cost.append([pl, pl2, abs(cst-cst2)])

cost.sort(key = lambda x:x[2])
parents = [i for i in range(N+1)]
answer, count = 0, 0
for li in cost:
    a, b, c = li
    if parent_find(a) != parent_find(b):
        parent_union(a, b)
        answer += c
        count += 1
    if count == N-1:
        break
print(answer)