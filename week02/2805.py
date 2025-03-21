# Time_Limit Code
# Go to 2805_1.py

import sys




n_m = list(map(int, sys.stdin.readline().split()))
n = n_m[0]
m = n_m[1]

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

def sum_arr(start, val):
    global n
    total = 0
    for i in range(start, n):
        total += arr[i]
    total -= val * (n - start)
    return total


def print_ans(start, idx):
    ans = start
 
    while(sum_arr(idx + 1, ans) > m):
        ans += 1

    print(ans)

check = 0
for i in range(n):
    if(sum_arr(i, arr[i]) < m):
        break
    else:
        check = i

print_ans(arr[check], check)



