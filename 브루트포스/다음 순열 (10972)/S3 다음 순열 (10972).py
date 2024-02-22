import sys

input = sys.stdin.readline

N = int(input().rstrip())
a = list(map(int, input().rstrip().split()))
sc = 1

for i in range(N-1, 0, -1):
    if a[i-1] < a[i]:
        sc = 0
        for j in range(N-1, 0, -1):
            if a[i-1] < a[j]:
                a[i-1], a[j] = a[j], a[i-1]
                a = a[:i] + sorted(a[i:])
                print(' '.join(map(str, a)))
                break
        break

if sc:
    print(-1)