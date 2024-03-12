import sys

input = sys.stdin.readline

def find():
    end = int(N**(0.5))
    for i in range(2, end+1):
        if sosoo[i] == False:
            continue
        for j in range(i*i, N+1, i):
            sosoo[j] = False
    for i in range(len(sosoo)):
        if sosoo[i] == True:
            prime_num.append(i)

N = int(input().rstrip())
sosoo = [True] * (N+1)
sosoo[0], sosoo[1] = False, False
prime_num = []
find()
answer = 0
start = 0
end = 0
sum_prime_num = 0
while start <= end:
    sum_prime_num = sum(prime_num[start:end])
    if sum_prime_num == N:
        answer += 1
        start += 1
    elif sum_prime_num < N:
        end += 1
    else:
        start += 1
    if end > len(prime_num):
        break
print(answer)