def merge_sort(l):
    if len(l) <= 1:
        return l

    # 반으로 나누고 병합 정렬
    left = merge_sort(l[:len(l)//2])
    right = merge_sort(l[len(l)//2:])

    # 정렬된 양쪽의 결과를 합쳐줌
    li, ri = 0, 0   # 왼쪽 인덱스 오른쪽 인덱스 초기화
    ret = [0]*len(l)
    for i in range(len(l)):
        if li >= len(left):     # 왼쪽 리스트 다썼다면
            ret[i] = right[ri]
            ri += 1
        elif ri >= len(right):  # 오른쪽 리스트 다썼다면
            ret[i] = left[li]
            li += 1
        else:                   # 둘다 남아있다면 작은 것을
            if left[li] < right[ri]:
                ret[i] = left[li]
                li += 1
            else:
                ret[i] = right[ri]
                ri += 1
    return ret

N = int(input())
lst = [int(input()) for _ in range(N)]

print(*merge_sort(lst), sep="\n")

# # 배열 인덱스를 이용한 퀵소트
# def qsort(start, end): # 시작인덱스, 마지막인덱스
#     if end-start <= 0: # 종료 조건 비어있거나 하나만 있다면 -> 이미 정렬 (비어있는 경우는 end<start)
#         return
#
#     pivot = lst[start]
#     left = start+1
#     right = end
#     while left<right: # 다른 동안 진행, 즉 left == right 되면 종료
#         if lst[left] <= pivot:      # (D) 같은 수가 올 수 있으므로
#             left += 1
#         elif lst[right] >= pivot:   # (D) 같은 수가 올 수 있으므로
#             right -= 1
#         else :
#         # lst[left]는 pivot보다 크고, lst[right]는 pivot 보다 작은 상태라 바꿀 준비가 되었다면
#             lst[left], lst[right] = lst[right], lst[left]
#
#     # lst[left]가 pivot보다 크다면, lst[left-1]가 pivot보다 작거나 같은 상태이므로 pivot과 자리를 바꿀 수 있음
#     if lst[left] > pivot:
#         lst[left-1], lst[start] = lst[start], lst[left-1]
#         qsort(start, left-2) # pivot이 left-1로 이동했으므로 왼쪽은 start~left-2 오른쪽은 left~end
#         qsort(left, end)
#     # lst[left]가 pivot보다 작거나 같다면, 바로 pivot과 자리를 바꿀 수 있음
#     else:
#         lst[left], lst[start] = lst[start], lst[left]
#         qsort(start, left-1) # pivot이 left로 이동했으므로 왼쪽은 start~left-1 오른쪽은 left+!~end
#         qsort(left+1, end)
#
#
# N = int(input())
# lst = [int(input()) for _ in range(N)]
# qsort(0, N-1)
# print(*lst, sep="\n")



# # 리스트를 이용한 퀵소트
# def qsort(l):
#     if len(l) <= 1: # 종료 조건 비어있거나 하나만 있다면 -> 이미 정렬
#          return l
#
#     pivot = l.pop() # 맨 마지막 원소 pop하여 피벗으로 (마지막을 pop하는게 제일 빠르므로)
#
#     left = [] # 빈리스트 생성, 피벗보다 작다면 왼쪽, 크다면 오른쪽에 append
#     right = []
#     for e in l:
#         if e<pivot:
#             left.append(e)
#         else:
#             right.append(e)
#
#     #left, right에 대해서도 퀵소트 시킴
#     return qsort(left) + [pivot] + qsort(right)
#
# print(*qsort(lst), sep="\n")


