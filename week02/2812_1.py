import sys

n, k = map(int, sys.stdin.readline().split())
num = sys.stdin.readline().rstrip()

size = n - k
stk = []

for i in range(n):
    if(k != 0):
        while(stk and stk[-1] < num[i]):
            stk.pop()
            k -= 1
            if(k == 0):
                break
    stk.append(num[i])

for i in range(size):
    print(stk[i], end="")