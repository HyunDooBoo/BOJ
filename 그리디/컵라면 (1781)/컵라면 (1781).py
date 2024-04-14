import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
li = []
cups = []

for i in range(N):
    d, c = map(int,input().rstrip().split())
    li.append([d,c])

li.sort()

for i in range(len(li)):
    heapq.heappush(cups, li[i][1])
    if li[i][0] < len(cups):
        heapq.heappop(cups)
print(sum(cups))