import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
times = []
stack = []
for i in range(N):
    S, T = map(int, input().rstrip().split())
    stack.append([S,T])

stack.sort()
heapq.heappush(times, stack[0][1])

for i in range(1, N):
    if times[0] <= stack[i][0]:
        heapq.heappop(times)
        heapq.heappush(times, stack[i][1])
    else:
        heapq.heappush(times, stack[i][1])
print(len(times))