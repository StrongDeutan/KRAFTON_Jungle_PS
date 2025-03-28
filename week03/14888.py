import sys
from itertools import permutations


N = int(sys.stdin.readline())

numbers = list(map(int, sys.stdin.readline().split()))

opers = list(map(int, sys.stdin.readline().split()))

operations = []            # 0 + 1 - 2 * 3 //

for i in range(4):
    for k in range(opers[i]):
        operations.append(i)

o = list(permutations(operations, N-1))     # 연산자 순열


ans_max = -(10**9)
ans_min = 10**9

for i in range(len(o)):
    total = numbers[0]
    for k in range(N - 1):
        if(o[i][k] == 0):
            total += numbers[k + 1]
        elif(o[i][k] == 1):
            total -= numbers[k + 1]
        elif(o[i][k] == 2):
            total *= numbers[k + 1]
        else:
            if(total < 0):
                total = abs(total) // numbers[k + 1]
                total = -total
            else:
                total //= numbers[k + 1]

    ans_max = max(ans_max, total)
    ans_min = min(ans_min, total)


print(ans_max)
print(ans_min)