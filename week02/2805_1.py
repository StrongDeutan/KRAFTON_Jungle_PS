import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))


start = 0
end = max(arr)

while(start <= end):
    mid = (start + end) // 2
    total = 0
    for i in arr:
        if(i > mid):
            total += (i - mid)
    if(total < m):
        end = mid - 1
    else:
        start = mid + 1
print(end)    

