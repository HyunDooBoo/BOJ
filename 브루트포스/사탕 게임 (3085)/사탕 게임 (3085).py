import sys

input = sys.stdin.readline

def check(array):
    ans = 1
    for i in range(len(array)):
        count = 1
        for j in range(1, len(array)):
            if array[i][j] == array[i][j-1]:
                count += 1
            else:
                count = 1
            ans = max(ans, count)
        
        count = 1    
        for j in range(1,len(array)):
            if array[j][i] == array[j-1][i]:
                count += 1
            else:
                count = 1
            ans = max(ans, count)
            
    return ans
            
N = int(input())
candy = []
ans = 0

for i in range(N):
    candy.append(list(input().rstrip()))

for i in range(N):
    for j in range(N):
        if j+1 < N:
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            cnt = check(candy)
            ans = max(cnt, ans)
            candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
            
        if i+1 < N:
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
            cnt = check(candy)
            ans = max(cnt, ans)
            candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
print(ans)
