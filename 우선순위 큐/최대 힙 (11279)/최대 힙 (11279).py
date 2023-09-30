import sys
import heapq as hq
input = sys.stdin.readline
N = int(input())
heap = []

for i in range(N):
    x = int(input())
    if x:
        hq.heappush(heap,-x)
    else:
        if heap:
            print(-1*hq.heappop(heap))
        else:
            print(0)
