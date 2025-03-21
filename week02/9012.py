import sys

t = int(sys.stdin.readline())
for i in range(t):
    stk = []
    str = sys.stdin.readline().rstrip()
    check = True
    for i in range(len(str)):
        if(len(stk) == 0):
            if(str[i] == ")"):
                check = False
                print("NO")
                break
        if(str[i] == "("):
            stk.append(str[i])
        if(str[i] == ")"):
            p = stk.pop()
            if(p != "("):
                check = False
                print("NO")
                break
    if(check):
        if(len(stk) == 0):
            print("YES")
        else:
            print("NO")