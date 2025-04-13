import sys




n = int(sys.stdin.readline())
cities = list(map(int, sys.stdin.readline().split()))
limit = int(sys.stdin.readline())


total = 0
for i in range(n):
    total += cities[i]


if(total <= limit):
    print(max(cities))
else:
    if((limit // n) < min(cities)):
        print(limit // n)
    else:
        cities.sort()
        start = cities[0]
        end = cities[len(cities) - 1]

        ans = 0
        while(start <= end):
            sum = 0
            mid = (start + end) // 2
           
            for i in range(n):
                sum += min(mid, cities[i])
            if(sum > limit):
                end = mid - 1
            else:
                ans = mid
                start = mid + 1
        print(ans)


