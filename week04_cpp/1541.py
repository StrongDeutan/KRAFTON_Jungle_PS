import sys


s = sys.stdin.readline().rstrip().split('-')

#print(s)

total = 0

temp1 = []

mult = 1
for k in s[0]:
    temp1.append(k)
while temp1:
    p = temp1[-1]
    if(p == '+'):
        temp1.pop()
        mult = 1
    else:
        total += int(p) * mult
        mult *= 10
        temp1.pop()

mult = 1


for i in range(1, len(s)):
    temp_total = 0
    temp = []
    for k in s[i]:
        temp.append(k)
    while temp:
        p = temp[-1]
        if(p == '+'):
            temp.pop()
            mult = 1
        else:
            temp_total += int(p) * mult
            mult *= 10
            temp.pop()
    #print(temp_total)
    total -= temp_total
    mult = 1

print(total)
