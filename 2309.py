import sys

arr = [0 for i in range(101)]
heights = []

total = 0

for i in range(9):
    height = int(sys.stdin.readline())
    heights.append(height)
    total += height
    arr[height] += 1 

total -= 100
for i in range(9):
    if(heights[i] != total - heights[i] and arr[total - heights[i]] == 1):
        
        arr[heights[i]] = 0
        arr[total - heights[i]] = 0
        break

for i in range(101):
    if(arr[i] == 1):
        print(i)


