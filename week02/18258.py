import sys
from collections import deque

n = int(sys.stdin.readline())

q = deque()
for i in range(n):
    put = sys.stdin.readline().split()
    com = put[0]
    
    if(com == "push"):
        k = int(put[1])
        q.append(k)
    elif(com == "front"):
        if(len(q) == 0):
            print(-1)
        else:
            print(q[0])
    elif(com == "size"):
        print(len(q))
    elif(com == "pop"):
        if(len(q) == 0):
            print(-1)
        else:
            print(q.popleft())
    elif(com == "empty"):
        if(len(q) == 0):
            print(1)
        else:
            print(0)
    else:
        if(len(q) == 0):
            print(-1)
        else:
            print(q[len(q) - 1])


