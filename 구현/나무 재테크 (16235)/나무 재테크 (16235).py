import sys
from collections import deque

input = sys.stdin.readline

def go():

    #봄
    for i in range(N):
        for j in range(N):
            tc = len(tree[i][j])
            for k in range(tc):
                if graph[i][j] < tree[i][j][k]:
                    for l in range(k, tc):
                        d_tree[i][j].append(tree[i][j].pop())
                    break
                else:
                    graph[i][j] -= tree[i][j][k]
                    tree[i][j][k] += 1
    
    #여름
    for i in range(N):
        for j in range(N):
            while d_tree[i][j]:
                graph[i][j] += d_tree[i][j].pop() // 2

    #가을
    for i in range(N):
        for j in range(N):
            for k in list(tree[i][j]):
                if k%5 == 0:
                    for l in range(8):
                        nx = i + dx[l]
                        ny = j + dy[l]
                        if 0 <= nx < N and 0 <= ny < N:
                            tree[nx][ny].appendleft(1)

            #겨울                            
            graph[i][j] += yang[i][j]

N, M, K = map(int, input().rstrip().split())
yang = [list(map(int, input().rstrip().split())) for i in range(N)]
graph = [[5] * N for i in range(N)]
tree = [[deque() for i in range(N)] for j in range(N)]
d_tree = [[list() for _ in range(N)] for _ in range(N)]

for i in range(M):
    x, y, z = map(int, input().rstrip().split())
    tree[x-1][y-1].append(z)

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(K):
    go()

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(tree[i][j])

print(answer)