import sys
sys.setrecursionlimit(10 ** 8)

count = 0

class computer:
    def __init__(self, val):
        self.val = val
        self.child_list = []
        self.visit = False


def DFS(computer_list: list, cur: computer):
    global count
    if(cur.visit == True):
        return
    
    cur.visit = True
    
    count += 1

    for i in cur.child_list:
        DFS(computer_list, computer_list[i])



n = int(sys.stdin.readline())
m = int(sys.stdin.readline())


computer_list = [None for i in range(n + 1)]
for i in range(1, n+1):
    computer_list[i] = computer(i)

for i in range(m):
    u, v = map(int, sys.stdin.readline().split())
    computer_list[u].child_list.append(v)
    computer_list[v].child_list.append(u)


DFS(computer_list, computer_list[1])

print(count - 1)

