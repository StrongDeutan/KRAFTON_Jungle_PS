import sys

total = 0
stk = []
k = int(sys.stdin.readline())
for i in range(k):
    p = int(sys.stdin.readline())
    if(p == 0):
        total -= stk[len(stk) - 1]
        stk.pop()
    else:
        total += p
        stk.append(p)

print(total)