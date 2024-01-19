import sys

input = sys.stdin.readline

def check(arr):
    v_count, c_count = 0, 0

    for i in arr:
        if i in check_li:
            v_count += 1
        else:
            c_count += 1

    if v_count >= 1 and c_count >= 2:
        return True
    else:
        return False

def dfs(start):
    if len(answer) == L:
        if check(answer):
            print(''.join(map(str, answer)))
        return
    for i in range(start, C):
        if visited[i] == False:
            answer.append(word[i])
            visited[i] = True
            dfs(i)
            answer.pop()
            visited[i] = False

L, C = map(int, input().rstrip().split())
word = list(map(str, input().rstrip().split()))
check_li = ['a', 'e', 'i', 'o', 'u']
word.sort()
answer = []
visited = [False] * C
for i in range(C):
    visited[i] = True
    answer.append(word[i])
    dfs(i)
    answer.pop()
    visited[i] = False