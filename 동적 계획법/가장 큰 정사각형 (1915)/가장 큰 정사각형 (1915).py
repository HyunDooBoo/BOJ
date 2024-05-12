import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
maps = [list(map(int, input().rstrip())) for i in range(n)]
for i in range(1,n):
    for j in range(1,m):
        if maps[i][j] == 1:
            maps[i][j] = min(maps[i-1][j-1], maps[i-1][j], maps[i][j-1])+1
answer = 0
for i in maps:
    answer = max(answer, max(i))
print(answer*answer)