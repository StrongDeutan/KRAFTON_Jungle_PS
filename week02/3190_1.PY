import sys
import queue

def print_board(board: list, n):
    for j in range(n):
        for p in range(n):
            print(board[j][p], end=" ")
        print()
    print()

def change_move(move: list, m: str):
    if(m == 'L'):
        if(move[0] == 0):
            if(move[1] == 1):
                move[0] = -1
                move[1] = 0
                return
            else:
                move[0] = 1
                move[1] = 0
                return
        else:
            if(move[0] == 1):
                move[1] = 1
                move[0] = 0
                return
            else:
                move[1] = -1
                move[0] = 0
                return
    else:
        if(move[0] == 0):
            if(move[1] == 1):
                move[0] = 1
                move[1] = 0
                return
            else:
                move[0] = -1
                move[1] = 0
                return
        else:
            if(move[0] == 1):
                move[1] = -1
                move[0] = 0
                return
            else:
                move[1] = 1
                move[0] = 0
                return



n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
board = [[0] * n for i in range(n)]
apple = [[0] * n for i in range(n)]

q = queue.Queue()

for i in range(k):
    x, y = map(int, sys.stdin.readline().split())
    apple[x - 1][y - 1] = 1

L = int(sys.stdin.readline())

move = [0, 1]

timer = []

for i in range(L):
    t, m = sys.stdin.readline().split()
    t = int(t)
    timer.append([t, m])
timer.append([100000, "X"])
head_x, head_y = 0, 0
tail_x, tail_y = 0, 0
q = queue.Queue()

board[0][0] = 1
count = 0
idx = 0
while True:
    #print_board(board, n)
    head_x += move[0]
    head_y += move[1]
    count += 1
    #print(head_x, head_y)
    if(head_x < 0 or head_y < 0 or head_y >= n or head_x >= n or board[head_x][head_y] == 1):
        print(f"{count}")
        break
    q.put([head_x, head_y])
    board[head_x][head_y] = 1
    
    if(timer[idx][0] == count):
        change_move(move, timer[idx][1])
        idx += 1
    
    if(apple[head_x][head_y] == 0):
        board[tail_x][tail_y] = 0
        tail = q.get()
        tail_x = tail[0]
        tail_y = tail[1]
    else:
        apple[head_x][head_y] = 0
    

                
