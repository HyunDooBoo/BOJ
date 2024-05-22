import sys

input = sys.stdin.readline

def check_row(x, y):
    i = x
    for j in range(y+1, N):
        if abs(maps[i][j-1] - maps[i][j]) > 1:
            return
        if maps[i][j-1] > maps[i][j]:
            for k in range(j, j+L):
                if N <= k or check[k] or maps[i][k] != maps[i][j]:
                    return False
                if maps[i][k] == maps[i][j]:
                    check[k] = True
        elif maps[i][j-1] < maps[i][j]:
            for k in range(j-1, j-1-L, -1):
                if 0 > k or check[k] or maps[i][k] != maps[i][j-1]:
                    return False
                if maps[i][k] == maps[i][j-1]:
                    check[k] = False
    return True

def check_col(x, y):
    j = y
    for i in range(x+1, N):
        if abs(maps[i-1][j] - maps[i][j]) > 1:
            return
        if maps[i-1][j] > maps[i][j]:
            for k in range(i, i+L):
                if N <= k or check[k] or maps[k][j] != maps[i][j]:
                    return False
                if maps[k][j] == maps[i][j]:
                    check[k] = True
        elif maps[i-1][j] < maps[i][j]:
            for k in range(i-1, i-1-L, -1):
                if 0 > k or check[k] or maps[k][j] != maps[i-1][j]:
                    return False
                if maps[k][j] == maps[i-1][j]:
                    check[k] = False
    return True


N, L = map(int, input().rstrip().split())
maps = [list(map(int ,input().rstrip().split())) for i in range(N)]
answer = 0

for i in range(N):
    check = [False for i in range(N)]
    if check_row(i, 0):
        answer += 1

for i in range(N):
    check = [False for i in range(N)]
    if check_col(0, i):
        answer += 1
print(answer)