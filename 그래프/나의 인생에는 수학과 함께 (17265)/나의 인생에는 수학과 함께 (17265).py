import sys

input = sys.stdin.readline

def cal():
    cal_result = int(result[0])
    for i in range(1,len(result),2):
        op = result[i]
        if op == '+':
            cal_result += int(result[i + 1])
        elif op == '-':
            cal_result -= int(result[i + 1])
        elif op == '*':
            cal_result *= int(result[i + 1])
    return cal_result
        

def dfs(x, y):
    global max_answer
    global min_answer

    if x == N-1 and y == N-1:
        max_answer = max(cal(), max_answer)
        min_answer = min(cal(), min_answer)
        return
    
    for i in range(2):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<N:
            result.append(maps[nx][ny])
            dfs(nx,ny,)
            result.pop()

N = int(input().rstrip())
dx = [1,0]
dy = [0,1]
max_answer = -(5**5)
min_answer = 5**5
maps = []
result = []
for i in range(N):
    maps.append(list(map(str, input().rstrip().split())))
result.append(maps[0][0])
dfs(0,0)
print(max_answer, min_answer)