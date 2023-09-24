import sys

input = sys.stdin.readline

N, C = map(int, input().rstrip().split())
wifi = [int(input()) for _ in range(N)]
start, end = 1, max(wifi)
wifi.sort()
result = 0

if C == 2:
    print(wifi[-1] - wifi[0])

else:
    while start <= end:

        mid = (start+end) // 2
        count = 1
        minus = wifi[0]
        for i in wifi:
            if i - minus >= mid:
                count += 1
                minus = i
        if count >= C:
            result = mid
            start = mid+1
        else:
            end = mid - 1
    print(result)
