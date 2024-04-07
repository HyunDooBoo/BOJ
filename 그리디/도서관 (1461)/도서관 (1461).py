import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
book_pos = list(map(int, input().rstrip().split()))
book_pos.sort()
minus = []
plus = []
dis = []
answer = 0
pos = 0
for i in book_pos:
    if i < 0:
        minus.append(i)
    else:
        plus.append(i)
plus.reverse()
for i in range(0, len(minus), M):
    dis.append(abs(minus[i]))
for i in range(0, len(plus), M):
    dis.append(plus[i])
dis.sort()

answer = dis.pop()
answer += 2*sum(dis)

print(answer)