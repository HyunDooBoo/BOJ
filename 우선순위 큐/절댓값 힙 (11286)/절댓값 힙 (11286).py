import sys
import heapq as hq

input = sys.stdin.readline

N = int(input())

A = []

for i in range(N):
    x = int(input())

    if x:
        hq.heappush(A, (abs(x),x))
    else:
        if A:
            print(hq.heappop(A)[1])
        else:
            print(0)
