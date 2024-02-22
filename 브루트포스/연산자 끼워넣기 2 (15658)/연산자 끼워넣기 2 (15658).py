import sys

input = sys.stdin.readline

def dfs(plus, minus, mul, div, result, depth):

    global max_num
    global min_num

    if depth == N:
        max_num = max(result, max_num)
        min_num = min(result, min_num)
        return

    if plus:
        dfs(plus-1, minus, mul, div, result+num_li[depth], depth + 1)
    if minus:
        dfs(plus, minus-1, mul, div, result-num_li[depth], depth + 1)
    if mul:
        dfs(plus, minus, mul-1, div, result*num_li[depth], depth + 1)
    if div:
        dfs(plus, minus, mul, div-1, int(result/num_li[depth]), depth + 1)

N = int(input().rstrip())
max_num= -1000000000
min_num = 1000000000
num_li = list(map(int,input().rstrip().split()))
calcul = list(map(int,input().rstrip().split()))
dfs(calcul[0],calcul[1],calcul[2],calcul[3],num_li[0],1)
print(max_num)
print(min_num)