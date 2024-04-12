import sys

input = sys.stdin.readline

N = int(input().rstrip())
W = list(map(int, input().rstrip().split()))
W.sort()
tmp = 1

for i in W:
    if tmp < i:
        break
    tmp += i
print(tmp)