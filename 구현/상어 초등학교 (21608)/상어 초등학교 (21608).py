import sys

N = int(input().rstrip())
nums = [list(map(int, input().rstrip().split())) for i in range(N**2)]
seats = [[0] * N for i in range(N)]
dx, dy = [-1,1,0,0], [0,0,-1,1]
answer = 0
score = [0, 1, 10, 100, 1000]

for student in nums:
    able = []
    for i in range(N):
        for j in range(N):
            if seats[i][j] == 0:
                love, empty = 0, 0
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0 <= nx < N and 0 <= ny < N:
                        if seats[nx][ny] in student[1:]:
                            love += 1
                        if seats[nx][ny] == 0:
                            empty += 1
                able.append((i,j,love,empty))
    able.sort(key = lambda x:(-x[2],-x[3],x[0],x[1]))
    seats[able[0][0]][able[0][1]] = student[0]
nums.sort()
for i in range(N):
    for j in range(N):
        count = 0
        for k in range(4):
            nx, ny = i + dx[k], j + dy[k]
            if 0 <= nx < N and 0 <= ny < N:
                if seats[nx][ny] in nums[seats[i][j] - 1][1:]:
                    count += 1
        answer += score[count]
print(answer)