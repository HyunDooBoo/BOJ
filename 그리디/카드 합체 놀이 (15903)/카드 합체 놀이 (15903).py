import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
a = list(map(int, input().rstrip().split()))
heapq.heapify(a)

for i in range(m):
    x = heapq.heappop(a)
    y = heapq.heappop(a)

    heapq.heappush(a, x + y)
    heapq.heappush(a, x + y)

print(sum(a))