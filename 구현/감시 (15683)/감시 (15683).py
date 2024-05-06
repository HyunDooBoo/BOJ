import sys
import copy
input = sys.stdin.readline

def scan(dir, x, y, field):
    for i in dir:
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]
            if 0 <= nx < N and 0 <= ny < M:
                if field[nx][ny] == 6:
                    break
                elif field[nx][ny] == 0:
                    field[nx][ny] = -1
            else:
                break

def dfs(depth, field):
    global answer

    if depth == len(cctvs):
        cnt = 0
        for i in range(N):
            for j in range(M):
                if field[i][j] == 0:
                    cnt += 1
        answer = min(cnt, answer)
        return
    
    copy_field = copy.deepcopy(field)
    cctv, x, y = cctvs[depth]

    for i in direction[cctv]:
        scan(i, x, y, copy_field)
        dfs(depth + 1, copy_field)
        copy_field = copy.deepcopy(field)

N, M = map(int, input().rstrip().split())
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
direction = [[], [[0], [1], [2], [3]], [[0, 2], [1, 3]],
             [[0, 1], [1, 2], [2, 3], [0, 3]],
             [[0,1,2], [0,1,3], [1,2,3], [0,2,3]],
             [[0,1,2,3]]]
maps = []
cctvs = []
answer = N*M
for i in range(N):
    maps.append(list(map(int, input().rstrip().split())))
    for j in range(M):
        if maps[i][j] in [1, 2, 3, 4, 5]:
            cctvs.append([maps[i][j], i, j])

dfs(0, maps)
print(answer)