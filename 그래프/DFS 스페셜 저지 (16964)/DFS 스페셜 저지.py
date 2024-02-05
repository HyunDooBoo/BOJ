import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(depth, idx):
    if visited[idx]:
        return
    visited[idx] = True
    depth_li[idx] = depth
    for next_idx in graph[idx]:
        if visited[next_idx] == False:
            children[idx] += dfs(depth + 1, next_idx) + 1
    return children[idx]

N = int(input().rstrip())
answer = []
depth_li = [0] * (N+1)
children = [0] * (N+1)
graph = [[] for i in range(N+1)]
visited = [False] * (N+1)
for i in range(N-1):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
result = [0] + list(map(int, input().split()))
dfs(0, 1)
dfs_check = True

for i in range(1, N+1):
    if i == 1:
        if result[i] != 1:
            dfs_check = False
            break
        else:
            continue
    node = result[i]
    depth_chk = i + children[node] + 1
    if depth_chk < N+1:
        chk_node = result[depth_chk]
        if depth_li[node] < depth_li[chk_node]:
            dfs_check = False
            break
if dfs_check:
    print(1)
else:
    print(0)