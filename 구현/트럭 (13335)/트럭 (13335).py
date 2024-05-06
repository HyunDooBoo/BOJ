import sys

input = sys.stdin.readline

n, w, L = map(int, input().rstrip().split())
truck = list(map(int, input().rstrip().split()))
bridge = [0] * (w)
tmp = 0
answer = 0
while bridge:
    answer += 1
    tmp -= bridge.pop(0)
    if truck:
        if tmp+truck[0] <= L:
            bridge.append(truck.pop(0))
            tmp = sum(bridge)
        else:
            bridge.append(0)
print(answer)