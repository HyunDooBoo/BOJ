import sys
import heapq as hq

input = sys.stdin.readline

N = int(input())

A = []

for i in range(N):
    x = int(input())

    if x:
        hq.heappush(A, x)
    else:
        if A:
            print(hq.heappop(A))
        else:
            print(0)
