import sys

sys.setrecursionlimit(10 ** 8)

class node:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.child_list = []
        self.visit = False

def DFS(node_list: list, cur: node, par):
    if(cur.visit == True):
        return
    cur.visit = True
    cur.parent = par
    for i in cur.child_list:
        DFS(node_list, node_list[i], cur.val)


N = int(sys.stdin.readline())

node_list = [None for i in range(N+1)]
for i in range(1, N+1):
    node_list[i] = node(i)

for i in range(N - 1):
    r, k = map(int, sys.stdin.readline().split())
    node_list[r].child_list.append(k)
    node_list[k].child_list.append(r)

DFS(node_list, node_list[1], 0)

for i in range(2, N+1):
    print(node_list[i].parent)
