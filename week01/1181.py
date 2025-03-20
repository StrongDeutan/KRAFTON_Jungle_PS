import sys
from functools import cmp_to_key
def compare(x, y):
    size_x = len(x)
    size_y = len(y)
    if(size_y < size_x):
        return 1
    elif( size_x == size_y ):
        temp = [x, y]
        temp.sort()
        if(temp[0] == y):
            return 1
        else:
            return -1
    else:
        return -1



n = int(sys.stdin.readline())



words = []
for i in range(n):
    a = input()
    words.append(a)

s = sorted(words, key=cmp_to_key(compare))
ans = [s[0]]
for i in range(1, len(s)):
    if(ans[len(ans) - 1] == s[i]):
        continue
    ans.append(s[i])

for i in range(len(ans)):
    print(ans[i])
    