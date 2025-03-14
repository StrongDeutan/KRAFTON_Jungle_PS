a = int(input())
b = int(input())
c = int(input())

result = a * b * c
result_str = str(result)
count = [0 for i in range(10)]

for i in range(len(result_str)):
    count[int(result_str[i])] += 1

for i in range(len(count)):
    print(count[i])

