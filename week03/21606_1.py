import sys

sys.setrecursionlimit(10 ** 8)

global count
count = 0

class location:
    def __init__(self):  
        self.child_list = []


def DFS(locations: list, cur: int, start: bool, visit_table: list, s_: list):
    global count

    if(visit_table[cur] == 1):
        return
    
    visit_table[cur] = 1

    if(not start):
        if(s_[cur - 1] != "0"):
            count += 1
            return
        
    for i in locations[cur].child_list:
        DFS(locations, i, False, visit_table, s_)




N = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()
s_ = []
for i in range(N):
    s_.append(s[i])


locations = [None for i in range(N + 1)]

for i in range(1, N+1):
    locations[i] = location()

for i in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    locations[u].child_list.append(v)
    locations[v].child_list.append(u)
   

# -------------입력-----------

for i in range(1, N+1):
    if(s_[i - 1] != "1"):
        continue
    visit = [0 for i in range(N+1)]
    DFS(locations, i, True, visit, s_)
    # print(f"{count, i} : count, i")
    

print(count)