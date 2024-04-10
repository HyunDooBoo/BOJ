import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip())
li = []
max_day = 0
for i in range(N):
    d, w = map(int,input().rstrip().split())
    heapq.heappush(li,(-w, d))
    max_day = max(max_day, d)

schedule = [0 for i in range(max_day+1)]
while li:
    score, day = heapq.heappop(li)
    score = -score
    for i in range(day, 0, -1):
        if schedule[i]:
            continue
        schedule[i] = score
        break
print(sum(schedule))