import sys

def solve(vidoe: list, n: int, left_top_row: int, left_top_col: int) -> str:
    # base case
    if(n == 2):
        lt = video[left_top_row][left_top_col]
        rt = video[left_top_row][left_top_col + 1]
        ld = video[left_top_row + 1][left_top_col]
        rd = video[left_top_row + 1][left_top_col + 1]
        if(lt == rt and rt == ld and ld == rd):
            return lt
        else:
            return lt + rt + ld + rd
    # recursion

    temp = ""
    n //= 2
    for i in range(2):
        for k in range(2):
           temp += solve(video, n, left_top_row + i * n, left_top_col + k * n) 
    

    # merge
    check = True
    for i in range(len(temp) - 1):
        if(temp[i] != temp[i + 1]):
            check = False
            break
        
    if(check):
        temp = temp[0]

    return temp





n = int(sys.stdin.readline())

video = [["0"] * n for i in range(n)]
for i in range(n):
    row = sys.stdin.readline().rstrip()
    for k in range(n):
        video[i][k] = row[k]

print(solve(video, n, 0, 0))