import sys

input = sys.stdin.readline

N = int(input().rstrip())
K = int(input().rstrip())
pos = list(map(int, input().rstrip().split()))
pos.sort()

dis = []

for i in range(N-1):
    dis.append(pos[i+1]-pos[i])
dis.sort()
if K >= N:
    print(0)
else:
    for i in range(K-1):
        dis.pop()
    print(sum(dis))