import sys

len_rec = list(map(int, sys.stdin.readline().split()))

col = [1 for i in range(len_rec[0] + 1)]
row = [1 for i in range(len_rec[1] + 1)]

rec = [row, col]

iter = int(sys.stdin.readline())

for i in range(iter):
    cut = list(map(int, sys.stdin.readline().split()))
    rec[cut[0]][cut[1]] = 0

prev = 0
row_max_len = 0
for i in range(len(row)):
    if(row[i] == 0):
        if(row_max_len < i - prev):
            row_max_len = i - prev
        prev = i
if(row_max_len < len(row) - prev - 1):
    row_max_len = len(row) - prev - 1

prev = 0
col_max_len = 0
for i in range(len(col)):
    if(col[i] == 0):
        if(col_max_len < i - prev):
            col_max_len = i - prev
        prev = i
if(col_max_len < len(col) - prev - 1):
    col_max_len = len(col) - prev - 1

print(col_max_len * row_max_len)