import sys
input = sys.stdin.readline

r, c = map(int, input().split())

graph = []

for _ in range(r):
    graph.append(list(input().rstrip()))

sign = False
for i in range(r):
    for j in range(c):
        if graph[i][j] == 'W':
            dx = [-1, 1, 0, 0]
            dy = [0, 0, -1, 1]

            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
        
                if 0<=nx<r and 0<=ny<c and graph[nx][ny] == 'S':
                    sign = True
                    break
    
        elif graph[i][j] == 'S':
            continue

        elif graph[i][j] == '.':
            graph[i][j] = 'D'

if sign == True:
    print(0)

else:
    print(1)
    for i in graph:
        print(''.join(i))