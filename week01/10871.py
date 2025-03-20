n, x = input().split()
n = int(n)
x = int(x)

A = input()
arr = A.split()


for i in range(n):
    arr[i] = int(arr[i])
    if(arr[i] < x):
        print(arr[i], end=' ')