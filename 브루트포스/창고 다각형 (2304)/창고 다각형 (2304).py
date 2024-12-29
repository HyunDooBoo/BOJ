import sys

N = int(input().rstrip())
li = [list(map(int, input().rstrip().split())) for i in range(N)]
li.sort()
top = 0
tmp = 0
for i in range(N):
    if tmp < li[i][1]:
        tmp = li[i][1]
        top = i
tmp = li[0][1]
answer = li[top][1]
for i in range(0, top):
    if tmp < li[i+1][1]:
        answer += tmp * (li[i+1][0] - li[i][0])
        tmp = li[i+1][1]
    else:
        answer += tmp * (li[i+1][0] - li[i][0])
    

tmp = li[-1][1]
for i in range(N-1, top, -1):
    if tmp < li[i-1][1]:
        answer += tmp * (li[i][0] - li[i-1][0])
        tmp = li[i-1][1]
    else:
        answer += tmp * (li[i][0] - li[i-1][0])
print(answer)