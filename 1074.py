import sys
import math

def find_area(a, row, col):
    if(row < a and col < a):
        return 0
    elif(row < a and col >= a):
        return 1
    elif(row >= a and col < a):
        return 2
    else:
        return 3
    
def solve(n, r, c, ans):
    if(n == 1):
        ans[0] += find_area(n, r, c)
        return
    divide_point = 2 ** (n - 1)
    mul = find_area(divide_point, r, c)
    ans[0] += mul * (divide_point ** 2)
    if(r >= divide_point):
        r -= divide_point
    if(c >= divide_point):
        c -= divide_point
    solve(n - 1, r, c, ans)

put = list(map(int, sys.stdin.readline().split()))
ans = [0]
solve(put[0], put[1], put[2], ans)
print(ans[0])



