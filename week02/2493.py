import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

stk = []
stk.append([arr[n-1], n - 1])
size = 1
for i in range(n-1):
    if(size == 0):
        stk.append([arr[n-2-i], n-2-i])
        size += 1
    else:
        while(size != 0 and stk[size - 1][0] <= arr[n-2-i]):
            arrive = stk.pop()
            size -= 1
            arr[arrive[1]] = n - 1 - i
        stk.append([arr[n-2-i], n-2-i])
        size += 1

for i in range(size):
    arrive = stk.pop()
    arr[arrive[1]] = 0

for i in arr:
    print(i, end=" ")
        