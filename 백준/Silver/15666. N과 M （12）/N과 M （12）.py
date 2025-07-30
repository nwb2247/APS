def bt(depth, start): # lst[start] ~ lst[N-1]을 selected[depth] 위치에 넣겠다.
    if depth == M:      # selected가 완성이 되면 str로 바꾸고 set에 있는지 확인하고 없으면 추가하고 출력
        st = " ".join(list(map(str, selected)))
        if st not in st_set:
            st_set.add(st)
            print(st)
        return

    for i in range(start, N):
        selected[depth] = lst[i]
        bt(depth + 1, i)  # 같은 수를 여러번 골라도 되므로 start = i로 설정


N, M = map(int, input().split())

# 비내림차순 출력을 위해 정렬하고 idx로 접근
lst = list(map(int, input().split()))
lst.sort()

selected = [0] * M

# 문자열로 바꾸고 중복 관리 위해 set 선언
st_set = set()

bt(depth=0, start=0)