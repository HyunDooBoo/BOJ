import sys

input = sys.stdin.readline

K, N = map(int, input().rstrip().split())
nums = []
max_num = 0
answer = ''

for i in range(K):
    num = input().rstrip()
    nums.append(num)
    max_num = max(max_num, int(num))

for i in range(N-K):
    nums.append(str(max_num))

nums.sort(key=lambda x:x*10, reverse=True)

print(int(''.join(nums)))
