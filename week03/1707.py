import sys

sys.setrecursionlimit(10 ** 8)

check = True


class node:
    def __init__(self, val):
        self.val = val
        self.color = 0         # 0 default, 1 and 2 -> color type
        self.visit = False
        self.child_list = []

    def get_color(self):
        return self.color
    

def DFS(node_list: list, cur: node, color: int):
    global check
    if(cur.visit):
        if(cur.color != color):
            # print(f"cur value: {cur.val}")
            # print(f"cur color : {cur.color}")
            # print(f"color : {color}")
            check = False
        return
    cur.visit = True
    cur.color = color
    if(color == 1):
            color = 2
    else:
        color = 1
    for i in cur.child_list:
        DFS(node_list, node_list[i], color)



k = int(sys.stdin.readline()) # test case
for i in range(k):
    check = True

    V, E = map(int, sys.stdin.readline().split())

    node_list = [None for i in range(V + 1)]

    for i in range(1, V+1):
        node_list[i] = node(i)

    for i in range(E):
        u, v = map(int, sys.stdin.readline().split())
        node_list[u].child_list.append(v)
        node_list[v].child_list.append(u)

    for i in range(1, V+1):
        if(node_list[i].visit == True):
            continue
        DFS(node_list, node_list[i], 1)
    if(check):
        print("YES")
    else:
        print("NO")

