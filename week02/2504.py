import sys


def solve(s: str):
    stk = []
    ans = 0

    temp = 1
    for i in range(len(s)):
        if(s[i] == "("):
            stk.append(s[i])
            temp *= 2
        elif(s[i] == "["):
            stk.append(s[i])
            temp *= 3
        elif(s[i] == ")"):
            if(not stk):
                ans = 0
                #print("error")
                break
            cur = stk.pop()
            if(cur != "("):
                ans = 0
                #print("error")
                break
            else:
                if(s[i-1] == "("):
                    ans += temp
                    #print(temp, i)
                temp //= 2
        else:
            if(not stk):
                ans = 0
                #print("error")
                break
            cur = stk.pop()
            if(cur != "["):
                ans = 0
                #print("error")
                break
            else:
                if(s[i-1] == "["):
                    #print(temp, i)
                    ans += temp
                temp //= 3
    if(stk):
        ans = 0
    print(ans)

    






s = sys.stdin.readline().rstrip()
solve(s)
