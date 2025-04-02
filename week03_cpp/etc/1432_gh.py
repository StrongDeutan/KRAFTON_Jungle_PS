import math
import sys
from collections import deque
import heapq
import copy
from itertools import combinations

sys.setrecursionlimit(100000)
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
n = int(input())
v = [[0 for _ in range(n+1)]]

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
q = deque()

for i in range(1, n+1):             # initialize q to append zero in-degree
    if deg[i] == 0:
        q.append(i)

if not q:
    flag = True

avail = [False for _ in range(n+1)]     # visit table

for i in q:
    avail[i] = True

topo=[]
lst = [i for i in range(1, n+1)]
result= [0]

def func():
    global avail
    global topo
    global lst
    if len(result) == n+1:
        topo.append(result[:])
        #print(result)
        return
    
    for i in lst:
        if avail[i]:
            result.append(i)
            avail[i] = False
            for j in range(1, n+1):
                if v[i][j] == 1:
                    deg[j] -=1
                    if deg[j] == 0:
                        avail[j] = True
            func()
            for j in range(1, n+1):
                if v[i][j] == 1:
                    deg[j] += 1
                    avail[j] = False
            result.pop()
            avail[i] = True
func()

if flag:
    print(-1)
else:
    real = []
    for t in topo:
        tmp = [0 for _ in range(n+1)]
        for i in range(1, n+1):
            tmp[t[i]] = i
        real.append(tmp)
    real.sort()
    for i in range(1, n+1):
        print(real[0][i], end=' ')