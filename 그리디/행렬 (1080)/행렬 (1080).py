import sys

input = sys.stdin.readline

def reverse(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            if A[i][j] == 0:
                A[i][j] = 1
            else:
                A[i][j] = 0

N, M = map(int, input().rstrip().split())
answer = 0
A = []
B = []
for i in range(2*N):
    if i<N:
        A.append(list(map(int, input().rstrip())))
    else:
        B.append(list(map(int, input().rstrip())))
if (M < 3 or N < 3) and A!=B:
    print(-1)
    exit()
else:
    for i in range(N-2):
        for j in range(M-2):
            if A[i][j] != B[i][j]:
                answer += 1
                reverse(i, j)

if A == B:
    print(answer)
else:
    print(-1)