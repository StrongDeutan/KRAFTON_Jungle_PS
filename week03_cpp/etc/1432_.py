import math
import sys
from collections import deque
import heapq
import copy
from itertools import combinations

sys.setrecursionlimit(10**5)

n = int(input())
v = [[0 for _ in range(n+1)]]

re_idx = 1                            # re indexing number


for _ in range(n):
    v.append([0] + list(map(int, list(sys.stdin.readline().strip()))))

deg = [0 for _ in range(n+1)]       # indegree count

for i in range(1, n+1):
    for j in range(1, n+1):
        if v[i][j] != 0:
            deg[j] += 1
            
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         print(v[i][j], end=' ')
#     print()

flag = False
q = []

for i in range(1, n+1):             # initialize q to append zero in-degree
    if deg[i] == 0:
        heapq.heappush(q, i)

if not q:
    flag = True                     # all node in one scc

result= [0 for _ in range(n + 1)]   # re_numbering array

def func():
    global re_idx
    count = 0                        # 모든 노드가 넘버링 되었는지 확인

    while q:
        cur_idx = heapq.heappop(q)          # in-degree가 0인 노드가 여러개 있다면, 앞에있는 인덱스부터
        result[cur_idx] = re_idx            # re_numbering
        re_idx += 1
        count += 1              
        for k in range(1, n+1):
            if(v[cur_idx][k] == 1):
                deg[k] -= 1
                if(deg[k] == 0):
                    heapq.heappush(q, k)


    if(count != n): flag = True     # 넘버링 된 노드가 부족하다면 -1

func()

if flag:
    print(-1)
else:
    for i in range(1, n+1):
        print(result[i], end=" ")