import sys

input = sys.stdin.readline

word = input().rstrip()
if word == word[0] * len(word):
    print(-1)
elif word[:] == word[::-1]:
    print(len(word)-1)
else:
    print(len(word))