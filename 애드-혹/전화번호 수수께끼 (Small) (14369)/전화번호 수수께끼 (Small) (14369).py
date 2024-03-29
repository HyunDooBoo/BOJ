import sys

input = sys.stdin.readline
alphabet = "ZWUXGHFOVI"
T = int(input().rstrip())
for i in range(T):
    S = input().rstrip()
    word = {0:"Z", 2:"W", 4:"U", 6:"X", 8:"G", 3:"H", 5:"F", 1:"O", 7:"V", 9:"I"}
    word = {v:k for k,v in word.items()}
    nums = {}
    for j in alphabet:
        nums[word[j]] = S.count(j)
    nums[3] -= nums[8]
    nums[5] -= nums[4]
    nums[1] -= nums[0] + nums[2] + nums[4]
    nums[7] -= nums[5]
    nums[9] -= nums[6] + nums[8] + nums[5]
    nums = sorted(nums.items(), key=lambda item: item[0])
    print(f"Case #{i+1}: {''.join(str(num[0]) * num[1] for num in nums)}")