import sys

input = sys.stdin.readline

gual = list(input().rstrip())

lis = []
result = 0

for i in range(len(gual)):
    if gual[i] == "(":
        lis.append("(")
    else:
        if gual[i-1] == "(":
            lis.pop()
            result += len(lis)
        else:
            lis.pop()
            result += 1

print(result)
