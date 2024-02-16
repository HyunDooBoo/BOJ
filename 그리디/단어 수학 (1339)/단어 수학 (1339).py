import sys

input = sys.stdin.readline

N = int(input().rstrip())
dict ={}
words = []
for i in range(N):
    word = list(map(str,input().rstrip()))
    words.append(word)

for i in range(len(words)):
    for j in range(len(words[i])):
        if words[i][j] in dict:
            dict[words[i][j]] += 10 ** (len(words[i]) - j - 1)
        else:
            dict[words[i][j]] = 10 ** (len(words[i]) - j - 1)

dict = sorted(dict.items(), key = lambda x: x[1], reverse = True)

num = 9
answer = 0
for i in dict:
    if i[1] == 0:
        break
    answer += i[1] * num
    num -= 1
print(answer)