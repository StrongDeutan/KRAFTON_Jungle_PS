import sys

n = int(sys.stdin.readline())

paper = [[0] * n for i in range(n)]
check = [[0] * n for i in range(n)]
#화이트 0 블루 1 완료 2

for i in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    for k in range(n):
        paper[i][k] = row[k]


ans_blue = 0
ans_white = 0
iter = 1
while(iter < n):
    dx = [0, iter, 0, iter]
    dy = [0, 0, iter, iter]
    
    i = 0
    while(i < n):
        k = 0
        while(k < n):
            blue_count = 0
            white_count = 0
            for p in range(4):
                # print(f"{iter} : iter {i+dx[p], k+dy[p]} : {paper[i+dx[p]][k+dy[p]]}")
                if(paper[i+dx[p]][k+dy[p]] == 0):
                    white_count += 1
                elif(paper[i+dx[p]][k+dy[p]] == 1):
                    blue_count += 1
                else:
                    continue
            if(white_count != 4 and blue_count != 4):
                paper[i][k] = 2
                # print(f"{iter} : iter {blue_count} : blue_count")
                # print(f"{iter} : iter {white_count} : white_count")
                ans_blue += blue_count
                ans_white += white_count
            k += iter * 2
        i += iter * 2

    iter *= 2

iter //= 2
if(paper[0][0] == paper[0][iter]):
    if(paper[0][0] == paper[iter][0]):
        if(paper[0][0] == paper[iter][iter]):
            if(paper[0][0] == 1):
                ans_blue += 1
            elif(paper[0][0] == 0):
                ans_white += 1

# print()
# print("-----ans-------------")
print(ans_white)
print(ans_blue)