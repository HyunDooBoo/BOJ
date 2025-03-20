import sys
import copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline

def bfs(pos):
    que = deque(pos)
    copy_map = copy.deepcopy(virus_map)
    count = 0
    visited = [[False] * N for i in range(N)]

    for i, j in que:
        copy_map[i][j] = 0
        visited[i][j] = True

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == False and copy_map[nx][ny] != '-':
                if copy_map[nx][ny] == -1:
                    copy_map[nx][ny] = copy_map[x][y] + 1
                    count = max(count, copy_map[nx][ny])
                elif copy_map[nx][ny] == '*':
                    copy_map[nx][ny] = copy_map[x][y] + 1
                visited[nx][ny] = True
                que.append((nx, ny))

    for check in copy_map:
        if -1 in check:
            return int(1e9)
    return count
                

N, M = map(int, input().rstrip().split())

virus_map = [list(map(int, input().rstrip().split())) for i in range(N)]
all_virus_pos = []
dx, dy = [1,-1,0,0], [0,0,1,-1]
answer = int(1e9)

for i in range(N):
    for j in range(N):
        if virus_map[i][j] == 1:
            virus_map[i][j] = '-'
        elif virus_map[i][j] == 2:
            virus_map[i][j] = '*'
            all_virus_pos.append((i,j))
        else:
            virus_map[i][j] = -1

for virus_pos in combinations(all_virus_pos, M):
    answer = min(answer, bfs(virus_pos))

if answer < int(1e9):
    print(answer)
else:
    print(-1)