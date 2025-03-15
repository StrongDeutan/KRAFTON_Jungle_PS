import sys



def find_area(mat: list, depth):
    
    count = 0
    q = []
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    n = len(mat)
    visit = [[1] * n for i in range(n)]

    
    for i in range(1, n - 1):
        for k in range(1, n - 1):
            visit[i][k] = 0
            if(mat[i][k] < depth):
                visit[i][k] = 1
    
    for i in range(n):
        for k in range(n):
            if(visit[i][k] == 0):
                q.append([i, k])
                while(len(q) != 0):
                    point = q.pop()
                    x = point[0]
                    y = point[1]
                    visit[x][y] = 1
                    for z in range(4):
                        if(visit[x+dx[z]][y+dy[z]] == 0):
                            q.append([x+dx[z], y+dy[z]])
                count += 1
    
    return count
    

n = int(sys.stdin.readline())
top = [1 for i in range(n + 2)]
matrix = []
matrix.append(top)
for i in range(n):
    row = [1]
    temp_row = list(map(int, sys.stdin.readline().split()))
    temp_row.append(1)
    row += temp_row
    matrix.append(row)
matrix.append(top)



max = 0
for i in range(1, 101):
    temp = find_area(matrix, i)
    if(max < temp):
        max = temp

print(max)