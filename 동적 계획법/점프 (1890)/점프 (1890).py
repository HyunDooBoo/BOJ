import sys

input = sys.stdin.readline

def dfs(x,y):

    if x == N-1 and y == N-1:
        return 1

    if visited[x][y] == -1:
        visited[x][y] = 0
        for i in range(2):
            nx, ny = x + dx[i] * board[x][y], y + dy[i] * board[x][y]
            if 0 <= nx < N and 0 <= ny < N:
                print(visited)
                visited[x][y] += dfs(nx, ny)
    
    return visited[x][y]

N = int(input().rstrip())
dx, dy = [1,0], [0,1]
board = [list(map(int, input().rstrip().split())) for i in range(N)]
visited = [[-1] * N for i in range(N)]
print(dfs(0,0))