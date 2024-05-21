import sys
from collections import deque

input = sys.stdin.readline

def check_cheese():
    cheese = 0
    for i in maps:
        cheese += sum(i)
    return cheese

def bfs():
    q = deque()
    q.append((0,0))
    visited[0][0] = True
    del_c = []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == False:
                visited[nx][ny] = True
                if maps[nx][ny] == 0:
                    q.append((nx, ny))
                else:
                    del_c.append((nx, ny))
    
    for x, y in del_c:
        maps[x][y] = 0

N, M = map(int, input().rstrip().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().rstrip().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
answer = 0
day = 0
while True:
    visited = [[False] * M for i in range(N)]
    cheese = check_cheese()
    if cheese:
        bfs()
    else:
        print(day)
        print(answer)
        break
    day += 1
    answer = cheese