import sys

input = sys.stdin.readline

N, S = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))
answer = 100000
sum = nums[0]
r, l = 0, 0
while True:
    if sum >= S:
        answer = min(answer, abs(r-l)+1)
        sum -= nums[l]
        l += 1
    else:
        r += 1
        if r == N:
            break
        sum += nums[r]

if answer == 100000:
    print(0)
    exit()
print(answer)