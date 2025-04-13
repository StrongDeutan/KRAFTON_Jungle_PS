import sys
from collections import deque

def solve(stk: list, arr: deque):
    check = True        # true -> 정방향

    for i in range(len(stk)):
        if(stk[i] == "R"):
            if(check):
                check = False
            else:
                check = True
        else:
            if(len(arr) == 0):
                print("error")
                return
            if(check):
                arr.popleft()
            else:
                arr.pop()

    if(not check):
        arr.reverse()            

    print("[", end="")
    for i in range(len(arr) - 1):
        print(arr[i], end=",")
    if(len(arr) != 0):
        print(arr[len(arr) - 1], end="")
    print("]")
    




T = int(sys.stdin.readline())
for i in range(T):
    p = sys.stdin.readline().rstrip()
    stk = []
    for j in range(len(p)):
        if(p[j] == "R"):                                # R이 2개 붙어있는 경우 없애기
            if(stk and stk[-1] == "R"):
                stk.pop()
            else:
                stk.append(p[j])
        else:
            stk.append(p[j])
    
    n = int(sys.stdin.readline())
    temp = sys.stdin.readline().rstrip()
    if(temp == "[]"):
        arr = deque()
    else:
        s = []
        s = temp[1: len(temp) - 1]
        arr = deque(s.split(","))

    
    solve(stk, arr)


    
