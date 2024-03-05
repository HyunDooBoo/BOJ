import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global wall
    global visited
    que = deque()
    que.append((7,0))
    while que:
        for i in range(len(que)):
            x, y = que.popleft()
            if (x, y) in wall:
                continue
            if x == 0:
                print(1)
                exit()
            for i in range(9):
                nx, ny = x+dx[i], y+dy[i]
                if 0<=nx<=7 and 0<=ny<=7:
                    if not (nx, ny) in wall and not (nx, ny) in visited:
                        que.append((nx, ny))
                        visited.add((nx, ny))
        if wall:
            visited = set()
        next_wall = set()
        for x, y in wall:
            if x < 7:
                next_wall.add((x+1,y))
        wall = next_wall
    print(0)

board = []
wall = set()
visited = set()
for i in range(8):
    board.append(list(map(str, input().rstrip())))

for i in range(8):
    for j in range(8):
        if board[i][j] == '#':
            wall.add((i,j))
dx = [-1,-1,-1,0,0,0,1,1,1]
dy = [0,1,-1,0,1,-1,0,1,-1]
bfs()