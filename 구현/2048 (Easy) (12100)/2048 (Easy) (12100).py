import sys
import copy

input = sys.stdin.readline

def up_move(table):
    for i in range(N):
        tmp = 0
        for j in range(1, N):
            if table[j][i] != 0:
                num = table[j][i]
                table[j][i] = 0

                if table[tmp][i] == 0:
                    table[tmp][i] = num
                
                elif table[tmp][i] == num:
                    table[tmp][i] += num
                    tmp += 1
                
                else:
                    tmp += 1
                    table[tmp][i] = num
    return table

def down_move(table):
    for i in range(N):
        tmp = N-1
        for j in range(N-2, -1, -1):
            if table[j][i] != 0:
                num = table[j][i]
                table[j][i] = 0

                if table[tmp][i] == 0:
                    table[tmp][i] = num
                
                elif table[tmp][i] == num:
                    table[tmp][i] += num
                    tmp -= 1
                
                else:
                    tmp -= 1
                    table[tmp][i] = num
    return table

def left_move(table):
    for i in range(N):
        tmp = 0
        for j in range(1, N):
            if table[i][j] != 0:
                num = table[i][j]
                table[i][j] = 0

                if table[i][tmp] == 0:
                    table[i][tmp] = num
                
                elif table[i][tmp] == num:
                    table[i][tmp] += num
                    tmp += 1
                
                else:
                    tmp += 1
                    table[i][tmp] = num
    return table

def right_move(table):
    for i in range(N):
        tmp = N-1
        for j in range(N-2, -1, -1):
            if table[i][j] != 0:
                num = table[i][j]
                table[i][j] = 0

                if table[i][tmp] == 0:
                    table[i][tmp] = num
                
                elif table[i][tmp] == num:
                    table[i][tmp] += num
                    tmp -= 1
                
                else:
                    tmp -= 1
                    table[i][tmp] = num
    return table

def dfs(cnt, game_table):
    global answer

    if cnt == 5:
        for i in range(N):
            for j in range(N):
                answer = max(game_table[i][j], answer)
        return
    
    for i in range(4):
        cgt = copy.deepcopy(game_table)
        if i == 0:
            dfs(cnt+1, up_move(cgt))
        elif i == 1:
            dfs(cnt+1, down_move(cgt))
        elif i == 2:
            dfs(cnt+1, left_move(cgt))
        else:
            dfs(cnt+1, right_move(cgt))

N = int(input().rstrip())
answer = 0
board = [list(map(int, input().rstrip().split())) for i in range(N)]

dfs(0, board)
print(answer)