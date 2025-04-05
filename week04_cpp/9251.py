import sys

str1 = sys.stdin.readline().rstrip()
str2 = sys.stdin.readline().rstrip()

row = len(str1)
col = len(str2)

dp = [[0] * (col + 1) for i in range(row + 1)]
for i in range(col + 1):
    dp[0][i] = 0
for i in range(row + 1):
    dp[i][0] = 0

for i in range(1, row+1):
    for k in range(1, col+1):
        if(str1[i-1] == str2[k-1]):
            dp[i][k] = dp[i-1][k-1] + 1
        else:
            dp[i][k] = max(dp[i-1][k], dp[i][k-1])

print(dp[row][col])
