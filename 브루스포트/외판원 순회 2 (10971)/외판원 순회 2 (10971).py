import sys

input = sys.stdin.readline

N = int(input().rstrip())

map_li = [list(map(int, input().split()))for _ in range(N)]
visited = [False] * N
answer = sys.maxsize

def dfs(x, first, value, depth):
    global answer
    if depth == N:
        if map_li[x][first]:
            value += map_li[x][first]
            if value < answer:
                answer = value
        return
    for i in range(N):
        if visited[i] == False and map_li[x][i]:
            visited[i] = True
            dfs(i, first, value + map_li[x][i], depth + 1)
            visited[i] = False

for i in range(N):
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False

print(answer)