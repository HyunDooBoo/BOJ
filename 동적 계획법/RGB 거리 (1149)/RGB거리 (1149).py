import sys

input = sys.stdin.readline

N = int(input())
rgb = []

for i in range(N):
    R, G, B = map(int,input().rstrip().split())
    rgb.append([R,G,B])

for i in range(1, N):
    rgb[i][0] += min(rgb[i-1][1], rgb[i-1][2])
    rgb[i][1] += min(rgb[i-1][0], rgb[i-1][2])
    rgb[i][2] += min(rgb[i-1][0], rgb[i-1][1])

print(min(rgb[-1]))
