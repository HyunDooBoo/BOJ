import sys
from collections import deque

input = sys.stdin.readline

N, M, R = map(int, input().rstrip().split())
A = [list(map(int ,input().rstrip().split())) for i in range(N)]
answer = [[0]*M for _ in range(N)]
cycle = min(N, M)//2

for i in range(cycle):
    que = deque()
    que.extend(A[i][i:M-i])
    que.extend([B[M-i-1] for B in A[i+1:N-i-1]])
    que.extend(A[N-i-1][i:M-i][::-1])
    que.extend([B[i] for B in A[i+1:N-i-1]][::-1])

    que.rotate(-R)
    for j in range(i, M-i):
        answer[i][j] = que.popleft()
    for j in range(i+1, N-i-1):
        answer[j][M-i-1] = que.popleft()
    for j in range(M-i-1, i-1, -1):
        answer[N-i-1][j] = que.popleft()
    for j in range(N-i-2, i, -1):
        answer[j][i] = que.popleft()
for i in answer:
    print(*i)