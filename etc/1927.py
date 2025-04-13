import sys
import heapq

N = int(sys.stdin.readline())

pq = []

for i in range(N):
    k = int(sys.stdin.readline())
    if(k == 0):
        if(len(pq) == 0):
            print(0)
        else:
            print(heapq.heappop(pq))
    else:
        heapq.heappush(pq, k)