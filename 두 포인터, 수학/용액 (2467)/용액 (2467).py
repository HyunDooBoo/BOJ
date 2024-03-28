import sys

input = sys.stdin.readline
N = int(input().rstrip())
li = list(map(int,input().rstrip().split()))
start = 0
end = len(li)-1
answer = abs(li[start] + li[end])
ans_r = li[end]
ans_l = li[start]
while start != end:
    if abs(li[start]+li[end]) <= answer:
        ans_r = li[end]
        ans_l = li[start]
        answer = abs(li[start]+li[end])
    if li[start]+li[end] < 0:
        start += 1
    else:
        end -= 1
print(ans_l, ans_r)