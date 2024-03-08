import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    que = deque()
    que.append((s, ''))
    while que:
        n, cal = que.popleft()
        if n == t:
            print(cal)
            return
        for i in range(4):
            if calc[i] == '*' and n > 1 and n*n <= t and n*n not in visited:
                que.append((n*n, cal+'*'))
                visited.add(n*n)

            if calc[i] == '+' and n != 0 and n+n <= t and n+n not in visited:
                que.append((n+n, cal+'+'))
                visited.add(n+n)
            if calc[i] == '-' and n != 0 and n-n not in visited:
                que.append((n-n, cal+'-'))
                visited.add(n-n)

            if calc[i] == '/' and n != 0 and n//n not in visited:
                que.append((n//n, cal+'/'))
                visited.add(n//n)
    print(-1)

s, t = map(int,input().rstrip().split())
visited = set()
calc = ['*', '+', '-', '/']
if s == t:
    print(0)
else:
    bfs()