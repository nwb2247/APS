arr = [list(map(int, input().split())) for _ in range(5)]
call = []
for _ in range(5):
    call += list(map(int, input().split()))

ans = 0
for i, ca in enumerate(call):
    # 마킹
    for r in range(5):
        for c in range(5):
            if arr[r][c] == ca:
                arr[r][c] = -1
    cnt = 0
    # 가로 카운트
    for r in range(5):
        if arr[r].count(-1) == 5:
            cnt += 1
    # 세로 카운트
    arr_t = [list(c) for c in zip(*arr)]
    for c in range(5):
        if arr_t[c].count(-1) == 5:
            cnt += 1
    # 우상향 대각 카운트
    sr, sc = 0, 0
    for j in range(5):
        if arr[sr+j*1][sc+j*1] != -1:
            break
    else:
        cnt += 1
    # 좌상향 대각 카운트
    sr, sc = 0, 4
    for j in range(5):
        if arr[sr+j*1][sc-j*1] != -1:
            break
    else:
        cnt += 1
    if cnt >= 3:
        ans = i+1
        break
print(ans)
