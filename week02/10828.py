import sys

N = int(sys.stdin.readline())

stk = []

for i in range(N):
    com = sys.stdin.readline().split()
    inst = com[0]
    if(inst == "push"):
        k = int(com[1])
        stk.append(k)
    elif(inst == "top"):
        if(len(stk) == 0):
            print(-1)
            continue
        print(stk[len(stk) - 1])
    elif(inst == "size"):
        print(len(stk))
    elif(inst == "pop"):
        if(len(stk) == 0):
            print(-1)
        else:
            print(stk.pop())
    else:
        if(len(stk) == 0):
            print(1)
        else:
            print(0)

