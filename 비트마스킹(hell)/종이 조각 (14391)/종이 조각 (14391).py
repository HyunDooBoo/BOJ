import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

paper = []
for _ in range(N):
    paper.append(list(map(int, input().rstrip())))

answer = []

for i in range(1 << N * M):
    total = 0

    for row in range(N):
        row_sum = 0
        for col in range(M):
            index = row * M + col
            if i & (1 << index) != 0:
                row_sum = row_sum * 10 + paper[row][col]
            else:
                total += row_sum
                row_sum = 0
        total += row_sum

    for col in range(M):
        col_sum = 0
        for row in range(N):
            index = row*M+col
            if i & (1 << index) == 0:
                col_sum = col_sum * 10 + paper[row][col]
            else:
                total += col_sum
                col_sum = 0
        total += col_sum
    answer.append(total)

print(max(answer))