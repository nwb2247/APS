N, M, B = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
mx = 0
mn = 256
# 주어진 입력값의 높이의 최소 최대값
for lst in arr :
    mx = max(mx, max(lst))
    mn = min(mn, min(lst))

# 주어진 입력 조건으로 mn_sec 초기값 설정
mn_sec = 500*500*256*2
h_sol = 0
for h in range(mn, mx+1) :
    remain = B # 인벤토리의 남은 개수
    sec = 0
    for r in range(N) :
        for c in range(M) :
            diff = arr[r][c] - h
            if diff < 0 :       # 메꿔야한다면
                sec += -diff    # 1초, 음수이므로 -1곱함
                remain -= -diff  # 인벤토리 소비
            elif diff > 0 :     # 파야한다면
                sec += 2*diff   # 2초
                remain += diff  # 인벤토리 축적
            # == 0인 경우는 아무것도 하지 않음
    if remain >= 0 :            # 갱신 조건 : 일단 인벤토리가 음수가 되면 안됨
        if sec < mn_sec :       # 최단 시간인 경우
            mn_sec = sec
            h_sol = h
        elif sec == mn_sec and h > h_sol :  # 최단 시간과 동일한 경우
            h_sol = h
print(mn_sec, h_sol)