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
    while i < len(left) and j < len(right) :
        if left[i] <= right[j] :
            srt[idx] = left[i]
            idx += 1
            i += 1
        else :
            srt[idx] = right[j]
            idx += 1
            j += 1
    if i < len(left) :
        # 개선 부분 (while문 대신 slicing으로 대입)
        # list의 slicing이 좌변에 오면 해당 위치에 원소를 하나씩 대입하겠다는 뜻
        # 우변에 오면 그 범위의 요소를 복사해 새 리스트를 만들겠다는 뜻
        # 즉 같은 개수를 가진 list slicing을 대입하면 각 원소가 대체됨
        # (단 갯수가 다르면 원본 배열의 길이가 늘어나거나 줄어들 수 있음)
        srt[idx:] = left[i:]
    else :
        srt[idx:] = right[j:]
    return srt
print(*merge_sort(input_lst), sep="\n")


"""
1차 시도
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
"""



