size = 9
arr = [0 for i in range(size)]
max = 0
idx = 0

for i in range(size):
    arr[i] = int(input())
    if(arr[i] > max):
        max = arr[i]
        idx = i + 1


print(max)
print(idx)

    
