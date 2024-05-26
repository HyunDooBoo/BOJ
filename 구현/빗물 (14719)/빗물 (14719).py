import sys

input = sys.stdin.readline

H, W = map(int, input().rstrip().split())
maps = list(map(int, input().rstrip().split()))

answer = 0

for i in range(1, W-1):
    left = max(maps[:i])
    right = max(maps[i+1:])
    tmp = min(left, right)
    if tmp > maps[i]:
        answer += tmp - maps[i]

print(answer)