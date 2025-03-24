import sys
from functools import cmp_to_key


#2261 템플릿

def double_Euclidean_distance(arr1: list, arr2: list):
    return (arr1[0] - arr2[0]) ** 2 + (arr1[1] - arr2[1]) ** 2

def compare(a: list, b: list):
    if(a[0] > b[0]):
        return 1
    elif(a[0] < b[0]):
        return -1
    else:
        return a[1] - b[1]

def solve(locations: list, start: int, end: int):
    ans = 10 ** 9


    return ans



n = int(sys.stdin.readline())
locations = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    locations.append([x, y])
locations.sort(key=cmp_to_key(compare))


print(solve(locations, 0, n))    
