import sys
import heapq

N = int(sys.stdin.readline())
pq = [-10000]
for i in range(N):
    k = int(sys.stdin.readline())
    

    heapq.heappush(pq, k)
    print(pq)
    s = len(pq) // 2
    


    #print(pq[len(pq) // 2])