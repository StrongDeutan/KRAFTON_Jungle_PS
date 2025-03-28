import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())

def count_water(matrix: list, row :int, col: int):
    if(matrix[row][col] < 1):
        return 0
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    count = 0

    for i in range(4):
        if(matrix[row + dx[i]][col + dy[i]] == 0):
            count += 1

    return count

def BFS(visit: list, row, col):
    q = deque()
    q.append([row, col])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while(q):
        cur = q.popleft()
        visit[cur[0]][cur[1]] = True
        for i in range(4):
            x = cur[0] + dx[i]
            y = cur[1] + dy[i]
            if(not visit[x][y]):
                q.append([x, y])


def count_area(matrix: list, visit: list):
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
minus_matrix = [[0] * m for i in range(n)]
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
while(True):
    if(ice < 1):
        year = 0
        break
    
    areas = count_area(matrix, visit)
 
    if(areas >= 2):
        break

    year += 1

    for i in range(n):
        for k in range(m):
            if(matrix[i][k] < 1):
                continue
            minus_matrix[i][k] = count_water(matrix, i, k)

    for i in range(n):
        for k in range(m):
            if(matrix[i][k] < 1):
                continue
            matrix[i][k] -= minus_matrix[i][k]

            if(matrix[i][k] < 1):
                ice -= 1
            else:
                visit[i][k] = False

print(year)
            




