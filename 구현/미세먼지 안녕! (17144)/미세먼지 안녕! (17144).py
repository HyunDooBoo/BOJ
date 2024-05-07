import sys

input = sys.stdin.readline

def find_cleaner():
    for i in range(R):
        if maps[i][0] == -1:
            return i, i+1

def move():
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    tmp = [[0] * C for i in range(R)]
    for i in range(R):
        for j in range(C):
            if maps[i][j] > 0:
                tmp_cnt = 0
                for k in range(4):
                    nx = dx[k] + i
                    ny = dy[k] + j
                    if 0 <= nx < R and 0 <= ny < C and maps[nx][ny] != -1:
                        tmp[nx][ny] += maps[i][j] // 5
                        tmp_cnt += maps[i][j] // 5
                maps[i][j] -= tmp_cnt
    
    for i in range(R):
        for j in range(C):
            maps[i][j] += tmp[i][j]

def clean_1():
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    dir = 0
    tmp = 0
    x, y = cu, 1
    while True:
        nx = dx[dir] + x
        ny = dy[dir] + y
        if x == cu and y == 0:
            break
        if 0 <= nx < R and 0 <= ny < C:
            maps[x][y], tmp = tmp, maps[x][y]
            x = nx
            y = ny
        else:
            dir += 1

def clean_2():
    dx = [0,1,0,-1]
    dy = [1,0,-1,0]
    dir = 0
    tmp = 0
    x, y = cd, 1
    while True:
        nx = dx[dir] + x
        ny = dy[dir] + y

        if x == cd and y == 0:
            break

        if 0 <= nx < R and 0 <= ny < C:
            maps[x][y], tmp = tmp, maps[x][y]
            x = nx
            y = ny
        else:
            dir += 1
        
        


R, C, T = map(int, input().rstrip().split())
maps = [list(map(int,input().rstrip().split())) for i in range(R)]
cu, cd = find_cleaner()
answer = 0
for i in range(T):
    move()
    clean_1()
    clean_2()

for i in range(R):
    answer += sum(maps[i])
print(answer+2)