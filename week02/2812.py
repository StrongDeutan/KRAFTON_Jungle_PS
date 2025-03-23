import sys

n, k = map(int, sys.stdin.readline().split())
num = sys.stdin.readline().rstrip()


stk = []
for i in range(1, n + 1):
    a = num[-i]
    stk.append(int(a))

sub_stk = []
for i in range(k):
    sub_stk.append(stk.pop())

while(len(sub_stk) > 0):
    temp = sub_stk.pop()
    if(temp > stk[len(stk) - 1]):
        stk.pop()
        stk.append(temp)

print(stk)


