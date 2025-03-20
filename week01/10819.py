import sys

# 인덱스를 다음 인덱스와 바꿧을 때 합이 늘어나는지 판단하는 함수
# 순간의 이득이 집단의 이득이 아님
# 틀린코드 _1 참조

def is_add(arr: list, idx):
    print("hi")
    if(idx == 0):
        l = abs(arr[2] - arr[1])
        r = abs(arr[2] - arr[0])
        print(l, r)
        if(r > l):
            temp = arr[idx+1]
            arr[idx+1] = arr[idx]
            arr[idx] = temp
            print('t1')
            return True
        else:
            print('f1')
            return False
    elif(idx == len(arr) - 2):
        l = abs(arr[idx-1] - arr[idx])
        r = abs(arr[idx-1] - arr[idx+1])
        print(l, r)
        if(r > l):
            temp = arr[idx]
            arr[idx] = arr[idx+1]
            arr[idx+1] = temp
            print('t2')
            return True
        else:
            print('f2')
            return False
    else:
        l = abs(arr[idx] - arr[idx-1]) + abs(arr[idx+2] - arr[idx+1])
        r = abs(arr[idx+1] - arr[idx-1]) + abs(arr[idx+2] - arr[idx])
        print(l, r)
        if(r > l):
            temp = arr[idx]
            arr[idx] = arr[idx+1]
            arr[idx+1] = temp
            print('t3')
            return True
        else:
            print('f3')
            return False


n = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
for i in range(len(arr) - 1):
    if(is_add(arr, i)):
        print(i)
        i = 0

print(arr)