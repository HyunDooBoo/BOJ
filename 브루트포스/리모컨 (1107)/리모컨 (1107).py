import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
button = [0,1,2,3,4,5,6,7,8,9]
min_count = abs(100-N)
if M>0:
    break_button = [int(num) for num in input().rstrip().split()]
    for i in break_button:
        button.remove(i)
for i in range(1000001):
    num = str(i)
    for j in range(len(num)):
        if int(num[j]) not in button:
            break
        if j == len(num)-1:
            min_count = min(min_count, abs(N-i)+len(num))
print(min_count)