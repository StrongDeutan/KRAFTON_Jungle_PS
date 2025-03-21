import sys

a = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1] * a

ans = 1
for i in range(1, a):
    for k in range(0, i):
        if(arr[i] > arr[k]):
            dp[i] = max(dp[i], dp[k] + 1)
    ans = max(ans, dp[i])
    
print(ans)