from collections import deque
import sys

def bfs(a):
    que = deque()
    que.append((A,""))
    while que:
        num, result = que.popleft()
        visited[num] = True

        if num == B:
            print(result)
            return

        Dnum = (2*num) % 10000
        if not visited[Dnum]:
            que.append((Dnum,result+"D"))
            visited[Dnum] = True

        Snum = (num-1) % 10000
        if not visited[Snum]:
            que.append((Snum,result+"S"))
            visited[Snum] = True
        
        Lnum = (num*10+num//1000)%10000
        if not visited[Lnum]:
            que.append((Lnum,result+"L"))
            visited[Lnum] = True
        
        Rnum = ((num//10) + (num%10*1000))%10000
        if not visited[Rnum]:
            que.append((Rnum,result+"R"))
            visited[Rnum] = True

input = sys.stdin.readline

for i in range(int(input())):
    A,B = map(int,input().split())
    visited = [False] * 10000
    bfs(A)