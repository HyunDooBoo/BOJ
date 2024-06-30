import sys

input = sys.stdin.readline

N, M, B = map(int, sys.stdin.readline().split())

maps = []
for _ in range(N):
    maps.append(list(map(int,input().rstrip().split())))

time = [0 for i in range(257)]
answer = 0
for g in range(257):
    
    block = B

    for i in maps:
        for j in i:
            if j <= g:
                time[g] += g - j
                block -= g - j
            else:
                time[g] += 2 * (j - g)
                block += j - g

    if block >= 0 and time[g] <= time[answer]:
        answer = g

print(time[answer], answer)