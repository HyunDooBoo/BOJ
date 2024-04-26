import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y, group_code):
    global max_range

    visited[x][y] = True
    group[x][y] = group_code
    room_range = 1
    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        place = wall[x][y]
        for i in range(4):
            if place >= check[i]:
                place -= check[i]
            else:
                nx, ny = x+dx[i], y+dy[i]
                if 0 <= nx < M and 0 <= ny < N:
                    if visited[nx][ny] == False:
                        visited[nx][ny] = True
                        q.append([nx,ny])
                        group[nx][ny] = group_code
                        room_range += 1
    group_range.append(room_range)
    max_range = max(max_range, room_range)


N, M = map(int, input().rstrip().split())
wall = []
visited = [[False] * N for i in range(M)]
group = [[0] * N for i in range(M)]
group_range = [0]
check = [8, 4, 2, 1]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
group_code = 1
room = 0
max_range = 0
two_max_range = 0
for i in range(M):
    wall.append(list(map(int, input().rstrip().split())))

for i in range(M):
    for j in range(N):
        if visited[i][j] == False:
            bfs(i, j, group_code)
            room += 1
            group_code += 1

for i in range(M):
    for j in range(N):
        for k in range(4):
            if wall[i][j] >= check[k]:
                nx, ny = i+dx[k], j+dy[k]
                if 0<=nx<M and 0<=ny<N:
                    if group[i][j] != group[nx][ny]:
                        two_max_range = max(
                            two_max_range, group_range[group[i][j]] +
                            group_range[group[nx][ny]])

print(room)
print(max_range)
print(two_max_range)