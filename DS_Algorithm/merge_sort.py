def merge(arr: list, start: int, end: int):
    if(start >= end):
        return [arr[start]]

    mid = (start + end) // 2
    left_arr = merge(arr, start, mid)
    right_arr = merge(arr, mid + 1, end)

    temp = []
    left_idx = 0
    right_idx = 0
    left_len = len(left_arr)
    right_len = len(right_arr)


    while(left_arr <left_len and right_idx < right_len):
        
    
