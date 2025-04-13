import sys
import heapq


n, k = map(int, sys.stdin.readline().split())

virus = []
grid = []
for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    grid.append(row)
    for j in range(n):
        if row[j] != 0:
            heapq.heappush(virus, (row[j], i, j))  

s, px, py = map(int, sys.stdin.readline().split())


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(s):
    if not virus:
        break
    next_virus = []
    
    while virus:
        v_n, x, y = heapq.heappop(virus)  

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

           
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            
            if grid[nx][ny] != 0:
                continue

           
            grid[nx][ny] = v_n
            heapq.heappush(next_virus, (v_n, nx, ny))

    virus = next_virus  

# 출력
print(grid[px-1][py-1]) 
