import sys

input = sys.stdin.readline

N = int(input().rstrip())

maps = [[False] * 101 for i in range(101)]

answer = 0

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

for i in range(N):

    y, x, d, g = map(int, input().rstrip().split())

    maps[x][y] = True

    dragon_curve = [d]
    for j in range(g):
        for k in range(len(dragon_curve)-1, -1, -1):
            dragon_curve.append((dragon_curve[k]+1)%4)
    
    for j in range(len(dragon_curve)):
        x += dx[dragon_curve[j]]
        y += dy[dragon_curve[j]]
        if 0 <= x < 101 and 0 <= y < 101:
            maps[x][y] = True

for i in range(100):
    for j in range(100):
        if maps[i][j] and maps[i+1][j] and maps[i][j+1] and maps[i+1][j+1]:
            answer += 1
print(answer)