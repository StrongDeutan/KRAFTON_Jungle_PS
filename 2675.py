import sys
iter = int(input())

for i in range(iter):
    read_line = sys.stdin.readline().split()
    repeat = int(read_line[0])
    s = read_line[1]
    for k in range(len(s)):
        for z in range(repeat):
            print(s[k], end='')
    print()
