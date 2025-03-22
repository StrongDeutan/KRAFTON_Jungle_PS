import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
board = [[0] * n for i in range(n)]
apple = [[0] * n for i in range(n)]
head = [0, 0]
timer = 0

for i in range(k):
    x, y = map(int, sys.stdin.readline().split())
    apple[x - 1][y - 1] = 1

L = int(sys.stdin.readline())
prev = 'R'
for i in range(L):
    t, move = map(sys.stdin.readline().split())
    t = int(t)
