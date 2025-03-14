import sys
import math
sys.setrecursionlimit(10**8)


def hanoi(n, start, sub, end):
    if(n == 1):
        print(start, end)
        return
    hanoi(n-1, start, end, sub)
    hanoi(1, start, sub, end)
    
    hanoi(n-1, sub, start, end)

n = int(sys.stdin.readline())

count = int(math.pow(2, n))
print(count - 1)
# 부동소수점 과정을 변환하면서 손실발생 가능
# print(2**100 - 1) 사용 가능


if(n <= 20):
    hanoi(n, 1, 2, 3)

    


    
