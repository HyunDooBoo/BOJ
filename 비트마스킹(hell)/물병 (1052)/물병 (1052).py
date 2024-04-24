import sys

input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

answer = 0

while bin(N).count('1') >  K:
    N += 1
    answer += 1
print(answer)