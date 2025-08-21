"""
처음 방향과 위치 주어짐
0북 1동 2남 3서
0 청소 X
1 or oob 벽
벽과 청소 O 구별해야함 청소 O => 2

S. 현재칸 미청소시 청소
2. 4칸 중 미청소 없는 경우
    2-1. 벽이 아니라면
        바라보는 방향 유지한 채로 후진 (cd+2)%4
        S로 돌아감 (continue)
    2-2. 벽이라면
        작동 멈춤
3. 미청소 있는 경우
    반시계 방향으로 회전 (cd + 4 - 1)%4
        3-1. 바라보는 앞 칸이 청소되지 않은 경우
            한칸 전진
    S로 돌아감 (continue)

"""
N, M = map(int, input().split())
cr, cc, cd = map(int, input().split())
ARR = [list(map(int, input().split())) for _ in range(N)]

DIR = {0:"북", 1:"동", 2:"남", 3:"서"}
DS = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 0북 1동 2남 3서
# for l in ARR:
#     print(l)

def oob(r, c):
    return not (0<=r<N and 0<=c<M)

cnt = 0
while True: # 0청소X 1벽 2청소O

    # 디버깅용
    # print(cr, cc, cd)
    # ARRR = [lst[:] for lst in ARR]
    # ARRR[cr][cc] = DIR[cd]
    # for l in ARRR:
    #     print(*l)
    # print()




    if ARR[cr][cc] == 0:                                # S. 현재칸 미청소시 청소
        cnt += 1
        ARR[cr][cc] = 2

    is_zero = False                                     # 인접 네 칸 확인해 미청소된 구역 있는지 확인
    for dr, dc in DS:
        nr, nc = cr+dr, cc+dc
        if not oob(nr, nc) and ARR[nr][nc] == 0:
            is_zero = True
            break

    if not is_zero:                                     #2. 4칸 중 미청소 없는 경우
        nd = (cd+2)%4
        dr, dc = DS[nd]
        nr, nc = cr+dr, cc+dc
        if not oob(nr, nc) and ARR[nr][nc] != 1:                # 2-1. 벽이 아니라면
            # cr, cc, cd = nr, nc, nd # (D) "방향을 유지한 채로"   # 바라보는 방향 유지한 채로 후진 (cd+2)%4 + 돌아감 continue
            cr, cc = nr, nc
            continue
        else:                                                   # 2-2. 벽이라면
            break                                               # 작동 멈춤 (loop 탈출)
    else:                                               #3. 미청소 있는 경우
        nd = (cd + 4 - 1)%4                                     # 반시계 방향으로 회전 (cd + 4 - 1)%4
        cd = nd                                                 # 회전은 무조건 해야함
        dr, dc = DS[nd]
        nr, nc = cr+dr, cc+dc
        if ARR[nr][nc] == 0:                                    # 3-1. 바라보는 앞 칸이 청소되지 않은 경우
            cr, cc = nr, nc                                         # 한칸 전진

print(cnt)