import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
num = str(input().rstrip())
nums = []
tmp = K
for i in num:
    while nums and nums[-1] < i and tmp > 0:
        nums.pop()
        tmp -= 1
    nums.append(i)
print(''.join(nums[:N-K]))