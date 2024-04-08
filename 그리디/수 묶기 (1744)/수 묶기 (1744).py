import sys

input = sys.stdin.readline

N = int(input().rstrip())
n_li = []
for i in range(N):
    n_li.append(int(input().rstrip()))

minus = []
plus = []

for i in n_li:
    if i <= 0:
        minus.append(i)
    else:
        plus.append(i)

plus.sort(reverse=True)
minus.sort()

nums = []

for i in range(0, len(minus), 2):
    if i+1 < len(minus):
        nums.append(minus[i]*minus[i+1])
    else:
        nums.append(minus[i])

while True:
    if len(plus)>0:
        if plus[-1] == 1:
            nums.append(plus.pop())
        else:
            break
    else:
        break

for i in range(0, len(plus), 2):
    if i+1 < len(plus):
        nums.append(plus[i]*plus[i+1])
    else:
        nums.append(plus[i])

print(sum(nums))