def bt(start, depth):       # depth 위치에 start부터 N까지 넣겠다.
    if depth == M:          # selected 완성되었다면
        print(*selected)    # 출력
        return

    for i in range(start, N+1):
        selected[depth] = i     # start 이후부터 확인하므로 중복된 것이 들어갈 가능성 없음
        bt(i+1, depth+1)

N, M = map(int, input().split())
selected = [0]*M
bt(start=1, depth=0)