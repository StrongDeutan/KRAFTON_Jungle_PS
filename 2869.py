import sys

arr = list(map(int, sys.stdin.readline().split()))

prev_h = arr[2] - arr[0]
prev_day = prev_h // (arr[0] - arr[1])
if(prev_h % (arr[0] - arr[1]) != 0):
    prev_day += 1
print(prev_day + 1)