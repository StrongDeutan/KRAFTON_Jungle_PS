import sys
import heapq

N = int(sys.stdin.readline())

pq = []
for i in range(N):
    card = int(sys.stdin.readline())
    heapq.heappush(pq, card)

if(N == 1):
    print(0)
else:
    total = 0
    for i in range(N - 1):
        a = heapq.heappop(pq)
        b = heapq.heappop(pq)
        total += (a+b)
        heapq.heappush(pq, a+b)
    print(total)