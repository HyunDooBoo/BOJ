import sys

input = sys.stdin.readline

def winner(word):
    check = word*3
    if check in [''.join(i) for i in li]:
        return True
    if check in [''.join([row[i] for row in li]) for i in range(3)]:
        return True
    if check in [''.join([li[i][i] for i in range(3)]),
                   ''.join([li[j][abs(j-2)] for j in range(3)])]:
        return True
    return False


def check():
    global x_count
    global o_count

    o_win, x_win = winner('O'), winner('X')

    if x_count == o_count and o_win and not x_win:
        print("valid")
        return
    elif (x_count - 1) == o_count:
        if x_win and not o_win:
            print("valid")
            return
        elif not x_win and not o_win and no_count == 0:
            print("valid")
            return
    print("invalid")


while True:
    case = input().rstrip()
    if case == 'end':
        break
    x_count = case.count('X')
    o_count = case.count('O')
    no_count = case.count('.')
    li = [list(case[i:i+3]) for i in range(0, 7, 3)]
    check()