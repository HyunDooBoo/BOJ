import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(start):
    for i in graph[start]:
        if visited[i] == False:
            visited[i] = True
            answer[i] = start
            dfs(i)

N = int(input().rstrip())
graph = [[] for i in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (N+1)
answer = [0] * (N+1)
dfs(1)

for i in range(2, N+1):
    print(answer[i])