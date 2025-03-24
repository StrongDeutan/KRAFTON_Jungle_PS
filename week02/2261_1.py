import sys
from functools import cmp_to_key

#go_to 2261_4.py

def double_Euclidean_distance(arr1: list, arr2: list):
    return (arr1[0] - arr2[0]) ** 2 + (arr1[1] - arr2[1]) ** 2

def compare(a: list, b: list):
    if(a[0] > b[0]):
        return 1
    elif(a[0] < b[0]):
        return -1
    else:
        return a[1] - b[1]



n = int(sys.stdin.readline())
locations_left = []
locations_right =[]

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if(x > 0):
        locations_right.append([x, y])
    else:
        locations_left.append([x, y])

locations_right.sort(key=cmp_to_key(compare))
locations_left.sort(key=cmp_to_key(compare))


len_left = len(locations_left)
len_right = len(locations_right)

ans = 10 ** 9

for i in range(len_left):
    if(ans == 0):
        break
    for k in range(i+1, len_left):
        if(abs(locations_left[i][0] - locations_left[k][0]) > ans):
            break
        ans = min(ans, double_Euclidean_distance(locations_left[i], locations_left[k]))
    
for i in range(len_left):
    if(ans == 0):
        break
    for k in range(len_right):
        if(abs(locations_left[i][0] - locations_right[k][0]) > ans):
            break
        ans = min(ans, double_Euclidean_distance(locations_left[i], locations_right[k]))

for i in range(len_right):
    if(ans == 0):
        break
    for k in range(i+1, len_right):
        if(abs(locations_right[i][0] - locations_right[k][0]) > ans):
            break
        ans = min(ans, double_Euclidean_distance(locations_left[i], locations_right[k]))


print(ans)    
