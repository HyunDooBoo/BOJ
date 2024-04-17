import sys

input = sys.stdin.readline

def swap(x,y):
    tmp = heap[x]
    heap[x] = heap[y]
    heap[y] = tmp

N = int(input().rstrip())
heap = [0, 1]

for i in range(2, N+1):
    heap.append(i)
    swap(i, i-1)
    tmp = i-1
    while tmp > 1:
        swap(tmp, tmp//2)
        tmp = tmp//2

for i in range(1, N+1):
    print(heap[i], end =' ')