import sys
from collections import deque

input = sys.stdin.readline

def right_spin(tmp, r):
    if tmp > 3:
        return False
    if tops[tmp][6] != r:
        return True
    return False

def left_spin(tmp, l):
    if tmp < 0:
        return False
    if tops[tmp][2] != l:
        return True
    return False

def spin(tmp, dir):
    if tmp > 3 or tmp < 0:
        return
    r, l = tops[tmp][2], tops[tmp][6]
    tops[tmp].rotate(dir)
    visited[tmp] = True

    if right_spin(tmp+1, r) and visited[tmp+1] == False:
        spin(tmp+1, -dir)

    if left_spin(tmp-1, l) and visited[tmp-1] == False:
        spin(tmp-1, -dir)
    

tops = [deque(list(map(int, input().rstrip()))) for i in range(4)]
answer = 0
K = int(input().rstrip())
command = [list(map(int, input().rstrip().split())) for i in range(K)]
for com in command:
    visited = [False] * 4
    spin(com[0]-1, com[1])

if tops[0][0] == 1:
    answer += 1
if tops[1][0] == 1:
    answer += 2
if tops[2][0] == 1:
    answer += 4
if tops[3][0] == 1:
    answer += 8
print(answer)