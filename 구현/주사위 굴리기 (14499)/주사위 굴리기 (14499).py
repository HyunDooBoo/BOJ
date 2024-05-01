import sys

input = sys.stdin.readline

def roll(d):
    if d == 1:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]
    elif d == 2:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]
    elif d == 3:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]
    else:
        dice[0], dice[1], dice[2], dice[3], dice[4], dice[5] = dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]

N, M, x, y, k = map(int, input().rstrip().split())
dice = [0,0,0,0,0,0]
dx = [0,0,-1,1]
dy = [1,-1,0,0]
maps = []
for i in range(N):
    maps.append(list(map(int, input().rstrip().split())))

command = list(map(int, input().rstrip().split()))

for com in command:
    x += dx[com-1]
    y += dy[com-1]

    if x < 0 or x >= N or y < 0 or y >= M:
        x -= dx[com-1]
        y -= dy[com-1]
        continue

    roll(com)

    if maps[x][y] == 0:
        maps[x][y] = dice[-1]
    
    else:
        dice[-1] = maps[x][y]
        maps[x][y] = 0
    
    print(dice[0])