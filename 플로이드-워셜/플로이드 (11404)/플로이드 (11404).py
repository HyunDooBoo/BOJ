import sys

input = sys.stdin.readline

def floyd_warshall(tmp):
    distance[tmp][tmp] = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            distance[i][j] = min(distance[i][j], distance[i][tmp] + distance[tmp][j])

n = int(input().rstrip())
m = int(input().rstrip())

distance = [[int(1e9)] * (n+1) for i in range(n+1)]

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    distance[a][b] = min(c, distance[a][b])

for i in range(1, n+1):
    floyd_warshall(i)

for i in range(1, n+1):
    for j in range(1, n+1):
        if distance[i][j] == int(1e9):
            print("0", end=" ")
        else:
            print(distance[i][j], end=" ")
    print()