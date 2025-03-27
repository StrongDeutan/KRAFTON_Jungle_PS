import sys

sys.setrecursionlimit(10 ** 8)

class node:
    def __init__(self, val):
        self.val = val
        self.child_list = []
        self.visit = False
    

def DFS(node_list: list, start: node):
    if(start.visit == True):
        return
    
    start.visit = True

    for i in start.child_list:
        DFS(node_list, node_list[i])



N, M = map(int, sys.stdin.readline().split())
node_list = [None for i in range(N + 1)]
for i in range(1, N+1):
    newNode = node(i)
    node_list[i] = newNode

for i in range(M):
    u ,v = map(int, sys.stdin.readline().split())
    node_list[u].child_list.append(v)
    node_list[v].child_list.append(u)

count = 0
for i in range(1, N+1):
    if(node_list[i].visit == False):
        count += 1
        DFS(node_list, node_list[i])
    else:
        continue

print(count)