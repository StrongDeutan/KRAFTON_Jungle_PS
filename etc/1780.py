import sys

#return list = [0갯수 1갯수 -1갯수]


def solve(k: int, paper: list, left_top_row: int, left_top_col: int):
    temp = [0] * 3
    if(k == 1):
        for i in range(3):
            for j in range(3):
                temp[paper[left_top_row + i][left_top_col + j]] += 1
        return temp
    
    for i in range(3):
        for j in range(3):
            a = solve(k - 1, paper, left_top_row + i * 3 ** (k - 1), left_top_col + j * 3 **(k - 1))
            #print(a)
            if(a[0] == 9):
                temp[0] += 1
            elif(a[1] == 9):
                temp[1] += 1
            elif(a[2] == 9):
                temp[2] += 1
            else:
                for z in range(3):
                    temp[z] += a[z]
    
    return temp





n = int(sys.stdin.readline())
paper = [[0] * n for i in range(n)]

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for k in range(n):
        paper[i][k] = row[k]

temp = [0, 0, 0]
if(n == 1):
    temp[paper[0][0]] += 1
else:
    t = 3
    k = 1
    while(t != n):
        t *= 3
        k += 1

    a = solve(k, paper, 0, 0)
    if(a[0] == 9):
        temp[0] += 1
    elif(a[1] == 9):
        temp[1] += 1
    elif(a[2] == 9):
        temp[2] += 1
    else:
        for i in range(3):
            temp[i] += a[i]

print(temp[-1])
print(temp[0])
print(temp[1])