import sys

input = sys.stdin.readline

N = int(input())
lst = [int(input()) for _ in range(N)]

# 배열 인덱스를 이용한 퀵소트
def qsort(start, end): # 시작인덱스, 마지막인덱스
    if end-start <= 0: # 종료 조건 비어있거나 하나만 있다면 -> 이미 정렬 (비어있는 경우는 end<start)
        return

    pivot = lst[start]
    left = start+1
    right = end
    while left<right: # 다른 동안 진행, 즉 left == right 되면 종료
        if lst[left] < pivot:
            left += 1
        elif lst[right] > pivot:
            right -= 1
        else :
            lst[left], lst[right] = lst[right], lst[left]
    if lst[left] > pivot:
        lst[left-1], lst[start] = lst[start], lst[left-1]
        qsort(start, left-2)
        qsort(left, end)
    else:
        lst[left], lst[start] = lst[start], lst[left]
        qsort(start, left-1)
        qsort(left+1, end)



qsort(0, N-1)
print(*lst, sep="\n")



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
