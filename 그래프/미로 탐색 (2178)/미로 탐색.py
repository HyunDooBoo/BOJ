import sys
from collections import deque

input = sys.stdin.readline

def bfs(x, y):

    position = deque()
    position.append((x,y))
    global count

    while position:
        x, y = position.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<N and 0<=ny<M:
                if maze[nx][ny] == 1:
                    position.append((nx, ny))
                    maze[nx][ny] += maze[x][y]
    return maze[N-1][M-1]


N, M = map(int, input().rstrip().split())
maze = []
dx = [0,0,-1,1]
dy = [-1,1,0,0]
count = 1
result = []

for i in range(N):
    maze.append(list(map(int, input().rstrip())))

print(bfs(0,0))