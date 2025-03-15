import sys

n = int(sys.stdin.readline())
arr = [0 for i in range(n)]
for i in range(n):
    arr[i] = int(sys.stdin.readline())

for i in range(n):
    check = True
    for k in range(n - 1):
        if(arr[k] > arr[k+1]):
            temp = arr[k]
            arr[k] = arr[k+1]
            arr[k+1] = temp
            check = False
    if(check):
        break

for i in range(n):
    print(arr[i])