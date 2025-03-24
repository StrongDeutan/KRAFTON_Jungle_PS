import sys

def solve(hist: list, start: int, end: int):   # max rectangle in range(start, end)
    if(start == end):
        return 0
    if(start + 1 == end):
        return hist[start]

    mid = (start + end) // 2
    ans = max(solve(hist, start, mid), solve(hist, mid, end))

    height = hist[mid]
    width = 1
    right_point = mid
    left_point = mid


    while right_point-left_point+1 < end-start:
        go_left = 0
        go_right = 0
        if (left_point > start):
            go_left = min(height, hist[left_point-1])
        else:
            go_left = -1
        
        if (right_point < end - 1):
            go_right = min(height, hist[right_point+1])
        else:
            go_right = -1
        
        if go_left >= go_right:
            height = go_left
            left_point -= 1
        else:
            height = go_right
            right_point += 1

        width += 1
        ans = max(ans, width*height)

    return ans




while(True):
    problem = list(map(int, sys.stdin.readline().split()))
    if(problem[0] == 0):
        break
    n = problem[0]
    histogram = problem[1: n + 1]
    print(solve(histogram, 0, n))