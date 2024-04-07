import sys

input = sys.stdin.readline

def cal_city_chicken_road():
    city_chicken_road = 0
    for i in home:
        min_dis = 2 * N - 2
        for j in range(len(visited)):
            if visited[j]:
                a = abs(i[0]-chicken[j][0]) + abs(i[1]-chicken[j][1])
                min_dis = min(min_dis, a)
        city_chicken_road += min_dis
    return city_chicken_road
        
    

def dfs(cnt, idx):
    global answer

    if cnt == M:
        tmp = cal_city_chicken_road()
        answer = min(tmp, answer)
        return
    
    for i in range(idx, len(chicken)):
        if visited[i] == False:
            visited[i] = True
            dfs(cnt+1, i+1)
            visited[i] = False


N, M = map(int, input().rstrip().split())
home = []
chicken = []
answer = 10000
for i in range(N):
    a = list(map(int, input().rstrip().split()))
    for j in range(N):
        if a[j] == 1:
            home.append([i,j])
        elif a[j] == 2:
            chicken.append([i,j])

visited = [False for i in range(len(chicken))]

for i in range(len(chicken)):
    visited[i] = True
    dfs(1,1)
    visited[i] = False

print(answer)