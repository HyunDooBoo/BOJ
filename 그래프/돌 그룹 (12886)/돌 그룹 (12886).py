import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    que = deque()
    que.append((A,B))
    visited[A][B] = True
    while que:
        a, b = que.popleft()
        c = sum_rock - a - b
        if a == b == c:
            print(1)
            return
        
        for a2, b2 in (a,b), (b,c), (a,c):
            if a2 > b2:
                a2 -= b2
                b2 += b2
            elif a2 < b2:
                b2 -= a2
                a2 += a2
            else:
                continue
            if visited[a2][b2] == False:
                que.append((a2, b2))
                visited[a2][b2] = True
    print(0)

A, B, C = map(int, input().rstrip().split())
sum_rock = A+B+C
visited = [[False] * (sum_rock+1) for i in range(sum_rock+1)]

if (sum_rock)%3 == 0:
    bfs()
else:
    print(0)