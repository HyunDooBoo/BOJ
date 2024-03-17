import sys

input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
max_num = max(nums)
num_set = set(nums)
num_dic = {}
for i in nums:
    num_dic[i] = 0

for i in nums:
    for j in range(i*2, max_num+1, i):
        if j in num_set:
            num_dic[j] -= 1
            num_dic[i] += 1
for i in nums:
    print(num_dic[i],end=" ")