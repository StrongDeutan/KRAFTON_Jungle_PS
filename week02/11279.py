import sys
import heapq

N = int(sys.stdin.readline())

pq = []

for i in range(N):
    x = int(sys.stdin.readline())
    if(x == 0):
        if(len(pq) == 0):
            print(0)
        else:
            print(heapq.heappop(pq)[1])
    else:
        heapq.heappush(pq, (-x, x))