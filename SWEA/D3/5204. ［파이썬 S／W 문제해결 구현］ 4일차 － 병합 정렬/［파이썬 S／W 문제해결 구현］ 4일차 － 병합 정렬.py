def merge_sort(lst):
    # print(lst)

    global ans
    if len(lst) <= 1: # 종료 조건, 정렬 필요 X
        return lst

    # 반으로 나눠 각각 재귀 호출
    left = merge_sort(lst[:len(lst)//2])
    right = merge_sort(lst[len(lst)//2:])

    # 정렬된 결과가 왼쪽 리스트 마지막이 오른쪽 리스트 마지막 보다 크다면 ans+=1
    if left[-1] > right[-1]:
        ans += 1

    li, ri = 0, 0
    ret = []
    # 빈 배열이 생길 때까지 작은 것을 ret에 append
    while li < len(left) and ri < len(right):
        if left[li] < right[ri]:
            ret.append(left[li])
            li += 1
        else:
            ret.append((right[ri]))
            ri += 1

    return ret + left[li:] + right[ri:]
    # 지금까지의 ret + 남은것 연결 (빈 것은 붙여도 영향없으므로 ok)



TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 0
    lst = merge_sort(lst)
    print(f"#{tc} {lst[N//2]} {ans}")