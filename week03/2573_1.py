import sys
from collections import deque

#pypy 통과

n, m = map(int, sys.stdin.readline().split())

def count_water(visit: list, row :int, col: int):
    if(visit[row][col] == True):
        return 0
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    count = 0

    for i in range(4):
        if(visit[row + dx[i]][col + dy[i]] == True):
            count += 1

    return count

def BFS(visit: list, row, col):
    q = deque()
    q.append([row, col])
    visit[row][col] = True
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while(q):
        cur = q.popleft()
        for i in range(4):
            x = cur[0] + dx[i]
            y = cur[1] + dy[i]
            if(not visit[x][y]):
                q.append([x, y])
                visit[x][y] = True


def count_area(visit: list):
    global n
    global m

    count = 0

    for i in range(n):
        for k in range(m):
            if(visit[i][k]):
                continue
            BFS(visit, i, k)
            count += 1

    return count



matrix = [[0] * m for i in range(n)]
visit = [[True] * m for i in range(n)]
ice = 0                                            # 다녹았는지 체크

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for k in range(m):
        if(row[k] > 0):
            ice += 1
            visit[i][k] = False
        matrix[i][k] = row[k]
    
# -------------------입력-------------------

year = 0
areas = 0
while(True):
    if(ice < 1):
        year = 0
        break

    for i in range(1, n - 1):
        for k in range(1, m - 1):
            if(visit[i][k]):
                continue
            matrix[i][k] -= count_water(visit, i, k)
            if(matrix[i][k] < 1):
                ice -= 1

    areas = count_area(visit)      # visit table all true
    # print(areas)
    if(areas >= 2):
        break
    
    year += 1

    
    for i in range(1, n - 1):
        for k in range(1, m - 1):
            if(matrix[i][k] < 1):
                continue
            visit[i][k] = False

print(year)
            




