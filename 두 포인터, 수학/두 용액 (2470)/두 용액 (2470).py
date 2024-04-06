import sys

input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
nums.sort()
start = 0
end = N-1
min_num = nums[start]
max_num = nums[end]
ans = 2000000000

while start != end:
    if abs(nums[start] + nums[end]) <= ans:
        min_num, max_num = nums[start], nums[end]
        ans = abs(nums[start] + nums[end])
    if nums[start]+nums[end] < 0:
        start += 1
    else:
        end -= 1
print(min_num, max_num)