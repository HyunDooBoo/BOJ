import sys

input = sys.stdin.readline

def cal(a, c, b):
    if c == "+":
        return a + b
    elif c == "*":
        return a * b
    else:
        return a - b
    
def dfs(depth, result):
    global answer

    if depth == N-1:
        answer = max(result, answer)
        return
    
    if depth + 2 < N:
        val1 = cal(result, li[depth+1], int(li[depth+2]))
        dfs(depth+2, val1)
    
    if depth + 4 < N:
        val2 = cal(int(li[depth+2]), li[depth+3], int(li[depth+4]))
        val2 = cal(result, li[depth+1], val2)
        dfs(depth+4, val2)


N = int(input().rstrip())

li = list(map(str, input().rstrip()))
answer = -10000000
dfs(0, int(li[0]))
print(answer)