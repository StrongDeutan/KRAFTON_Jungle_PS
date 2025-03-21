import sys

def multiple(a, b, c):
    ans = 1
    if(b % 2 != 0):
        ans *= a
    if(b <= 1):
        return a
    return (ans*multiple(a, b // 2, c)**2)%c


A, B, C = map(int, sys.stdin.readline().split())

if(B == 0):
    print(1)
elif(B == 1):
    print(A % C)
else:
    print(multiple(A, B, C))