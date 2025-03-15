import sys

n = int(sys.stdin.readline())

arr = [0] * 10001
for i in range(n):
    k = int(sys.stdin.readline())
    arr[k] += 1

count = 0
for i in range(1, 10001):
    if(arr[i] != 0):
        for k in range(arr[i]):
            print(i)
        count += arr[i]
    if(count == n):
        break