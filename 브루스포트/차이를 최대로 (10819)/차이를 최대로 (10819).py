import sys

input = sys.stdin.readline
N = int(input().rstrip())
a = list(map(int, input().rstrip().split()))
num_list = []
visited = [False] * N
answer = 0

def dfs():
    global answer
    if len(num_list) == N:
        answer_check = 0
        for i in range(N-1):
            answer_check += abs(num_list[i] - num_list[i+1])
        if answer_check > answer:
                answer = answer_check
        return
    for i in range(N):
        if visited[i] != True:
            visited[i] = True
            num_list.append(a[i])
            dfs()
            visited[i] = False
            num_list.pop()

dfs()
print(answer)