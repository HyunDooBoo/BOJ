import sys

input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())
sw = 0
while T:
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T.reverse()
    if S == T:
        sw = 1
        break

if sw:
    print(1)
else:
    print(0)