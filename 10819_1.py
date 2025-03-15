import sys
from itertools import permutations

def sum_of_arr(arr: list):
    total = 0
    for i in range(len(arr) - 1):
        total += abs(arr[i] - arr[i+1])
    return total

n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))

ans = 0
perm = list(permutations(arr))
for i in range(len(perm)):
    ans = max(ans, sum_of_arr(perm[i]))

print(ans)

