import sys
from functools import cmp_to_key

# 시간초과 -> 2261_4.py

def double_Euclidean_distance(arr1: list, arr2: list):
    return (arr1[0] - arr2[0]) ** 2 + (arr1[1] - arr2[1]) ** 2

def compare_by_x(a: list, b: list):
    if(a[0] > b[0]):
        return 1
    elif(a[0] < b[0]):
        return -1
    else:
        return a[1] - b[1]

def compare_by_y(a: list, b: list):
    if(a[1] > b[1]):
        return 1
    elif(a[1] < b[1]):
        return -1
    else:
        return a[0] - b[0]


def solve(locations: list, start: int, end: int):
    ans = 10 ** 9

    #base case
    if(start == end):
        return 10 ** 9
    if(start + 1 == end):
        return double_Euclidean_distance(locations[start], locations[end])
    #recursion
    mid = (start + end) // 2
    ans = min(solve(locations, start, mid - 1), solve(locations, mid, end))

    if(ans == 0):
        return 0
    #left-right in mid area
    border_line = locations[mid][0]   # x = a 선
    sub = []                            # 경계선의 왼쪽으로 ans 오른쪽으로 ans내의 x좌표 점들

    left_list = locations[0: mid]
    right_list = locations[mid: len(locations)]


    for i in range(1, mid + 1):
        if(left_list[-i][0] < (border_line - ans // 2)):
            break
        sub.append(left_list[-i])
    for i in range(0, len(right_list)):
        if(right_list[i][0] > (border_line + ans // 2) + 1):
            break
        sub.append(right_list[i])

    sub.sort(key=lambda x: x[1])

    for i in range(len(sub)):
        for k in range(i + 1, len(sub)):
            if(sub[k][1] - sub[i][1] > ans):
                break
            ans = min(ans, double_Euclidean_distance(sub[i], sub[k]))


    return ans



n = int(sys.stdin.readline())
locations = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    locations.append([x, y])
locations.sort()


print(solve(locations, 0, n - 1))    
