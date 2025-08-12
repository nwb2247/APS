TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    lst = [tuple(map(int, input().split())) for _ in range(N)]
    lst.sort(key=lambda x:x[1]) # 끝나는 시간으로 정렬
    # 끝나는 시간이 더 늦은 것을 고른다면, 그 다음에 넣을 수 있는 것의 개수는 항상 작거나 같아지므로,
    # 끝나는 시간이 빠른 것을 넣어야함

    cnt = 0 # 개수
    ce = 0  # 마지막 작업의 끝나는 시간
    for ns, ne in lst:
        if ns >= ce:
            cnt += 1
            # print(ns, ne)
            ce = ne

    print(f"#{tc} {cnt}")

