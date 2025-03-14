c = int(input())

for i in range(c):
    case_by_class = input()
    arr = case_by_class.split()

    total = 0
    arr[0] = int(arr[0])
    for k in range(1, len(arr)):
        arr[k] = int(arr[k])
        total += arr[k]
    
    
    avg = (total / arr[0])
    count = 0
    for k in range(1, len(arr)):
        if(arr[k] > avg):
            count += 1

    print(round(100 * count / arr[0], 3), end='')
    print("%")
