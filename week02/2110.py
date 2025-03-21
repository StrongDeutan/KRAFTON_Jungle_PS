import sys

n, c = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))
arr.sort()

s = 1
e = arr[n - 1] - arr[0]
ans = 0
while(s <= e):
    
    count = 1
    mid = (s + e) // 2

    prev = arr[0]
    for i in range(1, n):
        if(arr[i] >= prev + mid):
            count += 1
            prev = arr[i]
    if(count >= c):
        s = mid + 1
        ans = mid
    else:
        e = mid - 1
    

print(ans)
