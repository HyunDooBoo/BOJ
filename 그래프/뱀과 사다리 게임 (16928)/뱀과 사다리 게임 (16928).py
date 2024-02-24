import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    que = deque()
    que.append(1)

    while que:
        x = que.popleft()
        if x == 100:
            print(dist[x])
            exit()
        for i in range(1,7):
            dx = x + i
            if dx <= 100 and dist[dx] == 0:
                if stair[dx]:
                    if dist[stair[dx][0]] == 0:
                        que.append(stair[dx][0])
                        dist[stair[dx][0]] = dist[x] + 1
                    else:
                        continue
                else:
                    que.append(dx)
                    dist[dx] = dist[x] + 1

N, M = map(int, input().rstrip().split())
stair = [[] for i in range(101)]
dist = [0] * 101
for i in range(N+M):
    u, v = map(int, input().rstrip().split())
    stair[u].append(v)
bfs()