import sys
from collections import deque


def solve(arr: deque, cmd: str, size: int):
    if(size == 0):
        for i in cmd:
            if(i == "D"):
                print("error")
                return
        print("[]")
        return

    idx = 0
    while(idx < len(cmd)):
        if(cmd[idx] == "R"):
            if(cmd[idx + 1] == "R"):
                idx += 2
                continue
            if(len(arr) == 0 or len(arr) == 1):
                idx += 1
                continue
            arr.reverse()
        else:
            if(len(arr) == 0):
                print("error")
                return
            arr.popleft()
        idx += 1
    
    
    print("[", end="")
    for i in range(len(arr) - 1):
        print(arr[i], end=",")
    if(len(arr) != 0):
        print(arr[len(arr) - 1], end="")
    print("]")




T = int(sys.stdin.readline())

for i in range(T):
    func = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().rstrip()
    s = s[1: len(s) - 1]
    arr = deque(s.split(","))
    solve(arr, func, n)

