# 틀렸습니다


import sys
    #rect_from_mid = hist[mid]

    # while(left_point >= start and right_point < end):
    #     if(hist[left_point] < hist[right_point]):
    #         height = min(hist[right_point], height)
    #         width += 1
    #         rect_from_mid = max(rect_from_mid, height * width)
    #         if(right_point < end - 1):
    #             right_point += 1
    #         else:
    #             left_point -= 1
    #     else:
    #         height = min(hist[left_point], height)
    #         width += 1
    #         rect_from_mid = max(rect_from_mid, height * width)
    #         if(left_point > start):
    #             left_point -= 1
    #         else:
    #             right_point += 1

while(True):
    row = list(map(int, sys.stdin.readline().split()))
    if(row[0] == 0):
        break
    n = row[0]
    histogram = row[1:n + 1]

    ans = histogram[0]

    stk = [[histogram[0], 0]]
    size = 1
    
    prev_idx = 0

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
                    print(f"{i, ans, d * cur[0], d} : pop")
                    ans = max(ans, (d + 1) * histogram[i])
                    print(f"{i, ans, (d  + 1)* histogram[i], d} : push")
                    print(f"{prev_idx, i} : prev")
                    # pop하면서 max연산 추가
                    size -= 1


                prev_idx = i
            stk.append([histogram[i], i])
            size += 1
            ans = max(ans, histogram[i])            

    while(size > 0):    # 마지막 스택비우기
        cur = stk.pop()
        d = n - cur[1]
        ans = max(ans, d * cur[0])
        size -= 1
    print(ans)
