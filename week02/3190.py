import sys
import queue

#go to 3190_1.PY


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




count = 0
check = True
head_x = 0
head_y = 0
tail_x = 0 
tail_y = 0
prev = 0
for i in range(L):
    t, m = sys.stdin.readline().split()
    t = int(t)
    timer = t - prev
    prev = t
    
    if(check):
        for k in range(timer):
            
            if(head_x < 0 or head_y < 0 or head_y >= n or head_x >= n or board[head_x][head_y] == 1):
                print("end")
                check = False
                break
            count += 1
            board[head_x][head_y] = 1

            q.put([head_x, head_y])

            

            head_x += move[0]
            head_y += move[1]
                
            if(head_x < 0 or head_y < 0 or head_y >= n or head_x >= n or board[head_x][head_y] == 1):
                print("end2")
                check = False
                break
            if(apple[head_x][head_y] == 0):
                board[tail_x][tail_y] = 0
                tail = q.get()
                tail_x = tail[0]
                tail_y = tail[1]
            else:
                apple[head_x][head_y] = 0
            print_board(board, n)
            
            
    change_move(move, m)


print(count)