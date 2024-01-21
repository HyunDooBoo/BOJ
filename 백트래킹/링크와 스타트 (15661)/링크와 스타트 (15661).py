import sys

input = sys.stdin.readline

def dfs(depth):
    global answer
    if depth == N:
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    start += S[i][j]
                elif not visited[i] and not visited[j]:
                    link += S[i][j]
        answer = min(answer, abs(start-link))
        return

    for i in range(depth, N):
        visited[i] = True
        dfs(depth+1)
        visited[i] = False


N = int(input().rstrip())
S = []
for i in range(N):
    S.append(list(map(int, input().rstrip().split())))
visited = [False] * N

answer = 99999

for i in range(N):
    visited[i] = True
    dfs(i)
    visited[i] = False

print(answer)