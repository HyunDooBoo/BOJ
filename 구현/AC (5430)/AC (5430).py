import sys
from collections import deque

input = sys.stdin.readline

T = int(input().rstrip())
for i in range(T):
    p = list(input().rstrip())
    n = int(input().rstrip())
    a = input().rstrip()
    nums = a[1:-1]
    switch = 1
    rev = 0
    que = deque()
    for num in nums.split(','):
        que.append(num)
    if n == 0:
        que = []
    for command in p:
        if command == 'R':
            rev += 1
        elif command == 'D':
            if len(que) < 1:
                print('error')
                switch = 0
                break
            else:
                if rev % 2 == 0:
                    que.popleft()
                else:
                    que.pop()
    if switch:
        if rev % 2 == 0:
            print("[" + ",".join(que) + "]")
        else:
            que.reverse()
            print("[" + ",".join(que) + "]")
    else:
        continue