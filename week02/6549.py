# 틀렸습니다


import sys

while(True):
    row = list(map(int, sys.stdin.readline().split()))
    if(row[0] == 0):
        break
    n = row[0]
    histogram = row[1:n + 1]

    ans = histogram[0]

    stk = [[histogram[0], 0]]
    size = 1
    for i in range(1, n):       
        if(size == 0):
            stk.append([histogram[i], i])
            ans = max(histogram[i], ans)
            size += 1
        else:
            if(histogram[i] < stk[size - 1][0]):
                
                while(size > 0 and stk[size - 1][0] >= histogram[i]):
                    cur = stk.pop()
                    d = i - cur[1]
                    ans = max(ans, d * cur[0])
                    ans = max(ans, (d + 1) * histogram[i])
                    # pop하면서 max연산 추가
                    size -= 1
            stk.append([histogram[i], i])
            size += 1
            ans = max(ans, histogram[i])            

    while(size > 0):    # 마지막 스택비우기
        cur = stk.pop()
        d = n - cur[1]
        ans = max(ans, d * cur[0])
        size -= 1
    print(ans)
