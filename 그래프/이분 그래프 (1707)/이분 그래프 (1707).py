import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(start, flag):
    global sign

    if sign:
        return
    
    visited[start] = flag

    for i in graph[start]:
        if visited[i] == False:
            dfs(i, -flag)
        elif visited[start] == visited[i]:
            sign = True
            return

K = int(input().rstrip())
for i in range(K):
    V, E = map(int, input().rstrip().split())
    sign = False
    visited = [0] * (V+1)
    graph = [[] for i in range(V+1)]
    for j in range(E):
        u, v = map(int, input().rstrip().split())
        graph[u].append(v)
        graph[v].append(u)
    for k in range(1, V+1):
        if visited[k] == False:
            dfs(k, 1)
            if sign:
                break
    if sign:
        print("NO")
    else:
        print("YES")