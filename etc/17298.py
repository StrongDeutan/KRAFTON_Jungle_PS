import sys


n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
stk = []

for i in range(n):
    # print(f"iter : {i}")
    # print(f"stk : {stk}")
    
    if(i != n - 1 and arr[i] < arr[i+1]):
        arr[i] = arr[i+1]
        while(stk and stk[-1][0] < arr[i]):
            update = stk.pop()
            arr[update[1]] = arr[i]
    else:
        while(stk and stk[-1][0] < arr[i]):
            update = stk.pop()
            arr[update[1]] = arr[i]
        stk.append([arr[i], i])

arr[n - 1] = -1

while(stk):
    update = stk.pop()
    arr[update[1]] = -1

for i in arr:
    print(i, end=" ")