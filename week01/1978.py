import sys
import math

def check_prime(a):
    if(a == 1):
        return False
    for i in range(2, int(math.sqrt(a)) + 1):
        if(a % i == 0):
            return False
    return True

size = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

count = 0
for i in range(size):
    if(check_prime(arr[i])):
        count += 1
print(count)
    