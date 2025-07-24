N = int(input())
input_lst = [int(input()) for _ in range(N)]

def merge_sort(lst) :
    if len(lst) == 1 :
        return lst
    # divide 부분
    left = merge_sort(lst[:len(lst)//2])
    right = merge_sort(lst[len(lst)//2:])
    # conquer 부분
    return merge(left, right)

def merge(left, right) :
    srt = [0]*(len(left)+len(right))
    i, j, idx = 0, 0, 0
    while i<len(left) and j<len(right) :
        if left[i] <= right[j] :
            srt[idx] = left[i]
            idx += 1
            i += 1
        else :
            srt[idx] = right[j]
            idx += 1
            j += 1
    if i < len(left) :
        while i < len(left) :
            srt[idx] = left[i]
            idx += 1
            i += 1
    else :
        while j < len(right) :
            srt[idx] = right[j]
            idx += 1
            j += 1
    return srt
print(*merge_sort(input_lst), sep="\n")

