import sys

#point: 108/200 

sys.setrecursionlimit(10 ** 8)

global count
count = 0

class location:
    def __init__(self, is_internal, val):
        self.val = val
        self.is_internal = is_internal   # 1 실내 0 실외
        self.parent = None
        self.child_list = []
        self.visit = False


def DFS(locations: list, cur: location, start: bool):
    global count

    if(cur.visit):
        return
    
    cur.visit = True

    if(not start):
        if(cur.is_internal != 0):
            count += 1
            return
        
    for i in cur.child_list:
        DFS(locations, locations[i], False)

def DFS_init(locations: list, cur: location):
    if(not cur.visit):
        return
    
    cur.visit = False
        
    for i in cur.child_list:
        DFS_init(locations, locations[i])




N = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

locations = [None for i in range(N + 1)]

for i in range(1, N+1):
    locations[i] = location(int(s[i - 1]), i)

for i in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    locations[u].child_list.append(v)
    locations[v].child_list.append(u)
   

# -------------입력-----------

for i in range(1, N+1):
    if(locations[i].is_internal != 1):
        continue
    DFS(locations, locations[i], True)
    # print(f"{count, i} : count, i")
    DFS_init(locations, locations[i])


print(count)