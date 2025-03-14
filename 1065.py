import sys

n = int(input())


if(n < 100):
    print(n)
else:
    count = 0
    for i in range(100, n + 1):
        h = i // 100
        t = (i % 100) // 10
        o = i % 10
        if(h - t == t - o):
            count += 1
    
    print(99+count)


