import sys
count = 0
n = int(sys.stdin.readline())

board = [[0] * n for i in range(n)]

def solve(x):
    global count
    if(x == n - 1):
        for y in range(n):
            if(board[x][y] == 0):
                count += 1
    else:
        for y in range(n):
            if(board[x][y] == 0):
                for i in range(n):
                    board[x][i] += 1
                    board[i][y] += 1
                    if(x - i >= 0 and y - i >= 0):
                        board[x - i][y - i] += 1
                    if(x - i >= 0 and y + i < n):
                        board[x - i][y + i] += 1
                    if(x + i < n and y - i >= 0):
                        board[x + i][y - i] += 1
                    if(x + i < n and y + i < n):
                        board[x + i][y + i] += 1
                    
            
                
                solve(x + 1)
            
                for i in range(n):
                    board[x][i] -= 1
                    board[i][y] -= 1
                    if(x - i >= 0 and y - i >= 0):
                        board[x - i][y - i] -= 1
                    if(x - i >= 0 and y + i < n):
                        board[x - i][y + i] -= 1
                    if(x + i < n and y - i >= 0):
                        board[x + i][y - i] -= 1
                    if(x + i < n and y + i < n):
                        board[x + i][y + i] -= 1
                    
                




solve(0)
print(count)




