import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    while grow:
        x, y = grow.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                grow.append((nx, ny))

M, N = map(int, input().rstrip().split())
grow = deque()
dx = [0,0,-1,1]
dy = [-1,1,0,0]
tomato = []
answer = 0
for i in range(N):
    tomato.append(list(map(int, input().rstrip().split())))

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            grow.append((i,j))

bfs()
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
        answer = max(answer, j)
print(answer - 1)