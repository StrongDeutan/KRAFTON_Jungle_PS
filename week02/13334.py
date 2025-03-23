import sys
import heapq
from functools import cmp_to_key

def compare(x:list, y:list):
    if(x[1] > y[1]):
        return 1
    elif(x[1] < y[1]):
        return -1
    else:
        if(x[0] > y[0]):
            return 1
        else:
            return -1

def solve(l: list, dist: int):
    ans = 0
    pq = []
    for i in range(len(l)):
        if(l[i][1] - l[i][0] > dist):
            continue
        end = l[i][1]
        

        while(pq and (pq[0][0] < end - dist)):
            cur = heapq.heappop(pq)
            #print(cur)
        heapq.heappush(pq, l[i])
        ans = max(ans, len(pq))
    print(ans)






n = int(sys.stdin.readline())

l = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    if(x < y):
        l.append([x, y])
    else:
        l.append([y, x])

l.sort(key=cmp_to_key(compare))
#print(l)
d = int(sys.stdin.readline())
solve(l, d)

