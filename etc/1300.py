import sys

# 다시




n = int(sys.stdin.readline())
k = int(sys.stdin.readline())



if(k < n * (n+1) // 2):
    find = 1
    while(True):
        if((find+1) * (find + 2) // 2 > k):
            k -= find * (find + 1) // 2
            break
        find += 1
    if(k == 1 or k == 2):
        print(find)
    else:
        row = find - 1
        col = 2
        k -= 2
        while(k > 0):
            row -= 1
            col += 1
            k -= 1
        print(row * col)

else:
    k -= n * (n+1) // 2
    find = 1
    print(f"k : {k}")
    while(True):
        if(n * (n+1) // 2 -  (find+1) * (find + 2) // 2 < k):
            break
        find += 1
    find -= 1
    if(k == 1 or k == 2):
        print((n - find) * n)
    else:
        row = n - 1
        col = n + 1 - find
        k -= 3
        while(k > 0):
            row -= 1
            col += 1
            k -= 1
        print(row * col)

