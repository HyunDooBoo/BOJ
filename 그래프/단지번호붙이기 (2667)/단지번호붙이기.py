import sys

input = sys.stdin.readline

def dfs(x, y):

    global count
    
    count += 1
    
    for i in range(4):
        if (x+dx[i] < N and x+dx[i] >= 0) and (y+dy[i] < N and y+dy[i]>=0):
            if houses[x+dx[i]][y+dy[i]]:
                houses[x+dx[i]][y+dy[i]] = 0
                dfs(x+dx[i], y+dy[i])

N = int(input().rstrip())
houses = []
count = 0
result = []
for i in range(N):
    houses.append(list(map(int,input().rstrip())))

dx = [0,0,-1,1]
dy = [-1,1,0,0]

for i in range(N):
    for j in range(N):
        if houses[i][j]:
            houses[i][j] = 0
            dfs(i, j)
            result.append(count)
            count = 0

result.sort()

print(len(result))
for i in result:
    print(i)