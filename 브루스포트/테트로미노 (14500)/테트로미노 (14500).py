import sys

input = sys.stdin.readline

move = [(0,1), (0,-1), (1,0), (-1,0)]

N, M = map(int, input().rstrip().split())

paper = [list(map(int, input().rstrip().split())) for i in range(N)]
visit = [[False] *M for i in range(N)]

max_count = 0

def dfs(i, j, count, visit_count):
    global max_count
    if visit_count == 4:
        max_count = max(max_count, count)
        return
    
    for moving in range(4):
        moving_i = i+move[moving][0]
        moving_j = j+move[moving][1]
        if 0 <= moving_i < N and 0 <= moving_j < M and not visit[moving_i][moving_j]:
            visit[moving_i][moving_j] = True
            dfs(moving_i, moving_j, count + paper[moving_i][moving_j], visit_count+1)
            visit[moving_i][moving_j] = False


def another(i, j):
    global max_count
    for n in range(4):
        count = paper[i][j]
        for moveing in range(3):
            tmp = (n+moveing)%4
            moving_i = i+move[tmp][0]
            moving_j = j+move[tmp][1]

            if not (0 <= moving_i < N and 0 <= moving_j < M):
                break

            count += paper[moving_i][moving_j]
        max_count = max(max_count, count)

for i in range(N):
    for j in range(M):
        visit[i][j] = True
        dfs(i, j, paper[i][j], 1)
        visit[i][j] = False
        another(i, j)

print(max_count)