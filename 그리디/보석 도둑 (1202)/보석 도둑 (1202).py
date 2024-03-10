import sys
import heapq

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
gems = []
bags = []
for i in range(N):
    gems.append(list(map(int, input().rstrip().split())))
for i in range(K):
    bags.append(int(input().rstrip()))

gems.sort()
bags.sort()
heap = []
answer = 0

for bag in bags:
    while gems and gems[0][0] <= bag:
        heapq.heappush(heap, -gems[0][1])
        heapq.heappop(gems)
    if heap:
        answer -= heapq.heappop(heap)
print(answer)