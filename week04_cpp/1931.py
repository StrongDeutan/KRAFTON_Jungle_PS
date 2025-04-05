import sys
from functools import cmp_to_key


n = int(sys.stdin.readline().rstrip())

arr = []

def compare(arr1: list, arr2: list):
    if(arr1[1] > arr2[1]):
        return 1
    elif(arr1[1] < arr2[1]):
        return -1
    else:
        if(arr1[0] > arr2[0]):
            return 1
        else:
            return -1


for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    arr.append(row)

arr.sort(key=cmp_to_key(compare))

# print(arr)
# print("--------------------")

count = 1
end_time = arr[0][1]
for i in range(1, n):
    if(end_time > arr[i][0]):
        continue
    #print(f"{end_time} : end time")
    end_time = arr[i][1]
    count += 1

print(count)
