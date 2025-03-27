import sys
from collections import deque

sys.setrecursionlimit(10 ** 7)

class vertex:
    def __init__(self, value):
        self.value = value
        self.child_list = []
        self.visit_DFS = False
        self.visit_BFS = False


def DFS(start: vertex, vertex_list: list):
    if(start.visit_DFS == True):
        return
    
    print(start.value, end=" ")
    start.visit_DFS = True

    if(len(start.child_list) == 0):
        return
    for i in start.child_list:
        DFS(vertex_list[i], vertex_list)


def BFS(start: vertex, vertex_list: list):
    q = deque()
    q.append(start)
    while q:
        cur = q.popleft()
        if(cur.visit_BFS == True):
            continue
        print(cur.value, end=" ")
        cur.visit_BFS = True
        for i in cur.child_list:
            q.append(vertex_list[i])




lines = list(map(int, sys.stdin.readline().split()))
N = lines[0]
M = lines[1]
start = lines[2]

vertex_list = [None for i in range(N + 1)]
for i in range(1, N + 1):
    newVertex = vertex(i)
    vertex_list[i] = newVertex

for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    vertex_list[s].child_list.append(e)
    vertex_list[e].child_list.append(s)

for i in range(1, N + 1):
    vertex_list[i].child_list.sort()

DFS(vertex_list[start], vertex_list)
print()
BFS(vertex_list[start], vertex_list)

