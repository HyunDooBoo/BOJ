import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(x):
    global answer
    visited[x] = True
    team.append(x)
    if visited[num[x]]:
        if num[x] in team:
            answer += len(team[team.index(num[x]):])
    else:
        dfs(num[x])

T = int(input().rstrip())
for i in range(T):
    n = int(input().rstrip())
    num = [0] + list(map(int, input().rstrip().split()))
    visited = [True] + [False] * n
    answer = 0

    for j in range(1,n+1):
        if visited[j] == False:
            team = []
            dfs(j)
    print(n - answer)