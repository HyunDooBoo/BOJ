import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, depth):
    global max_depth
    visited[node] = True
    tree[node][3] = depth
    if max_depth < depth:
        max_depth = depth

    for i in range(2):
        if visited[tree[node][i+1]] == False:
            dfs(tree[node][i+1], depth + 1)

def in_order(v):
    global order

    if v:
        in_order(tree[v][1])
        tree[v][4] = order
        order += 1
        in_order(tree[v][2])

N = int(input().rstrip())
tree = [[0,0,0,0,0] for i in range(N+1)]
visited = [False] * (N+1)
visited[0] = True
max_depth = 0
for i in range(N):
    node, left, right = map(int,input().rstrip().split())
    if left == -1: left = 0
    if right == -1: right = 0
    tree[node][1] = left
    tree[node][2] = right
    tree[left][0] = node
    tree[right][0] = node

root = 0
for i in range(1, N+1):
    if tree[i][0] == 0:
        root = i

dfs(root,1)

order = 1
in_order(root)

depth_list = [[] for i in range(max_depth + 1)]

for i in range(1, N+1):
    depth_list[tree[i][3]].append(tree[i][4])

answer = []
for i in range(len(depth_list)):
    if len(depth_list[i]) <= 1:
        answer.append(1)
    else:
        answer.append(max(depth_list[i])-min(depth_list[i])+1)
print(answer.index(max(answer),1), max(answer))