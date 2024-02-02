import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    position = deque()
    position.append((k_x,k_y))
    while position:
        x, y = position.popleft()
        if x == g_x and y == g_y:
            return matrix[x][y] -1
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0<=nx<I and 0<=ny<I and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y] + 1
                position.append((nx, ny))


T = int(input().rstrip())

for i in range(T):
    I = int(input().rstrip())
    matrix = [[0]*I for i in range(I)]
    dx = [-2,-2,2,2,-1,-1,1,1]
    dy = [-1,1,-1,1,-2,2,-2,2]
    k_x, k_y = map(int,input().rstrip().split())
    g_x, g_y = map(int,input().rstrip().split())
    matrix[k_x][k_y] = 1
    print(bfs())