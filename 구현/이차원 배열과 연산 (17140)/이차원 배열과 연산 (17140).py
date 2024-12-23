import sys

input = sys.stdin.readline
def sorting(li, command):
    sort_li = []
    count = 0
    for i in range(len(li)):
        B = []
        dic = dict()
        for j in range(len(li[i])):
            if li[i][j] != 0:
                if li[i][j] not in dic:
                    dic[li[i][j]] = 1
                else:
                    dic[li[i][j]] += 1
        for key, value in dic.items():
            B.append([key,value])
        B.sort(key = lambda x: [x[1], x[0]])
        C = sum(B, []) #중요
        count = max(count, len(C))
        sort_li.append(C)
    for i in sort_li:
        i += [0] * (count - len(i))
        if len(i) > 100:
            i = i[:100]
    if command == "R":
        return sort_li
    else:
        return list(zip(*sort_li))
        

r, c, k = map(int, input().rstrip().split())
A = [list(map(int, input().rstrip().split())) for i in range(3)]
answer = 0
while True:
    if answer > 100:
        print(-1)
        break
    if r-1<len(A) and c-1<len(A[0]):
        if A[r-1][c-1] == k:
            print(answer)
            break
    if len(A) >= len(A[0]):
        A = sorting(A, "R")
    else:
        A = sorting(list(zip(*A)), "C")
    answer += 1