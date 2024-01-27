import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(start):

    for i in range(1, N+1):
        if visited[i] == False and graph[start][i]:
            visited[i] = True
            dfs(i)

N, M = map(int, input().rstrip().split())

graph = [[False] * (N+1) for i in range(N+1)]
answer = 0
visited = [False] * (N+1)

for i in range(M):
    u, v = map(int, input().rstrip().split())
    graph[u][v] = True
    graph[v][u] = True

for i in range(1, N+1):
    if visited[i] == False:
        visited[i] = True
        dfs(i)
        answer += 1
print(answer)