import sys
from copy import deepcopy

input = sys.stdin.readline

N = int(input().rstrip())
place = list(map(int, input().rstrip().split()))
sums = deepcopy(place)
answer = 0

for i in range(1, len(sums)):
    sums[i] = sums[i-1] + sums[i]

for i in range(1, len(place)-1):
    answer = max(answer, 2*sums[-1]-place[0]-place[i]-sums[i])

for i in range(1, len(place)-1):
    answer = max(answer, sums[-1]-place[-1]-place[i]+sums[i-1])

for i in range(1, len(place)-1):
    answer = max(answer, sums[i]-place[0]+sums[-1]-place[-1]-sums[i-1])
print(answer)