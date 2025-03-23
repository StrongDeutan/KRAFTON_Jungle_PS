import sys
import heapq

N = int(sys.stdin.readline())
pq_left = []
ans = 0
pq_right = []


first = int(sys.stdin.readline())
ans = first
print(ans)


for i in range(1, N):
    k = int(sys.stdin.readline())
    if(ans < k):
        if(len(pq_left) == len(pq_right)):
            heapq.heappush(pq_right, k)
            print(ans)
        elif(len(pq_right) - len(pq_left) == 1):
            heapq.heappush(pq_left, -ans)
            ans = k
            pr = heapq.heappop(pq_right)
            if(pr < ans):
                temp = pr
                pr = ans
                ans = temp
            heapq.heappush(pq_right, pr)
            print(ans)
        else:
            print("error")
    else:
        if(len(pq_left) == len(pq_right)):
            heapq.heappush(pq_right, ans)
            ans = k
            if(len(pq_left) != 0):
                pl = -heapq.heappop(pq_left)
                if(pl > ans):
                    temp = pl
                    pl = ans
                    ans = temp
                heapq.heappush(pq_left, -pl)
            print(ans)
        elif(len(pq_right) - len(pq_left) == 1):
            heapq.heappush(pq_left, -k)
            print(ans)
        else:
            print("error")

    
    
    


    