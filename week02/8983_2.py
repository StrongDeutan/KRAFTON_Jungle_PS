#nlogm time 9 points

import sys


def manhattan_distance(x1, y1, p):
    return abs(x1 - p) + y1

def check_distance(animal: list, p: list, r):
    
    s = 0
    e = len(p) - 1
    
    animal_x = animal[0]
    mid = 0
    while(s <= e):
        mid = (s + e) // 2
        if(p[mid] > animal_x):
            e = mid - 1     
        else:
            if(manhattan_distance(animal[0], animal[1], p[mid]) <= r):
                return True
            s = mid + 1
    
    if(abs((s-1) - animal_x) < abs((e + 1) - animal_x)):
        mid = s - 1
    else:
        mid = e + 1
    if(manhattan_distance(animal[0], animal[1], p[mid]) <= r):
        return True
    return False



M, N, L = map(int, sys.stdin.readline().split())


point = list(map(int, sys.stdin.readline().split()))
point.sort()

animals = []

for i in range(N):
    animals.append(list(map(int, sys.stdin.readline().split())))

ans = 0

for i in range(N):
    if(check_distance(animals[i], point, L)):
        ans += 1


print(ans)