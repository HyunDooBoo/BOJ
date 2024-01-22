import sys

input = sys.stdin.readline

def check(i, j, k):
    if k == '<':
        if i > j:
            return False
    if k == '>':
        if i < j:
            return False
    return True

def dfs(depth, ans):
    global k
    if depth == k+1:
        answer.append(ans)
        return
    for i in range(10):
        if visited[i] == False and (depth == 0 or check(int(ans[depth-1]), i, k_li[depth-1])):
            visited[i] = True
            dfs(depth+1, ans+str(i))
            visited[i] = False

k = int(input().rstrip())
k_li = list(map(str, input().rstrip().split()))
visited = [False] * 10
answer = []
dfs(0, '')
answer.sort()
print(answer[-1])
print(answer[0])