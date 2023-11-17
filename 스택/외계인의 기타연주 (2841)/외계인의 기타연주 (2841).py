import sys

input = sys.stdin.readline

N, P = map(int, input().rstrip().split())
plat = [[] for i in range(7)]
count = 0

for i in range(N):
    a, b = map(int, input().rstrip().split())
    if not plat[a]:
        plat[a].append(b)
        count += 1
    else:
        while plat[a] and b < plat[a][-1]:
            plat[a].pop()
            count += 1
        if b > plat[a][-1]:
            plat[a].append(b)
            count += 1
        else:
            pass
print(count)