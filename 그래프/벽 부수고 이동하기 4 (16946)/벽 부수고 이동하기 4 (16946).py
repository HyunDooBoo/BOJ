import sys
from collections import deque

input = sys.stdin.readline

def bfs(a, b):

    result = 1
    que = deque()
    que.append((a,b))
    
    while que:
        x, y = que.popleft()
        zero_map[x][y] = group
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if maps[nx][ny] == 0 and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    result += 1
                    que.append((nx, ny))
    
    group_dic[group] = result

N, M = map(int, input().rstrip().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
group = 1
group_dic = {}
group_dic[0] = 0
visited = [[False for i in range(M)] for i in range(N)]
zero_map = [[0 for i in range(M)] for i in range(N)]
maps = []

for i in range(N):
    maps.append(list(map(int, input().rstrip())))


for i in range(N):
    for j in range(M):
        if maps[i][j] == 0 and visited[i][j] == False:
            visited[i][j] = True
            bfs(i, j)
            group += 1

for i in range(N):
    for j in range(M):
        group_set = set()
        if maps[i][j]:
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                if 0 <= nx < N and 0 <= ny < M:
                    group_set.add(zero_map[nx][ny])
            for result in group_set:
                maps[i][j] += group_dic[result]
                maps[i][j] %= 10

for i in maps:
    print(''.join(map(str, i)))