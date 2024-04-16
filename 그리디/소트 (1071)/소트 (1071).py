import sys

input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
answer = []
count = [0] * 1003
for i in nums:
    count[i] += 1

tmp = 0
while sum(count) != 0:
    switch = 1
    if count[tmp] and count[tmp+1]:
        for i in range(tmp+2, 1001):
            if count[i]:
                for j in range(count[tmp]):
                    answer.append(tmp)
                count[tmp] = 0
                answer.append(i)
                count[i] -= 1
                switch = 0
                break
        
        if switch:
            for i in range(count[tmp+1]):
                    answer.append(tmp+1)
            count[tmp+1] = 0
            for i in range(count[tmp]):
                    answer.append(tmp)
            count[tmp] = 0
    else:
        for i in range(count[tmp]):
            answer.append(tmp)
        count[tmp] = 0
    tmp+=1

print(*answer)