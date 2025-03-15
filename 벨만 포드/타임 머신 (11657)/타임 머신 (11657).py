import sys

input = sys.stdin.readline

def bellman(tmp):
    distance[tmp] = 0
    
    for i in range(1, N+1):
        for j in range(M):
            a, b, cost = bus[j]
            if distance[a] != int(1e9) and distance[b] > distance[a] + cost: #distance[a] != 1000000는 거쳐갔는지 판별
                distance[b] = distance[a] + cost
                #distance[b] = min(distance[b], distance[a] + cost)로 하지 않은 이유는
                #if문에 distance[b] > distance[a] + cost 이 조건을 걸어둬야
                #i == N (조건을 사용 가능하기 때문)
                if i == N:
                    return True
       
    return False

N, M = map(int, input().rstrip().split())
bus = [list(map(int, input().rstrip().split())) for i in range(M)]
distance = [int(1e9)] * (N + 1)
cycle = bellman(1)

if cycle:
    print(-1)
else:
    for i in range(2, N+1):
        if distance[i] == int(1e9):
            print(-1)
        else:
            print(distance[i])