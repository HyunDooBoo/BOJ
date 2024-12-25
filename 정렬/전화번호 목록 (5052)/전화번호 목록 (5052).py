import sys

input = sys.stdin.readline

t = int(input().rstrip())

for test_case in range(t):
    n = int(input().rstrip())
    number = [input().rstrip() for _ in range(n)]
    number.sort()
    answer = "YES"
    for i in range(len(number)-1):
        if number[i] == number[i+1][:len(number[i])]:
            answer = "NO"
    print(answer)
