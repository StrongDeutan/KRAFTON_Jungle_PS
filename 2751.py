# 실패

import sys


def merge(arr: list, start, end):
    mid = (start + end) // 2
    arr1 = arr[0:mid]
    arr2 = arr[mid:end]

    size1 = len(arr1)
    size2 = len(arr2)
    total_size = size1 + size2
    temp_arr = [0 for i in range(total_size)]

    idx1 = 0
    idx2 = 0
    for i in range(total_size):
        if(idx1 == size1):
            temp_arr[i] = arr2[idx2]
            idx2 += 1
        elif(idx2 == size2):
            temp_arr[i] = arr1[idx1]
            idx1 += 1
        else:
            if(arr1[idx1] < arr2[idx2]):
                temp_arr[i] = arr1[idx1]
                idx1 += 1
            else:
                temp_arr[i] = arr2[idx2]
                idx2 += 1
    return temp_arr

def merge_sort(arr: list, start, end):
    if(start < end):
        mid = (start + end) // 2
        arr1 = merge_sort(arr, start, mid)
        arr2 = merge_sort(arr, mid + 1, end)
        return merge(arr, start, end)


    


n = int(sys.stdin.readline())
arr = [0 for i in range(n)]
for i in range(n):
    arr[i] = int(int(sys.stdin.readline()))
sorted_arr = merge_sort(arr, 0, len(arr))
for i in range(len(sorted_arr)):
    print(sorted_arr[i])


