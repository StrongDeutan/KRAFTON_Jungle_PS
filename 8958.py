iter = int(input())

for i in range(iter):
    quiz_result = input()
    size = len(quiz_result)

    seq = 0
    total = 0
    for k in range(size):
        if(quiz_result[k] == 'O'):
            seq += 1
            total += seq
        else:
            seq = 0

    print(total)