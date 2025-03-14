import sys

eratos = [1 for i in range(10001)]
eratos[0] = 0
eratos[1] = 0
for i in range(2, 101):
    if(eratos[i] == 0):
        continue
    
    mul = 2
    while(i * mul <= 10000):
        eratos[i * mul] = 0
        mul += 1



iter = int(sys.stdin.readline())

for i in range(iter):
    even = int(sys.stdin.readline())
    left = 0
    right = 0
    for k in range(2, (even // 2) + 1):
        if(eratos[k] == 1 and eratos[even - k] == 1):
            left = k; right = even - k
    
    print(left, right)

