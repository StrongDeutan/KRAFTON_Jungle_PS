import sys

def double_Euclidean_distance(arr1, arr2):
    return (arr1[0] - arr2[0]) ** 2 + (arr1[1] - arr2[1]) ** 2

def solve(locations, start, end):
    ans = 10 ** 9
    # base case
    if end - start == 1:
        return double_Euclidean_distance(locations[start], locations[end])
    if end - start == 2:
        return min(
            double_Euclidean_distance(locations[start], locations[start+1]),
            double_Euclidean_distance(locations[start+1], locations[end]),
            double_Euclidean_distance(locations[start], locations[end])
        )
    # recursion
    mid = (start + end) // 2
    ans = min(solve(locations, start, mid), solve(locations, mid + 1, end))

    # left-right in mid-range
    border_line = locations[mid][0]
    sub = []
    for i in range(start, end + 1):
        if ((locations[i][0] - border_line) ** 2 < ans):
            sub.append(locations[i])

    
    sub.sort(key=lambda x: x[1])

    
    sub_len = len(sub)
    for i in range(sub_len):
        for k in range(i + 1, sub_len):
            if((sub[k][1] - sub[i][1]) ** 2 > ans):
                break
            ans = min(ans, double_Euclidean_distance(sub[i], sub[k]))

    return ans

n = int(sys.stdin.readline())
locations = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    locations.append([x, y])
locations.sort() 

print(solve(locations, 0, n - 1))
