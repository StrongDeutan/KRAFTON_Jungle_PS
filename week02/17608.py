import sys

n = int(sys.stdin.readline())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))

last = arr[n-1]
ans = 1
m = last
for i in range(2, n + 1):
    if(arr[n - i] > last and arr[n - i] > m):
        ans += 1
        m = max(m, arr[n - i])
print(ans)