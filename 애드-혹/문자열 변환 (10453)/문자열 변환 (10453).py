import sys

input = sys.stdin.readline

def find_a(li):
    idx = []
    for i in range(len(li)):
        if li[i] == 'a':
            idx.append(i)
    return idx

T = int(input().rstrip())
for i in range(T):
    word = list(map(str, input().rstrip().split(' ')))
    A, B = list(word[0]), list(word[1])
    count = 0
    A_idx = find_a(A)
    B_idx = find_a(B)
    for i in range(len(A_idx)):
        count += abs(A_idx[i]-B_idx[i])
    print(count)