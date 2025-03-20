import sys
n = int(sys.stdin.readline())
arr = [0 for i in range(n)]
for i in range(n):
    arr[i] = int(int(sys.stdin.readline()))
arr.sort()
for i in range(len(arr)):
    print(arr[i])
