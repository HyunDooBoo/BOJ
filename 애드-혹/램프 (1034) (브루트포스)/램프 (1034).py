import sys

input = sys.stdin.readline

N, M = map(int,input().rstrip().split())
lamp = []
can = []
answer = 0
for i in range(N):
    lamp.append(list(map(int,input().rstrip())))
a = int(input().rstrip())
for i in range(N):
    zero = 0
    for j in range(M):
        if lamp[i][j] == 0:
            zero += 1
    if zero <= a and (a-zero)%2==0:
        can.append(i)
for i in can:
    cnt = 0
    for j in range(N):
        if lamp[i] == lamp[j]:
            cnt += 1
    answer = max(answer, cnt)
print(answer)