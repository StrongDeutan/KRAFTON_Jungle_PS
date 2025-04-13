import sys

# 틀렸습니다

def binary_search(blocks: list, start: int, end: int, value: int) -> list:
    if(start >= end):
        if(blocks[start] == value):
            return [True, blocks[start]]
        return [False, 0]
    mid = (start + end) // 2
    if(blocks[mid] == value):
        return [True, blocks[mid]]
    elif(blocks[mid] > value):
        return binary_search(blocks, start, mid - 1, value)
    else:
        return binary_search(blocks, mid + 1, end, value)



def Testcase():
    try:
        x = int(sys.stdin.readline())
    except:
        return False
    x *= 10 ** 7       # 나노미터 변환

    n = int(sys.stdin.readline())
    blocks = []

    for i in range(n):                      # 블록 입력
        blocks.append(int(sys.stdin.readline()))

    blocks.sort()

    for i in range(n - 1):
        temp = binary_search(blocks, i + 1, n - 1, x - blocks[i])
        if(temp[0] == True):
            print("yes", blocks[i], temp[1])
            return
        else:
            continue
    print("danger")

    return True

def __main__():
    while(True):
        if not Testcase():
            break

__main__()

