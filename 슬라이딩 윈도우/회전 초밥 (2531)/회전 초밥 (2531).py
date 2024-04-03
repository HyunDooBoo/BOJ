import sys

input = sys.stdin.readline

N, d, k, c = map(int, input().rstrip().split())
sushi = []
for i in range(N):
    sushi.append(int(input().rstrip()))

answer = 0
for i in range(N):
    sushi_set = set()
    if i <= N-k:
        sushi_set = set(sushi[i:i+k]+[c])
    else:
        sushi_set = set(sushi[i:])
        sushi_set.update(sushi[:(i+k)%N]+[c])
    
    answer = max(answer, len(sushi_set))
print(answer)