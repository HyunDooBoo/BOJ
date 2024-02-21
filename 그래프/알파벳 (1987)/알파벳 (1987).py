def dfs(x,y,cnt):
    global answer

    answer = max(answer, cnt)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<R and 0<=ny<C and not board[nx][ny] in alphabet_list:
            alphabet_list.add(board[nx][ny])
            dfs(nx, ny, cnt+1)
            alphabet_list.remove(board[nx][ny])

R, C = map(int, input().split())
board = []
alphabet_list = set()
answer = 0
dx = [0,0,1,-1]
dy = [1,-1,0,0]
for i in range(R):
    board.append(list(input()))
alphabet_list.add(board[0][0])
dfs(0,0,1)
print(answer)