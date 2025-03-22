import sys
from functools import cmp_to_key
import heapq

def compare(x: list, y: list):
    if(x[0] > y[0]):
        return 1
    elif(x[0] < y[0]):
        return -1
    else:
        if(x[1] > y[1]):
            return 1
        else:
            return -1
    


def count_area(circles: list):
    ans = len(circles)
    pq = []
    for i in range(len(circles)):
        check = False
        total = 0
        while(len(pq) != 0):
            top = heapq.heappop(pq)
            a = -top[0]
            top[0] = a
            if(top[0] > circles[i][0] or top[0] <= circles[i][0] - 2 * circles[i][1]):
                heapq.heappush(pq, [-top[0], top[1]])
                break
            total += 2 * top[1]

        if(total == circles[i][1] * 2):
            ans += 1
        heapq.heappush(pq, [-circles[i][0], circles[i][1]])

    
    print(ans + 1)

                        




n = int(sys.stdin.readline())
arr = []
for i in range(n):
    circle = list(map(int, sys.stdin.readline().split()))
    put = [circle[0] + circle[1], circle[1]]
    arr.append(put)
arr.sort(key=cmp_to_key(compare))
count_area(arr)

