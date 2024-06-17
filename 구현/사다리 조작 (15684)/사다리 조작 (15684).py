import sys

input = sys.stdin.readline

def check():
    for i in range(N):
        tmp = i
        for j in range(H):
            if board[j][tmp]:
                tmp += 1
            elif tmp>0 and board[j][tmp-1]:
                tmp -= 1
        if tmp != i:
            return False
    return True

def dfs(x, y, count):
    global answer
    if check():
        answer = min(answer, count)
        return
    elif count == 3 or answer <= count:
        return
    
    for i in range(x, H):
        if i == x:
            tmp = y
        else:
            tmp = 0
        
        for j in range(tmp, N - 1):
            if board[i][j] == False and board[i][j+1] == False:
                if j>0 and board[i][j-1]:
                    continue
                board[i][j] = True
                dfs(i, j+2, count+1)
                board[i][j] = False


N, M, H = map(int, input().rstrip().split())
board = [[False] * N for i in range(H)]
answer = 4
for i in range(M):
    a, b = map(int, input().rstrip().split())
    board[a-1][b-1] = True

dfs(0,0,0)

if answer > 3:
    print(-1)
else:
    print(answer)