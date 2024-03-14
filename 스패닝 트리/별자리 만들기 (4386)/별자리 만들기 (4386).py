import sys
import math

input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(x, y):
    x = find_parent(x)
    y = find_parent(y)
    parent[x] = y

n = int(input().rstrip())
stars = []
lines = []
parent = []

for i in range(n):
    parent.append(i)

answer = 0
for i in range(n):
    x, y = map(float, input().rstrip().split())
    stars.append([x, y])
for i in range(n-1):
    for j in range(i+1, n):
        lines.append((math.sqrt((stars[i][0]-stars[j][0])**2 + (stars[i][1]-stars[j][1])**2),i,j))

for line in lines:
    cost, a, b = line
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        answer += cost

print(round(answer, 2))