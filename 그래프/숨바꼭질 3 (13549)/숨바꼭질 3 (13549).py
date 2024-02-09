import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    que = deque()
    if N == 0:
        que.append(1)
    else:
        que.append(N)
    while que:
        x = que.popleft()
        if x == K:
            if N == 0:
                print(distance[x] + 1)
            else:
                print(distance[x])
            break
        for i in range(3):
            nx = x * teleport[i] + dx[i]
            if 0<=nx<100001 and distance[nx] == 0:
                if nx == x*2:
                    que.appendleft(nx)
                    distance[nx] = distance[x]
                else:
                    que.append(nx)
                    distance[nx] = distance[x] + 1

N, K = map(int, input().rstrip().split())

dx = [-1,1,0]
teleport = [1,1,2]
distance = [0] * 100001
bfs()