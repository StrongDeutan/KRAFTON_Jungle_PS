import sys

arr = sys.stdin.readline().split()
max = 0
for i in range(len(arr)):
    temp_str = ""
    for k in range(len(arr[i])):
        temp_str += arr[i][len(arr[i]) - 1 - k]
    arr[i] = int(temp_str)
    if(max < arr[i]):
        max = arr[i]

print(max)

