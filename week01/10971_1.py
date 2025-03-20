import sys
from itertools import permutations

n = int(sys.stdin.readline())
arr_init = []
cost = [[0]*n for i in range(n)]

for i in range(n):
    arr_init.append(i)
    row = list(map(int, sys.stdin.readline().split()))
    for k in range(n):
        cost[i][k] = row[k]



ans = 100000000

perm = list(permutations(arr_init))
for i in range(len(perm)):
    travel = perm[i]
    total = 0
    check = True
    for k in range(len(travel) - 1):
        start = travel[k]
        end = travel[k+1]
        if(cost[start][end] == 0):
            check = False
            break
        total += cost[start][end]
        
    if(check):
        if(cost[travel[len(travel) - 1]][travel[0]] == 0):
            continue
        else:
            total += cost[travel[len(travel) - 1]][travel[0]]
            ans = min(ans, total)

print(ans)


#pypy로 제출하니 correct