def oob(r, c):
    return not (0<=r<N and 0<=c<M)

N, M, R = map(int, input().split())

ARR = [list(map(int, input().split())) for _ in range(N)]   # 입력
NEW_ARR = [[0 for _ in range(M)] for _ in range(N)]         # 정답
DS = [(1, 0), (0, 1), (-1, 0), (0, -1)] # 하우상좌

er, ec = 0, 0                  # 사이클 최좌상단 (val의 맨마지막에 들어감)
while NEW_ARR[er][ec] == 0:    # 안채운 곳이 없을때까지
    val = []    # NEW_ARR에 넣을 값
    pos = []    # NEW_ARR에 넣을 위치
    cr, cc, cd = er, ec, 0  # er, ec 다음 것이 가장 먼저 들어가고, er, ec가 가장 늦게 들어감
    while cd < 4:   # 모든 방향으로 진행할때까지
        dr, dc = DS[cd]
        nr, nc = cr+dr, cc+dc
        if oob(nr, nc) or NEW_ARR[nr][nc] != 0: 
            # nr, nc가 범위값이거나 이미 채운 곳이라면 반시계방향으로 90도 틀고, nr, nc 다시 구함
            cd += 1
            continue
        val.append(ARR[nr][nc])     # val과 pos 채우기
        pos.append((nr, nc))
        cr, cc = nr, nc
    rotate_num = R % len(val)
    val = val[-rotate_num:] + val[:-rotate_num]     # R % len(val)만큼 앞으로 회전
    for i, (nr, nc) in enumerate(pos):
        NEW_ARR[nr][nc] = val[i]                    # 회전한 것을 반영해 NEW_ARR에 넣어주기
    er += 1         # er, ec 하나씩 늘려줌
    ec += 1

for l in NEW_ARR:
    print(*l)