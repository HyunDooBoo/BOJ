import sys

input = sys.stdin.readline

N, M, L, K = map(int, input().rstrip().split())
stars = [list(map(int, input().rstrip().split())) for i in range(K)]
answer = 0
for x in stars:
    for y in stars:
        count = 0
        for star in stars:
            if x[0] <= star[0] <= x[0] + L and y[1] <= star[1] <= y[1] + L:
                count += 1
        answer = max(count, answer)
print(K - answer)