import sys
from collections import deque
sys.setrecursionlimit(5000)

def cycle(start, idx, cnt, li):
    global cycle_can
    if start == idx and cnt >= 3:
        cycle_can = True
        for i in li:
            cycle_list.add(i)
        return
    visited[idx] = True
    for i in station[idx]:
        if visited[i] == False:
            cycle(start, i, cnt+1, li + [i])
        elif i == start and cnt >= 3:
            cycle(start, i, cnt, li)
    visited[idx] = False
    return

def distance():

    que = deque()
    for i in cycle_list:
        que.append((i, 0))
        answer[i] = 0

    while que:
        now, depth = que.popleft()
        for i in station[now]:
            if answer[i] == -1:
                que.append((i, depth+1))
                answer[i] = depth+ 1
    print(*answer[1:])

N = int(input().rstrip())
station = [[] for i in range(N+1)]
cycle_list = set()
answer = [-1] * (N+1)
visited = [False] * (N+1)
cycle_can = False
for i in range(N):
    a, b = map(int, input().rstrip().split())
    station[a].append(b)
    station[b].append(a)
for i in range(1,N+1):
    if cycle_can:
        break
    visited[i] = True
    cycle(i,i,1,[i])
    visited[i] = False
cycle_list = list(cycle_list)
distance()