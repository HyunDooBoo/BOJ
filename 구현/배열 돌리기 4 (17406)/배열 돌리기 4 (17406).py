import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

def dfs(depth):
    global answer
    
    if depth == K:
        answer = min(answer, rotate(deepcopy(order)))
        return
    
    for i in range(K):
        if visited[i] == False:
            visited[i] = True
            order.append(command[i])
            dfs(depth + 1)
            visited[i] = False
            order.pop()

def rotate(orders):
    copy_A = deepcopy(A)
    while orders:
        x, y, s = orders.popleft()
        x1, y1 = x-s-1, y-s-1
        x2, y2 = x+s-1, y+s-1
        cycle = min(abs(x1-x2)+1, abs(y1-y2)+1) // 2
        for i in range(cycle):
            que = deque()
            que.extend(copy_A[x1+i][y1+i:y2-i+1])
            que.extend([B[y2-i] for B in copy_A[x1+i+1:x2-i]])
            que.extend(copy_A[x2-i][y1+i:y2-i+1][::-1])
            que.extend([B[y1+i] for B in copy_A[x1+i+1:x2-i]][::-1])
        
            que.rotate(1)
            
            
            for j in range(y1+i, y2-i+1):
                copy_A[x1+i][j] = que.popleft()
            for j in range(x1+i+1, x2-i):
                copy_A[j][y2-i] = que.popleft()
            for j in range(y2-i, y1+i-1, -1):
                copy_A[x2-i][j] = que.popleft()
            for j in range(x2-i-1, x1+i, -1):
                copy_A[j][y1+i] = que.popleft()
            
    result = 1000000

    for i in copy_A:
        result = min(result, sum(i))
    return result

N, M, K = map(int, input().rstrip().split())
A = [list(map(int ,input().rstrip().split())) for i in range(N)]
command = [list(map(int, input().rstrip().split())) for i in range(K)]
visited = [False for i in range(K)]
answer = 1000000
order = deque()
dfs(0)
print(answer)