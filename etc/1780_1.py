import sys

def solve(n: int, paper: list, left_top_row: int, left_top_col: int) -> list:
    temp = [0] * 3
    if(n == 1):
        temp[paper[left_top_row][left_top_col]] += 1
        return temp
    
    for i in range(3):
        for k in range(3):
            a = solve(n // 3, paper, left_top_row + i * n // 3, left_top_col + k * n // 3)
            for z in range(3):
                temp[z] += a[z]

    if(temp[0] == 0 and temp[1] == 0):
        temp[2] //= 9
    elif(temp[1] == 0 and temp[2] == 0):
        temp[0] //= 9
    elif(temp[0] == 0 and temp[2] == 0):
        temp[1] //= 9
    return temp


n = int(sys.stdin.readline().rstrip())

paper = [[0] * n for i in range(n)]

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for k in range(n):
        paper[i][k] = row[k]

ans = solve(n, paper, 0, 0)
print(ans[-1])
print(ans[0])
print(ans[1])