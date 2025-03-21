import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
lp = 0
rp = N - 1

val = 2 * (10 ** 9)
ans_l = 0
ans_r = 0
while(lp < rp):
    mix = arr[lp] + arr[rp]
    if(val > abs(mix)):
        val = abs(mix)
        ans_l = lp
        ans_r = rp
    if(mix == 0):
        ans_l = lp
        ans_r = rp
        break
    elif(mix < 0):
        lp += 1
    else:
        rp -= 1
    
print(arr[ans_l], arr[ans_r])