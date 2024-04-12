import sys
import heapq
input = sys.stdin.readline

N = int(input().rstrip())
cards = []
for i in range(N):
    heapq.heappush(cards,int(input().rstrip()))
answer = 0

for i in range(N-1):
    tmp = heapq.heappop(cards) + heapq.heappop(cards)
    answer += tmp
    heapq.heappush(cards,tmp)
print(answer)