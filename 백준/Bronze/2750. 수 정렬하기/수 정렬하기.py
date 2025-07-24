# swap을 이용한 정렬 (선택 정렬과 유사)
N = int(input())
lst = [int(input()) for _ in range(N)]
for i in range(N-1) : # N-2번째까지 정렬을 마치면 N-1(마지막)번째는 자동으로 가장 큰 값이 오게 됨
    # i : i번째로 작은 값을 찾아 넣을 것
    # i+1부터 끝까지 lst[i]와 비교하여 swap하고, 가장 작은 값이 i번째에 오도록 함
    for j in range(i+1, N) :
        if lst[j] < lst[i] :
            lst[i], lst[j] = lst[j], lst[i]
print(*lst)
