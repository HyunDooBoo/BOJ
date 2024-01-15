import sys

input = sys.stdin.readline

N = int(input().rstrip())

a = list(map(int, input().rstrip().split()))
sw = 1

for i in range(N-1, 0, -1):
    if a[i-1] > a[i]:
        for j in range(N-1, 0, -1):
            if a[i-1] > a[j]:
                a[i-1], a[j] = a[j], a[i-1]
                a = a[:i] + sorted(a[i:], reverse=True)
                print(' '.join(map(str, a)))
                sw = 0
                break
        break

if sw:
    print(-1)