import sys


# 2812_1.py로


n, k = map(int, sys.stdin.readline().split())
num = sys.stdin.readline().rstrip()

size = n - k
stk = []
for i in range(1, n + 1):
    a = num[-i]
    stk.append(int(a))

sub_stk = []
ans = []

#print(stk)


while(k > 0):
    #print(f"{k} : k")
    #print(f"{stk} : stk")
    
    count = 0
    big = 0
    for i in range(k):
        temp = stk.pop()
        big = max(big, temp)
        sub_stk.append(temp)
    
    if(len(stk) == 0):
        while(sub_stk and count < k):
            cur = sub_stk.pop()
            if(cur >= big):
                ans.append(cur)
                count += 1
        break
    else:
        while sub_stk:
            cur = sub_stk.pop()
        
            if(cur >= stk[len(stk) - 1] and cur >= big):
                ans.append(cur)
            else:
                count += 1 
    k -= count


while stk:
    ans.append(stk.pop())
for i in range(size):
    print(ans[i], end="")

