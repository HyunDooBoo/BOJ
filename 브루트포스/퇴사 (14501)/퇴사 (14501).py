import sys

def dfs(day,cost):

    global answer

    if day > N:
        answer = max(cost, answer)
        return

    if day + consulting[day][0] <= N + 1:
        dfs(day + consulting[day][0], cost + consulting[day][1])
    dfs(day + 1, cost)
    

input = sys.stdin.readline

consulting = [[0,0]]
N = int(input().rstrip())
answer = 0
for i in range(N):
    T, P = map(int, input().rstrip().split())
    consulting.append([T, P])
dfs(1,0)
print(answer)