import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    que = deque()
    que.append((1,0,0))
    while que:
        a, b, cnt = que.popleft()
        if a==S:
            print(cnt)
            break
        if emozi[a][a] == -1:
            emozi[a][a] = emozi[a][b] + 1
            que.append((a,a,cnt+1))
        if a+b <= S and emozi[a+b][b] == -1:
            emozi[a+b][b] = emozi[a][b] + 1
            que.append((a+b,b,cnt+1))
        if a-1 >= 0 and emozi[a-1][b] == -1:
            emozi[a-1][b] = emozi[a][b] + 1
            que.append((a-1,b,cnt+1))

answer = 0
S = int(input().rstrip())
emozi = [[-1] * (S+1) for i in range(S+1)]
emozi[1][0] = 0
bfs()