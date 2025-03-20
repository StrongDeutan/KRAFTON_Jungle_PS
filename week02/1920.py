import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

m = int(sys.stdin.readline())
find = list(map(int, sys.stdin.readline().split()))

def find_k(k: int, s: int, e: int):
    mid = (s + e) // 2
    if(arr[mid] == k):
        return 1
    if(s >= e):
        return 0
    if(arr[mid] < k):
        return find_k(k, mid + 1, e)
    else:
        return find_k(k, s, mid - 1)



for i in range(m):
    print(find_k(find[i], 0, n - 1))



