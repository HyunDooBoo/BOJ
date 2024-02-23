import sys

input = sys.stdin.readline

def dfs(idx, cnt):
    global answer

    if cnt == K - 5:
        answer = max(answer, check_word())
        return

    for i in range(idx, len(learn)):
        if not learn[i]:
            learn[i] = True
            dfs(i, cnt + 1)
            learn[i] = False

def check_word():
    cnt = 0
    for word in words:
        switch = 1
        for w in word:
            if not learn[ord(w) - ord('a')]:
                switch = 0
                break
        if switch:
            cnt += 1
    return cnt


N, K = map(int, input().split())

default = ['a', 'n', 't', 'i', 'c']
answer = 0
words = set()
for i in range(N):
    words.add(input().rstrip())
learn = [0] * 26

for i in default:
    learn[ord(i) - ord('a')] = 1

if K < 5:
    print(0)
else:
    dfs(0, 0)
    print(answer)