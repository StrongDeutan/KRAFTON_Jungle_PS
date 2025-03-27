import sys
import heapq

class edge:
    def __init__(self):
        self.edgeList = []

    def insert_edge(self, dest, weight):
        self.edgeList.append([weight, dest])

V, E = map(int, sys.stdin.readline().split())

nodes = [0] * (V + 1)
edges = [edge() for _ in range(V+1)]


pq = []
for i in range(E):
    row = list(map(int, sys.stdin.readline().split()))
    w = row[2]
    v1 = row[0]
    v2= row[1]
    edges[v1].insert_edge(v2, w)
    edges[v2].insert_edge(v1, w)

start_edge = edges[1]
nodes[1] = 1
for i in range(len(start_edge.edgeList)):
    heapq.heappush(pq, start_edge.edgeList[i])

count = 1
total = 0
while(count != V):
    cur = heapq.heappop(pq)
    idx = cur[1]
    if(nodes[idx] == 1):
        continue
    else:
        start_edge = edges[idx]
        nodes[idx] = 1
        count += 1
        total += cur[0]
        for i in range(len(start_edge.edgeList)):
            heapq.heappush(pq, start_edge.edgeList[i])

print(total)

