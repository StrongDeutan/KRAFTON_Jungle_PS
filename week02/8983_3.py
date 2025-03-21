import sys

def binary_search(p: list, x):
    s = 0
    e = len(p) - 1
    mid = 0
    while(s <= e):
        mid = (s+e) // 2
        if(p[mid] > x):
            e = mid - 1
        elif(p[mid] == x):
            return mid
        else:
            s = mid + 1
    if e < 0: 
        return s
    if s >= len(p): 
        return e
    
    if abs(p[s] - x) < abs(p[e] - x):
        return s
    else:
        return e
M, N, L = map(int, sys.stdin.readline().split())
point = list(map(int, sys.stdin.readline().split()))
point.sort()
ans = 0
for i in range(N):
    x, y = map(int, sys.stdin.readline().split())
    # x로 이분탐색
    # 가장 가까운 point와 맨해튼거리측정
    # L 이하이면 ans++

    if(abs(point[binary_search(point, x)] - x) + y <= L):
        ans += 1
print(ans)
