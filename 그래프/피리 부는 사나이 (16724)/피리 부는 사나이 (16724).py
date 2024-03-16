import sys

input = sys.stdin.readline

def dfs(x, y):
    global answer
    visited[x][y] = True
    cycle.append([x, y])

    if li[x][y] == 'U':
        x -= 1
    elif li[x][y] == 'D':
        x += 1
    elif li[x][y] == 'R':
        y += 1
    elif li[x][y] == 'L':
        y -= 1
    if visited[x][y]:
        if [x,y] in cycle:
            answer += 1
    else:
        dfs(x, y)

N, M = map(int, input().rstrip().split())
li = []
visited = [[False] * M for i in range(N)]
answer = 0
for i in range(N):
    li.append(list(map(str, input().rstrip())))
for i in range(N):
    for j in range(M):
        if visited[i][j] == False:
            cycle = []
            dfs(i, j)
print(answer)