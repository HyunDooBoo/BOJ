import sys

input = sys.stdin.readline

N = int(input().rstrip())
li = list(map(int, input().rstrip().split()))
li.sort()
answer = 0
for tmp in range(N):
    x = li[tmp]
    left = 0
    right = len(li) - 1
    while left != right:
        if left == tmp:
            left += 1
            continue
        elif right == tmp:
            right -= 1
            continue
        if li[left] + li[right] > x:
            right -= 1
        elif li[left] + li[right] < x:
            left += 1
        else:
            answer += 1
            break
print(answer)