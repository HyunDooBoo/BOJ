import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().rstrip().split()))
M = int(input())
B = list(map(int, input().rstrip().split()))

def binary_search(array, target, start, end):
    if start > end:
        return 0
    mid = (start+end)//2

    if array[mid]==target:
        return 1
    elif array[mid]>target:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

A.sort()
for i in B:
    print(binary_search(A, i, 0, len(A)-1))
