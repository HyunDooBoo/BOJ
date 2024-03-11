import sys
import heapq
input = sys.stdin.readline

n = int(input().rstrip())

if n == 0:
    print(0)
    exit()

lectures = []

for i in range(n):
    p, d = map(int,input().rstrip().split())
    lectures.append([d,p])

lectures.sort()
heap = []

for lecture in lectures:
    heapq.heappush(heap, lecture[1])
    if len(heap) > lecture[0]:
        heapq.heappop(heap)
print(sum(heap))