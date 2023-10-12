import sys

input = sys.stdin.readline

n = int(input())

tri = [[int(input())]]

for i in range(n-1):
    a = list(map(int,input().rstrip().split()))
    tri.append(a)

for i in range(1, n):
    for j in range(len(tri[i])):
        if j == 0:
            tri[i][j] += tri[i-1][j]
        elif j==len(tri[i])-1:
            tri[i][j] += tri[i-1][j-1]
        else:
            tri[i][j] += max(tri[i-1][j], tri[i-1][j-1])
            
print(max(tri[n-1]))
