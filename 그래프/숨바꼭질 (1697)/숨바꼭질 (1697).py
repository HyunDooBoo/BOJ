import sys
from collections import deque
sys.setrecursionlimit(10000)

def bfs():
    que = deque()
    que.append(N)
    while que:
        x = que.popleft()
        if x == K:
            print(distance[x])
            break
        for i in range(3):
            nx = x * teleport[i] + dx[i]

            if max_num > nx >= 0 and distance[nx] == 0:
                distance[nx] = distance[x] + 1
                que.append(nx)

input = sys.stdin.readline
max_num = 10 ** 5 + 1
N, K = map(int, input().rstrip().split())
dx = [1,-1, 0]
teleport = [1, 1, 2]
distance = [0] * (max_num)
bfs()