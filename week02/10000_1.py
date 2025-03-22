import sys
from functools import cmp_to_key

# 10000_2.py

r = 10 ** 9

def compare(x: list, y: list):
    if(x[0] > y[0]):
        return 1
    elif(x[0] < y[0]):
        return -1
    else:
        if(x[1] > y[1]):
            return -1
        else:
            return 1
        

def count_area(circles: list):
    ans = 0
    stk = []
    sub_stk = []
    for i in range(len(circles)):
        if(len(stk) == 0):
            stk.append(circles[i])
            #print(f"{circles[i]} : cur append")
        else:
            if(stk[0][1] > circles[i][0]):
                stk.append(circles[i])
                #print(f"{circles[i]} : cur append")
            else:
                while(len(stk) > 0):
                    cur = stk.pop()
                    #print(f"{cur} : cur")
                    ans += 1
                    if(len(sub_stk) == 0):
                        sub_stk.append(cur)
                    else:
                        if(sub_stk[-1][0] >= cur[1]):
                            sub_stk.append(cur)
                            #print(f"{cur} : cur sub")
                        else:
                            total = 0
                            
                            #print(f"{stk} : stack pop")
                            while(len(sub_stk) > 0):
                                s_cur = sub_stk.pop()
                                total += s_cur[1] - s_cur[0]
                            if(total == cur[1] - cur[0]):
                                ans += 1
                                #print(f"{cur} : cur sub")
                            sub_stk.append(cur)
                stk.append(circles[i])
    while(len(stk) > 0):
        cur = stk.pop()
        #print(f"{cur} : cur1")
        ans += 1
        if(len(sub_stk) == 0):
            sub_stk.append(cur)
        else:
            if(sub_stk[-1][0] >= cur[1]):  # 04 가 두번나와야함 조건문제 체크
                sub_stk.append(cur)
            else:
                total = 0
                while(len(sub_stk) > 0):       
                    s_cur = sub_stk.pop()
                    total += s_cur[1] - s_cur[0]
                if(total == cur[1] - cur[0]):
                    ans += 1
                    #print(f"{cur} : cur1 sub")
                sub_stk.append(cur)
    print(ans + 1)

                        




n = int(sys.stdin.readline())
arr = []
for i in range(n):
    circle = list(map(int, sys.stdin.readline().split()))
    put = [circle[0] - circle[1], circle[0] + circle[1]]
    arr.append(put)
arr.sort(key=cmp_to_key(compare))
count_area(arr)

