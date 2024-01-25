import sys

input = sys.stdin.readline

N = int(input().rstrip())
numbers = list(map(int, input().rstrip().split()))
numbers = list(map(str, numbers))
numbers.sort(key = lambda x:x*1000, reverse = True)
answer = ''.join(map(str, numbers))
if answer[0] == '0':
    print(0)
else:
    print(answer)