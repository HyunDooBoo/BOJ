import sys

input = sys.stdin.readline

def dfs(depth):
    if depth == M:
        print(' '.join(map(str, answer)))
        return
    for i in range(N):
        if not visit_check[i]:
            visit_check[i] = True
            answer.append(numbers[i])
            dfs(depth+1)
            answer.pop()
            visit_check[i] = False


N, M = map(int, input().split())

numbers = list(map(int,input().rstrip().split()))
visit_check = [False] * N
numbers.sort()
answer = []
dfs(0)