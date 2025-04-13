import sys

def count_lines(lines: list, distance: int):
    if(distance == 0):
        return 0
    count = 0
    for i in lines:
        count += (i // distance)
    return count

k, n = map(int, sys.stdin.readline().split())
lines = []

for i in range(k):
    lines.append(int(sys.stdin.readline()))
lines.sort()

start = 0
end = lines[k - 1]

ans = 0
while(start <= end):
    mid = (start + end) // 2
    if(count_lines(lines, mid) < n):
        end = mid - 1
    else:
        ans = mid
        start = mid + 1


if(ans == 0):
    ans = 1
print(ans)

