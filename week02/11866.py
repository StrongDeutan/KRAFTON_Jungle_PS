import sys
from collections import deque

iput = list(map(int, sys.stdin.readline().split()))
n = iput[0]
k = iput[1]

q = deque()
for i in range(1, n+1):
    q.append(i)

ans = []
check = True
while(len(q) > 0):
    for i in range(k - 1):
        q.append(q.popleft())
    ans.append(q.popleft())


print("<", end="")
for i in range(len(ans) - 1):
    print(f"{ans[i]}, ", end="")
print(f"{ans[len(ans) - 1]}>")
