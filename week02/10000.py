import sys
from functools import cmp_to_key

# 10000_2.py 로


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
        

def stk_pop(sub_stk: list):
    re = sub_stk.pop()
    val = 0
    total = re[1] - re[0]
    while(len(sub_stk) > 1):
        c = sub_stk.pop()
        total += c[1] - c[0]
    if(len(sub_stk) != 0 and total == sub_stk[0][1] - sub_stk[0][0]):
        val += 1
        sub_stk.pop()
    sub_stk.append(re)
    return val


def count_area(circles: list):
    ans = 1
    stk = [circles[0]]
    start_idx = 0
    for i in range(1, len(circles)):
        if(circles[i][0] < circles[start_idx][1]):
            stk.append(circles[i])
            if(circles[i][1] >= stk[0][1] - 1):
                ans += stk_pop(stk)
            ans += 1
        else:
            start_idx = i
            ans += stk_pop(stk)
            stk.append(circles[i])
            ans += 1
    ans += stk_pop(stk)
    

    print(ans + 1)

                        




n = int(sys.stdin.readline())
arr = []
for i in range(n):
    circle = list(map(int, sys.stdin.readline().split()))
    put = [circle[0] - circle[1], circle[0] + circle[1]]
    arr.append(put)
arr.sort(key=cmp_to_key(compare))
count_area(arr)

