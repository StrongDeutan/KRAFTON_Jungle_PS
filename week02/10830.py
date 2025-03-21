import sys

arr = list(map(int, sys.stdin.readline().split()))
N, B = arr[0], arr[1]


def multiply_mat(mat1: list, mat2: list):
    temp_mat = [[0] * N for i in range(N)]
    for i in range(N):
        for k in range(N):
            for z in range(N):
                temp_mat[i][k] += (mat1[i][z] * mat2[z][k])
            temp_mat[i][k] %= 1000
    return temp_mat

ans = [[0] * N for i in range(N)]
A = [[0] * N for i in range(N)]

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    for k in range(N):
        A[i][k] = row[k]
        if(i == k):
            ans[i][k] = 1


while(B >= 1):
    if(B % 2 != 0):
        ans = multiply_mat(ans, A)   
    A = multiply_mat(A, A)
    B //= 2
for i in range(N):
    for k in range(N):
        print(ans[i][k], end=" ")
    print()