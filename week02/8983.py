# nm time 60 points


import sys


def manhattan_distance(x1, y1, p):
    return abs(x1 - p) + y1

def check_distance(animal: list, p: list, r):
    for k in range(len(p)):
        if(manhattan_distance(animal[0], animal[1], p[k]) <= r):
            return True
    return False



M, N, L = map(int, sys.stdin.readline().split())


point_ = list(map(int, sys.stdin.readline().split()))

animals = []

for i in range(N):
    animals.append(list(map(int, sys.stdin.readline().split())))

ans = 0

for i in range(N):
    if(check_distance(animals[i], point_, L)):
        ans += 1


print(ans)