H, W = map(int, input().split())
arr = [input().rstrip() for _ in range(H)]      # 입력 배열
ans = [[0 for c in range(W)] for r in range(H)] # 정답 배열
# 각 좌표에서 왼쪽으로 구름을 찾을때까지 한칸씩 이동
for r in range(H) :
    for c in range(W) :
        sec = 0         # 0초부터 시작
        found = False   # 구름이 뜨는지 여부
        while c-sec >= 0 :
            if arr[r][c-sec] == 'c' :
                found = True
                break
            # else :
            #     pass
            sec += 1
        if not found :  # 구름을 못찾았다면 -1로 바꿔줌
            sec = -1
        ans[r][c] = sec
for r in range(H) :
    print(*ans[r])
