import sys

input = sys.stdin.readline

def calculate(m,n,x,y):
    a = x
    while a <= m*n:
        if (a-x)%m == 0 and (a-y)%n==0:
            return a
        a += m
    return -1
T = int(input())

for i in range(T):
    M, N, x, y = map(int, input().split())
    print(calculate(M,N,x,y))