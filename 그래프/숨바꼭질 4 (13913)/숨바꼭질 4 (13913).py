import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    que = deque()
    que.append(N)
    while que:
        x = que.popleft()
        if x == K:
            print(distance[x])
            answer.append(K)
            for i in range(distance[x]):
                answer.append(pos[answer[i]])
            answer.reverse()
            print(' '.join(map(str, answer)))
            break
        for i in range(3):
            nx = x * teleport[i] + dx[i]
            if 0<=nx<100001 and distance[nx] == 0:
                que.append(nx)
                distance[nx] = distance[x] + 1
                pos[nx] = x

N, K = map(int, input().rstrip().split())

dx = [1,-1,0]
teleport = [1,1,2]
pos = [0] * 100001
distance = [0] * 100001
answer = []
bfs()