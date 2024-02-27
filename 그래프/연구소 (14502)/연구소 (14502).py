import sys
import copy
from collections import deque
from itertools import combinations

input = sys.stdin.readline

def bfs(maps2):
    global answer
    result = len(zero)-3
    que = deque()
    for i in range(len(virus_pos)):
        que.append(virus_pos[i])

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if maps2[nx][ny] == 0:
                    maps2[nx][ny] = 2
                    que.append([nx, ny])
                    result -= 1
    answer = max(result, answer)

def find(cnt):
    for i in combinations(zero,3):
        maps2 = copy.deepcopy(maps)
        for x,y in i:
            maps2[x][y] = 1
        bfs(maps2)

N, M = map(int, input().rstrip().split())
maps = []
virus_pos = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
zero = []
answer = 0
for i in range(N):
    maps.append(list(map(int, input().rstrip().split())))

for i in range(N):
    for j in range(M):
        if maps[i][j] == 2:
            virus_pos.append([i,j])
        if maps[i][j] == 0:
            zero.append([i,j])
find(0)
print(answer)