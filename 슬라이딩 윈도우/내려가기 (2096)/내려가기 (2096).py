import sys

input = sys.stdin.readline
N = int(input().rstrip())
nums = list(map(int,input().rstrip().split()))
max_nums = [nums[0], nums[1], nums[2]]
min_nums = [nums[0], nums[1], nums[2]]
for i in range(N-1):
    nums = list(map(int,input().rstrip().split()))
    max_nums = [nums[0]+max(max_nums[0],max_nums[1]), nums[1]+max(max_nums), nums[2]+max(max_nums[1],max_nums[2])]
    min_nums = [nums[0]+min(min_nums[0],min_nums[1]), nums[1]+min(min_nums), nums[2]+min(min_nums[1],min_nums[2])]
print(max(max_nums), min(min_nums))


# 메모리 초과 코드
# for i in range(N):
#     nums.append(list(map(int, input().rstrip().split())))
# max_num = copy.deepcopy(nums)
# min_num = copy.deepcopy(nums)

# for i in range(1, N):
#     max_num[i][0] += max(max_num[i-1][0], max_num[i-1][1])
#     max_num[i][1] += max(max_num[i-1][0], max_num[i-1][2])
#     max_num[i][2] += max(max_num[i-1][2], max_num[i-1][1])
    
#     min_num[i][0] += min(min_num[i-1][0], min_num[i-1][1])
#     min_num[i][1] += min(min_num[i-1][0], min_num[i-1][2])
#     min_num[i][2] += min(min_num[i-1][2], min_num[i-1][1])
# print(max(max_num[N-1]), min(min_num[N-1]))