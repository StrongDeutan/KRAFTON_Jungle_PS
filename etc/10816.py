import sys



n = int(sys.stdin.readline())

cards = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())

find = list(map(int, sys.stdin.readline().split()))

d = dict()
for i in range(len(cards)):
    k = cards[i]
    if(k in d):
        temp = d.get(k)
        temp += 1
        d[k] = temp
    else:
        d[k] = 1

for i in range(len(find)):
    if(find[i] in d):
        print(d[find[i]], end=" ")
    else:
        print(0, end=" ")