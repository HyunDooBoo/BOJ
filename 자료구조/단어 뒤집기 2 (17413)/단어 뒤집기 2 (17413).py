import sys

input = sys.stdin.readline

S = list(input().rstrip())

chk = 0
start = 0

while chk < len(S):
    if S[chk] == "<":
        chk += 1
        while S[chk] != ">":
            chk += 1
        chk += 1
    elif S[chk].isalnum():
        start = chk
        while chk < len(S) and S[chk].isalnum():
            chk += 1
        tmp = S[start:chk]
        tmp.reverse()
        S[start:chk] = tmp
    else:
        chk += 1
for i in S:
    print(i, end="")
