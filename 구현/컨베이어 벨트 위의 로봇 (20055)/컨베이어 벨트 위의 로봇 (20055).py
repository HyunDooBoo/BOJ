import sys
from collections import deque

input = sys.stdin.readline

def move_check(x):
    if box_status[x] and durability[x+1] > 0 and box_status[x+1] == 0:
        return True
    return False

N, K = map(int, input().rstrip().split())
durability = deque(list(map(int, input().rstrip().split())))
box_status = deque([0] * N)
zero = 0
answer = 0

while True:
    answer += 1
    
    durability.rotate(1)
    box_status.rotate(1)
    box_status[N-1] = 0

    for i in range(N-2, -1, -1):
        if move_check(i):
            box_status[i], box_status[i+1] = 0, 1
            durability[i+1] -= 1
    box_status[N-1] = 0

    if durability[0] > 0:
        box_status[0] = 1
        durability[0] -= 1
    
    if durability.count(0) >= K:
        break

print(answer)