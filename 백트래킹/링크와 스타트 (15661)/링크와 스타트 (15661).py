import sys

input = sys.stdin.readline

def dfs():
    global answer
    start, link = 0, 0
    for i in range(N):
        for j in range(N):
            if visited[i] and visited[j]:
                start += S[i][j]
            elif not visited[i] and not visited[j]:
                link += S[i][j]
    answer = min(answer, abs(start-link))
    return

def sol(depth):
    if depth == N:
        dfs()
        return
    visited[depth] = True
    sol(depth+1)
    visited[depth] = False
    sol(depth+1)

N = int(input().rstrip())
S = []
for i in range(N):
    S.append(list(map(int, input().rstrip().split())))
visited = [False] * N

answer = 99999

sol(0)
print(answer)