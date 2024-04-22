import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(x):
    for i in graph[x]:
        if chk[i] == False:
            chk[i] = True
            if visited[i] == -1 or dfs(visited[i]):
                visited[i] = x
                return True
    return False
        

N, M = map(int, input().rstrip().split())
graph = [[] for i in range(N+1)]
answer = 0
visited = [-1] * (M+1)
for i in range(1, N+1):
    nums = list(map(int,(input().rstrip().split())))
    for j in range(1, nums[0]+1):
        graph[i].append(nums[j])

for tmp in range(1, N+1):
    chk = [False] * (M+1)
    if dfs(tmp):
        answer +=1

print(answer)

#======pypy3 통과 코드======
# import sys

# input = sys.stdin.readline

# def dfs(x):
#     if visited[x]:
#         return False
#     visited[x] = True

#     for i in graph[x]:
#         if work[i] == 0 or dfs(work[i]):
#             work[i] = x
#             return True
#     return False
        

# N, M = map(int, input().rstrip().split())
# graph = [[] for i in range(N+1)]
# work = [0] * (M+1)
# answer = 0
# for i in range(1, N+1):
#     nums = list(map(int,(input().rstrip().split())))
#     for j in range(1, nums[0]+1):
#         graph[i].append(nums[j])

# for i in range(1, N+1):
#     visited = [False] * (N+1)
#     dfs(i)

# for i in range(1, len(work)):
#     if work[i]:
#         answer += 1

# print(answer)