def min4(a,b,c,d):
    min = a
    if(min > b):
        min = b
    if(min > c):
        min = c
    if(min > d):
        min = d
    return min

x,y,w,h = input().split()

x = int(x)
y = int(y)
w = int(w)
h = int(h)


print(min4(x, y, w-x, h-y))